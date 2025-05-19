# Sentiment Analysis of Rwanda’s Distance-Based Fare Pricing System

## Project Overview

Rwanda recently shifted from flat-rate fares to a distance-based fare pricing model in public transport, aiming to create a fairer and more sustainable transport system. This change has sparked varied reactions across social media platforms like Twitter, Instagram, and Facebook, as well as other communication channels.

This project analyzes public sentiment towards this new fare system by extracting, processing, and visualizing data from multiple sources. The goal is to provide policymakers with actionable insights into public perception trends, key concerns, and potential misinformation.

## Data Sources
## Data Collection

I collected comments from a specific tweet and related posts across social media platforms announcing the trial of the new **distance-based transport fare system**. The script uses **Selenium** and **undetected-chromedriver** to simulate user scrolling and extract public replies. Additionally, the collected data—originally in Kinyarwanda—was translated into English to enable effective Natural **Language Processing (NLP)** and sentiment analysis.

## The following are Social medias I used:
- Twitter posts and replies  
- Instagram comments  
- Facebook comments
- LinkedIn  

These datasets contain user-generated content reflecting real-time opinions and discussions about the distance-based fare system.

## Sentiment Analysis Summary

The sentiment analysis of the collected comments shows that:

- **Positive sentiments dominate**, making up approximately **60.2%** of the comments. This indicates that most citizens view the distance-based fare system favorably or are supportive of the change.

- **Neutral sentiments account for about 19.7%** of the comments. These represent users who may be undecided, seeking more information, or simply sharing observations without strong opinions.

- **Negative sentiments constitute roughly 19.5%** of the feedback. These comments highlight concerns, frustrations, or opposition towards aspects of the new pricing model, signaling areas where policymakers should focus on communication and improvement.

- A small fraction, **0.6% of comments, express no particular concern** related to the fare change, possibly representing unrelated or off-topic discussions.

## Features

- Upload CSV datasets containing social media comments  
- Display sentiment distribution and platform usage with clear visualizations  
- Interactive dashboard built with Streamlit for easy exploration  
- Insights to guide policymakers on public opinion and areas needing attention  

## How to Run

1. Clone the repository  
2. Install dependencies: `pip install -r requirements.txt`  
3. Run the Streamlit app: `streamlit run app.py`  
4. Upload your CSV dataset via the dashboard and explore the sentiment analysis  
## Deployment

The app is deployed and accessible at:  
[https://sntiment-analysis-for-transport-pricing.onrender.com](https://sntiment-analysis-for-transport-pricing.onrender.com)



## Repository

[GitHub Repository](https://github.com/Kagabo183/SNTIMENT_ANALYSIS-For-Transport-pricing-shifting)


