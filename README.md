# Spam Email Detector

📧 **Project:** Spam Email Detection using Machine Learning  
🛠 **Tech Stack:** Python, Scikit-learn, TF-IDF, Logistic Regression, Streamlit  

---

## 🔹 Description

This project is a **Spam Email Detection system** that classifies emails as **Spam** or **Non-Spam** (Ham) using **Machine Learning**.  
The model is trained on a **public Kaggle dataset**, and the application provides an **interactive UI** to test emails in real-time.

---

## 🔹 Features

- Preprocessing of raw email data:
  - Handling missing values
  - Text cleaning
  - Removal of stopwords
- Vectorization using **TF-IDF** (`TfidfVectorizer`)
- Classification with **Logistic Regression**
- Model saving/loading using **Pickle**
- Evaluation metrics:
  - Accuracy: ~97%
- Interactive **Streamlit UI**:
  - Enter email content
  - Display prediction (Spam / Non-Spam)
  - Show model confidence (%)

---

## 🔹 Dataset

The model was trained using a **public Kaggle dataset**.  
- The dataset itself is **not included** due to licensing restrictions.  
- You can access the original dataset here: [Kaggle Spam Email Dataset](https://www.kaggle.com/uciml/sms-spam-collection-dataset)  

---

## 🔹 Usage

1. Open the Streamlit app in your browser.

2. Paste or type an email in the input field.

3. Click Analyze.

4. The app will display:

   . Prediction: SPAM or Non-Spam

   . Confidence of the prediction
git clone https://github.com/yourusername/spam-email-detector.git
cd spam-email-detector
