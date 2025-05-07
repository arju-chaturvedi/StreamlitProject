import streamlit as st
import pandas as pd
from textblob import TextBlob
import random
from dotenv import load_dotenv
import os
import csv

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Storytelling Comparison", layout="wide")


def classify_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

@st.cache_data
def load_data():
    df = pd.read_csv("sample_news_sentiment.csv")
    df.dropna(subset=['text', 'title'], inplace=True)
    if 'sentiment_label' not in df.columns:
        df["sentiment_label"] = df["text"].apply(classify_sentiment)
    return df

def log_feedback(data):
    filename = "feedback.csv"
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)


df = load_data()

st.title("📰 Interactive Storytelling Experiment")
st.markdown("Compare **linear vs nonlinear storytelling** by exploring news articles and sharing your experience.")

# Linear story
st.header("📖 Story 1: Linear Format")
story_id = st.number_input("Choose a story number:", min_value=0, max_value=len(df)-1, value=0)
story = df.iloc[story_id]
st.subheader(story["title"])
st.write(story["text"])

with st.form("linear_form"):
    clarity = st.radio("How clear was this story?", ["Very clear", "Somewhat clear", "Unclear"])
    engagement = st.radio("How engaging was the story?", ["Very engaging", "Somewhat engaging", "Not engaging"])
    understanding = st.text_area("What did you understand from this story?")
    submitted = st.form_submit_button("Submit Linear Feedback")
    if submitted:
        log_feedback({
            "story_id": story_id,
            "format": "linear",
            "sentiment": "",
            "title": story["title"],
            "clarity": clarity,
            "engagement": engagement,
            "understanding": understanding,
            "preference": "",
            "match_expectation": ""
        })
        st.success("✅ Linear feedback submitted!")

st.markdown("---")

# Nonlinear story sentiment selection
st.header("📚 Story 2: Nonlinear Format")

if 'sentiment_choice' not in st.session_state:
    st.session_state.sentiment_choice = None
if 'nonlinear_story' not in st.session_state:
    st.session_state.nonlinear_story = None

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("😊 Positive"):
        st.session_state.sentiment_choice = "positive"
        st.session_state.nonlinear_story = None
with col2:
    if st.button("😐 Neutral"):
        st.session_state.sentiment_choice = "neutral"
        st.session_state.nonlinear_story = None
with col3:
    if st.button("😠 Negative"):
        st.session_state.sentiment_choice = "negative"
        st.session_state.nonlinear_story = None

if st.session_state.sentiment_choice:
    filtered_df = df[df["sentiment_label"] == st.session_state.sentiment_choice]
    if not filtered_df.empty:
        if st.session_state.nonlinear_story is None:
            st.session_state.nonlinear_story = random.choice(filtered_df.to_dict("records"))

        nonlinear_story = st.session_state.nonlinear_story

        st.subheader(nonlinear_story["title"])
        st.write(nonlinear_story["text"])

        with st.form("nonlinear_form"):
            match = st.radio("Did the sentiment match your expectation?", ["Yes", "No"])
            nonlin_engagement = st.radio("How engaging was this format?", ["Very engaging", "Somewhat engaging", "Not engaging"])
            nonlin_notes = st.text_area("What did you understand from this story?")
            preference = st.radio("Which format did you prefer overall?", ["Linear", "Nonlinear", "Both equally"])
            submitted2 = st.form_submit_button("Submit Nonlinear Feedback")

            if submitted2:
                log_feedback({
                    "story_id": story_id,
                    "format": "nonlinear",
                    "sentiment": st.session_state.sentiment_choice,
                    "title": nonlinear_story["title"],
                    "clarity": "",
                    "engagement": nonlin_engagement,
                    "understanding": nonlin_notes,
                    "preference": preference,
                    "match_expectation": match
                })
                st.success("✅ Nonlinear feedback submitted!")
    else:
        st.warning(f"No stories found for '{st.session_state.sentiment_choice}' sentiment.")
