import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import re
import textwrap
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud

# Download VADER lexicon
nltk.download("vader_lexicon")

# App title
st.title("Sentiment Analysis of RURA Comments")

# --------------------------------------------------------
# Upload CSV file
# --------------------------------------------------------
uploaded_file = st.file_uploader("Upload the RURA Comments CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='latin1')

    # --------------------------------------------------------
    # Clean Text
    # --------------------------------------------------------
    df_clean = df[df["Translated Comments (English)"].notnull()].copy()
    df_clean["Translated Comments (English)"] = df_clean["Translated Comments (English)"].str.strip()
    df_clean = df_clean[df_clean["Translated Comments (English)"] != ""]
    df_clean.reset_index(drop=True, inplace=True)

    def clean_text(text):
        text = text.lower()
        text = re.sub(r'[\U0001F600-\U0001FAFF\U00002700-\U000027BF]', '', text)
        text = re.sub(r'[^\w\s]', '', text)
        text = ' '.join(text.split())
        return text if text else 'na'

    df_clean['Cleaned Translated Comments (English)'] = df_clean['Translated Comments (English)'].apply(clean_text)

    # --------------------------------------------------------
    # Sentiment Analysis
    # --------------------------------------------------------
    vader = SentimentIntensityAnalyzer()
    df_clean["Compound"] = df_clean["Cleaned Translated Comments (English)"].apply(lambda x: vader.polarity_scores(x)["compound"])

    def is_no_concern(text):
        text = text.strip().lower()
        return text in ['no comment', 'none', 'n/a', 'nothing', 'no concerns', 'na', 'nil']

    df_clean["No Concern"] = df_clean["Cleaned Translated Comments (English)"].apply(is_no_concern)

    def assign_label(row):
        if row["No Concern"]:
            return "No Concern"
        elif row["Compound"] >= 0.05:
            return "Positive"
        elif row["Compound"] <= -0.05:
            return "Negative"
        else:
            return "Neutral"

    df_clean["Sentiment Label"] = df_clean.apply(assign_label, axis=1)

    # --------------------------------------------------------
    # Sentiment Distribution Plot
    # --------------------------------------------------------
    st.subheader("Sentiment Distribution")
    colors = {
        "Negative": "#f08080",
        "Neutral": "#f7e967",
        "Positive": "#90ee90",
        "No Concern": "#d3d3d3"
    }
    fig1, ax1 = plt.subplots(figsize=(10, 9))
    sns.countplot(data=df_clean, x="Sentiment Label",
                  order=["Negative", "Neutral", "Positive", "No Concern"],
                  palette=colors, ax=ax1)

    total = len(df_clean)
    for bar in ax1.patches:
        count = bar.get_height()
        percent = 100 * count / total
        ax1.text(bar.get_x() + bar.get_width() / 2,
                 count + 1,
                 f'{count}\n({percent:.1f}%)',
                 ha='center', fontsize=10)

    st.pyplot(fig1)

    # --------------------------------------------------------
    # Top 5 Positive & Negative Comments
    # --------------------------------------------------------
    st.subheader("Top 5 Positive & Negative Comments")

    top_neg = df_clean[df_clean["Sentiment Label"] == "Negative"].sort_values("Compound").head(5)
    top_pos = df_clean[df_clean["Sentiment Label"] == "Positive"].sort_values("Compound", ascending=False).head(5)
    top = pd.concat([top_neg, top_pos])
    top["Sentiment"] = ["Negative"] * len(top_neg) + ["Positive"] * len(top_pos)

    def wrap(text, width=90):
        return "\n".join(textwrap.wrap(text, width))

    top["Wrapped"] = top["Translated Comments (English)"].apply(wrap)

    fig2, ax2 = plt.subplots(figsize=(12, 6))
    sns.barplot(data=top, x="Compound", y="Wrapped", hue="Sentiment",
                palette={"Positive": "green", "Negative": "red"}, ax=ax2)
    ax2.set_xlabel("Sentiment Score")
    ax2.set_ylabel("Comment")
    st.pyplot(fig2)

    # --------------------------------------------------------
    # Sentiment Compound Score Histogram
    # --------------------------------------------------------
    st.subheader("Compound Score Distribution")
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    sns.histplot(df_clean["Compound"], bins=20, kde=True, color='skyblue', ax=ax3)
    ax3.axvline(0, color='red', linestyle='--', label='Neutral Boundary')
    ax3.legend()
    st.pyplot(fig3)


        # Platform Distribution
    st.subheader("Platform Distribution")

    platform_counts = df["Platform"].value_counts()

    fig, ax = plt.subplots(figsize=(6, 4))
    colors = sns.color_palette("pastel")[:len(platform_counts)]  # Soft, professional color palette

    ax.bar(platform_counts.index, platform_counts.values, color=colors)
    ax.set_title("Platform Distribution", fontsize=14)
    ax.set_xlabel("Platform", fontsize=12)
    ax.set_ylabel("Number of Comments", fontsize=12)
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    for i, v in enumerate(platform_counts.values):
        ax.text(i, v + 0.5, str(v), ha='center', va='bottom', fontsize=10)

    st.pyplot(fig)


    # --------------------------------------------------------
    # Word Clouds
    # --------------------------------------------------------
    st.subheader("Word Clouds")

    pos_text = " ".join(df_clean[df_clean["Sentiment Label"] == "Positive"]["Translated Comments (English)"])
    neg_text = " ".join(df_clean[df_clean["Sentiment Label"] == "Negative"]["Translated Comments (English)"])

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Positive Comments**")
        wc_pos = WordCloud(background_color='white', colormap='Greens').generate(pos_text)
        fig4, ax4 = plt.subplots()
        ax4.imshow(wc_pos, interpolation='bilinear')
        ax4.axis("off")
        st.pyplot(fig4)

    with col2:
        st.markdown("**Negative Comments**")
        wc_neg = WordCloud(background_color='white', colormap='Reds').generate(neg_text)
        fig5, ax5 = plt.subplots()
        ax5.imshow(wc_neg, interpolation='bilinear')
        ax5.axis("off")
        st.pyplot(fig5)

    