# 🔊 Sonar Rock vs Mine Classification Model

Welcome to the Sonar Classification Project! This machine learning web app classifies sonar signals as **Rocks** or **Mines** based on 60 features derived from sonar signal reflections. Built with a **Logistic Regression** model and deployed using **Streamlit**, this project demonstrates a full machine learning pipeline from preprocessing to production.

---

## 🚀 Live Demo

🔗 **Try the deployed Streamlit app**:  
👉 [https://sonar-classification-model-ktwidmitnfseoyyxzwpkwk.streamlit.app/](https://sonar-classification-model-ktwidmitnfseoyyxzwpkwk.streamlit.app/)

---

## 🧠 About the Project

This project includes:
- A clean interface for users to input sonar values
- A pre-trained ML model predicting whether the object is a **Rock** or a **Mine**
- Deployment-ready architecture using Streamlit
- Dataset and training code available in repo and Colab

---

## 📚 Dataset

- The model is trained on the **Sonar Dataset** from the UCI Repository.
- The dataset file is included in the repo.

📂 [`sonar_data.csv`](./sonar_data.csv)

---

## 📓 Google Colab Notebook

🔍 Explore the training process, EDA, and model development step-by-step:  
👉 [Open in Google Colab](https://colab.research.google.com/drive/1tsYnAiBn8gbLONBRo_SS540AUunCOLwu?usp=sharing)

---

## 🛠 Tech Stack

| Tool        | Purpose                        |
|-------------|---------------------------------|
| Python      | Core programming language       |
| Pandas, NumPy | Data manipulation              |
| Scikit-learn | ML model training               |
| Joblib      | Model serialization              |
| Streamlit   | Web app framework                |
| GitHub      | Code versioning and collaboration |

---

## 💻 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/sonar-classification-model.git
cd sonar-classification-model

# 2. Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run sonar_app.py
