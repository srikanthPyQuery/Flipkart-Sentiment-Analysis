import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ---------- Text Cleaning (SAME as training) ----------
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

stop_words = set(stopwords.words('english'))
negations = {'not', 'no', 'nor', 'never'}
stop_words = stop_words - negations

lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = [
        lemmatizer.lemmatize(word)
        for word in text.split()
        if word not in stop_words and len(word) > 2
    ]
    return ' '.join(tokens)

# ---------- Load Model ----------
model = joblib.load("final_sentiment_model.pkl")

# ---------- Streamlit UI ----------
st.set_page_config(page_title="Flipkart Review Sentiment", layout="centered")

st.title("Flipkart Product Review Sentiment Analysis")
st.write("Enter a product review to predict sentiment")

user_input = st.text_area("Customer Review", height=150)

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a review.")
    else:
        cleaned_text = clean_text(user_input)
        prediction = model.predict([cleaned_text])[0]

        if prediction == 1:
            st.success("Positive Review")
        else:
            st.error("Negative Review")
