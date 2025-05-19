# 🚍 Sentiment Analysis of Rwanda’s Distance-Based Fare Pricing System

## 📘 Overview

Rwanda recently transitioned from a flat-rate fare model to a **distance-based fare pricing system** in public transportation. This reform aims to promote fairness, sustainability, and efficiency. In response, citizens voiced a range of opinions across social media platforms.

This project showcases a complete end-to-end solution **entirely developed by me** — from **AI-based translation**, **data scraping**, to **natural language processing (NLP)** and interactive **visual analytics**. It’s designed to provide policymakers and stakeholders with actionable insights into how the public perceives the new fare policy.

---

## 📥 Data Collection

Comments were extracted from official and public posts on:
- **Twitter**
- **Instagram**
- **Facebook**
- **LinkedIn**

The data collection process used **Selenium** and **undetected-chromedriver** to simulate user interactions and scroll through dynamic content, enabling the extraction of real-time comments and replies.

Since many of the comments were written in **Kinyarwanda**, I built an **AI-powered translation pipeline** to automatically convert them into English using natural language processing tools. This was a necessary step to allow consistent sentiment analysis across multilingual content.

---

## 🧠 Natural Language Processing & Sentiment Analysis

After translating all comments into English, I applied sentiment analysis using NLP techniques to classify each message as **positive**, **neutral**, or **negative**.  

The results show that **the majority of comments (around 60%) were positive**, reflecting a general support or optimism about the fare system shift. These users appreciate the fairness, flexibility, or innovation it brings.  

About **19.7% of the comments were neutral**, meaning they neither supported nor criticized the change — they mostly included factual statements, questions, or observations.  

Approximately **19.5% of the comments were negative**, highlighting public frustrations or opposition. These comments expressed concerns about implementation, timing, communication, or fairness in specific areas.  

A small percentage, around **0.6%**, were off-topic or unrelated to the fare policy.

---

## ⚙️ Features

-  **AI-generated translation** from Kinyarwanda to English
-  **Real-time sentiment analysis** using NLP
-  Upload your own social media CSV data to explore trends
- 🖥 **Interactive dashboard** built with Streamlit
-  Clear visualizations to help decision-makers understand public opinion
-  Modular and extensible pipeline for future projects

---


## Repository

[GitHub Repository](https://github.com/Kagabo183/SNTIMENT_ANALYSIS-For-Transport-pricing-shifting)

## 🖥️ How to Run Locally
1. **Clone the repository**
   ```bash
   git clone https://github.com/Kagabo183/SNTIMENT_ANALYSIS-For-Transport-pricing-shifting
   cd SNTIMENT_ANALYSIS-For-Transport-pricing-shifting
