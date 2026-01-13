import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("spam_prediction.pkl","rb"))
vectorizer = pickle.load(open("vertorize_model.pkl","rb"))

st.set_page_config(
    page_title="Spam Email Detector",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Spam Email Detection")
st.markdown(
    "Automatically detect whether an email is Spam or Non-Spam using Machine Learning."
)

email_text = st.text_area(
    "✉️ Enter the email content:",
    height=200,
    placeholder="Paste your email here…"
)

if st.button("🔍 Analyser"):
    if email_text.strip() == "":
        st.warning("⚠️ please Enter the text.")
    else:
        
        email_vector = vectorizer.transform([email_text])
        prediction = model.predict(email_vector)[0]
        proba = model.predict_proba(email_vector)

        if prediction == 1:
            st.error(f"SPAM détecté (confiance : {max(proba[0])*100:.2f}%)")
            st.progress(int(max(proba[0]) * 100))
        else:
            st.success(f"Email sûr (confiance : {max(proba[0])*100:.2f}%)")
            st.progress(int(max(proba[0]) * 100))
st.markdown("---")
st.caption("Projet ML | CREE PAR MOHAMMED SADIK ")
