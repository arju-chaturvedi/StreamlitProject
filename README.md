from pathlib import Path

# README 
readme_content = """
# 📚 Interactive Storytelling App

This project explores the **impact of linear vs. nonlinear storytelling formats** on reader engagement and comprehension, especially in the context of journalism. It is part of an academic research thesis combining **data science**, **NLP**, and **interactive media**.

---

### 🎯 Project Objectives

- Compare linear and nonlinear storytelling formats using a sentiment-aware news interface.
- Allow users to interact with news stories and submit qualitative feedback.
- Use **TextBlob** for sentiment classification and **Streamlit** for visualization.
- Log anonymous user responses to understand engagement and comprehension patterns.

---

### 🛠️ Technologies Used

| Tool/Library     | Purpose |
|------------------|---------|
| `Streamlit`      | Frontend web app for interaction |
| `TextBlob`       | Sentiment analysis of news articles |
| `pandas`         | Data preprocessing and filtering |
| `python-dotenv`  | Load OpenAI API keys safely |
| `csv` module     | Feedback logging |
| `.env`           | Stores private environment variables like API keys |

---

### 🧠 How It Works

#### 👓 Linear Mode:
- Displays a full news article with a traditional sequential structure.
- The user provides clarity, engagement, and understanding feedback.

#### 🎛️ Nonlinear Mode:
- The user selects **sentiment filters** (😊 Positive, 😐 Neutral, 😠 Negative).
- They receive a story that matches the sentiment.
- Feedback includes expectation alignment, engagement, comprehension, and preference.

#### 📊 Feedback Logging:
All feedback is saved to `feedback.csv` for later analysis.

---

### 📸 Interface Overview

This shows the linear vs nonlinear comparison screen:

![Storytelling App](https://github.com/arju-chaturvedi/StreamlitProject/blob/main/Screenshot%202025-05-08%20at%201.57.03%20AM.png)


### 🚀 Run Locally

#### 1. Clone the Repo

```bash
git clone https://github.com/arju-chaturvedi/StreamlitProject.git
cd StreamlitProject
