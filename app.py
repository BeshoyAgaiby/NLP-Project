import streamlit as st
import joblib

vectorizer = joblib.load("tfidf_vectorizer.joblib")
model = joblib.load("logistic_text_model.joblib")

st.title("Keyword Extraction & Text Classification")

st.write("Enter a text and the model will predict its class.")

user_text = st.text_area("Enter your text here:")

if st.button("Predict"):
    if user_text.strip() != "":
        text_tfidf = vectorizer.transform([user_text])

        prediction = model.predict(text_tfidf)
        probability = model.predict_proba(text_tfidf)

        st.success(f"Predicted Label: {prediction[0]}")
        st.info(f"Prediction Probability: {probability}")
    else:
        st.warning("Please enter some text.")
