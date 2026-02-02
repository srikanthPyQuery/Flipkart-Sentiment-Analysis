# Flipkart-Sentiment-Analysis
Sentiment Analysis of Flipkart Product Reviews using ML and Streamlit
📊 Sentiment Analysis of Real-Time Flipkart Product Reviews
🔍 Project Overview

This project performs binary sentiment classification (Positive / Negative) on real-time Flipkart product reviews using machine learning.
The final trained model is deployed using Streamlit for real-time user inference.

Product: YONEX MAVIS 350 Nylon Shuttle
Total Reviews: 8,518

🎯 Objective

Classify customer reviews as positive or negative

Identify pain points from negative reviews

Select the best-performing model using cross-validation

Deploy the model using Streamlit for real-time prediction

📁 Repository Structure
Flipkart-Sentiment-Analysis/
│
├── data.csv
├── model_training_and_selection.ipynb
├── final_sentiment_model.pkl
├── app.py
└── README.md

🧠 Model Selection

Text Vectorization: TF-IDF

Models Evaluated:

Logistic Regression

Linear SVM

Multinomial Naive Bayes

Hyperparameter tuning using Optuna

Evaluation Metric: F1 Score

Cross-validated model selection

🏆 Best Model

The best-performing model was selected based on cross-validated F1 score and evaluated on an unseen test dataset.

📦 Trained Model

Download the trained model here:
➡️ final_sentiment_model.pkl

🚀 Streamlit Application

The Streamlit app allows users to input a review and get instant sentiment prediction.

File: app.py

Run Locally
streamlit run app.py

🔍 Pain Point Analysis

Negative reviews were analyzed to extract frequent words and phrases, highlighting customer dissatisfaction areas such as quality issues and unmet expectations.

🛠️ Technologies Used

Python

Scikit-learn

Optuna

Streamlit

NLTK

Pandas

NumPy
