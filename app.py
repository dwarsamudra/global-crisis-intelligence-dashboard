import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Global Crisis Dashboard", layout="wide")

st.title("🌍 Global Crisis Intelligence Dashboard")
st.markdown("AI-powered dashboard for crisis tracking using NLP, sentiment analysis, and severity scoring")

# Load data
df = pd.read_csv("data/global_crisis_final.csv")

# KPI section
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Articles", len(df))
col2.metric("Top Category", df["crisis_category"].mode()[0])
col3.metric("Average Severity", round(df["crisis_severity_score"].mean(), 2))
col4.metric("Top Sentiment", df["sentiment"].mode()[0])

st.divider()

# Category counts
st.subheader("Crisis Category Distribution")
category_counts = df["crisis_category"].value_counts()
fig1, ax1 = plt.subplots()
category_counts.plot(kind="bar", ax=ax1)
ax1.set_xlabel("Crisis Category")
ax1.set_ylabel("Number of Articles")
ax1.set_title("Crisis Distribution by Category")
st.pyplot(fig1)

st.divider()

# Sentiment distribution
st.subheader("Sentiment Distribution")
sentiment_counts = df["sentiment"].value_counts()
fig2, ax2 = plt.subplots()
sentiment_counts.plot(kind="bar", ax=ax2)
ax2.set_xlabel("Sentiment")
ax2.set_ylabel("Number of Articles")
ax2.set_title("Sentiment Analysis of Crisis News")
st.pyplot(fig2)

st.divider()

# Top severe articles
st.subheader("Top 10 Most Severe Crisis Articles")
top_severe = df.sort_values(by="crisis_severity_score", ascending=False)[
    ["title", "crisis_category", "sentiment", "crisis_severity_score"]
].head(10)

st.dataframe(top_severe, use_container_width=True)

st.divider()

# Full dataset preview
st.subheader("Full Dataset Preview")
st.dataframe(df.head(20), use_container_width=True)
