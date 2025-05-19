import streamlit as st
import pandas as pd
from deep_translator import GoogleTranslator

st.set_page_config(page_title="AI Comment Translator", layout="centered")

st.title("📄 Auto Translate Comments to English")

uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Read file depending on type
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("✅ File loaded successfully!")
    st.dataframe(df.head())

    # Choose which column to translate
    text_column = st.selectbox("Select the column to translate", df.columns)

    if st.button("🔁 Translate to English"):
        try:
            with st.spinner("Translating comments..."):
                df["Translated_Comment"] = df[text_column].apply(
                    lambda x: GoogleTranslator(source='auto', target='en').translate(str(x))
                )

            st.success("✅ Translation complete!")
            st.dataframe(df[["Name", "Handle", text_column, "Translated_Comment"]].head())

            # Save to CSV for download
            output_file = "translated_output.csv"
            df.to_csv(output_file, index=False)

            with open(output_file, "rb") as f:
                st.download_button(
                    label="⬇️ Download Translated File",
                    data=f,
                    file_name="translated_output.csv",
                    mime="text/csv"
                )

        except Exception as e:
            st.error(f"Something went wrong: {e}")
