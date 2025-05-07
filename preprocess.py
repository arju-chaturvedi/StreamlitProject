import pandas as pd
from textblob import TextBlob
import nltk

# Download required NLTK models
nltk.download('punkt')

# Load the dataset
df = pd.read_csv("sample_news_sentiment.csv")

# Rename 'description' to 'text' if needed
if "description" in df.columns and "text" not in df.columns:
    df["text"] = df["description"]

# Drop empty rows
df.dropna(subset=['text', 'title'], inplace=True)

# Sentiment function
def classify_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

# Add sentiment label column
df["sentiment_label"] = df["text"].apply(classify_sentiment)

# Save the final dataset
df.to_csv("sample_news_sentiment.csv", index=False)
print("✅ Sentiment labels added and file saved.")
