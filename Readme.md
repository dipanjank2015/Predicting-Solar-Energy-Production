# ☀️ Solar Energy Production Prediction using Machine Learning

---

## 🚀 Live Demo

👉 **Streamlit App:**  
"https://predicting-solar-energy-appuction-du3bvcxprxn5sg2dndcrjm.streamlit.app/"

---

## 📌 Project Overview

This project predicts **Annual Solar Energy Production (kWh)** using a **Random Forest Regressor** model. The application is built with **Streamlit**, allowing users to enter solar project details and receive an instant prediction of annual energy generation.

The project demonstrates an end-to-end Machine Learning workflow, including:

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Model Training
- Model Evaluation
- Model Deployment using Streamlit

---

## 🎯 Problem Statement

Accurately estimating annual solar energy production is important for:

- Solar project planning
- Investment analysis
- Energy demand forecasting
- Infrastructure optimization
- Renewable energy management

This project provides an intelligent prediction system based on historical solar project data.

---

## 📂 Dataset Information

The dataset includes information such as:

- Data Date
- Connection Date
- Utility
- City
- County
- ZIP Code
- Division
- Substation
- Circuit ID
- Developer
- Metering Method
- PV System Size (kWdc)
- PV System Size (kWac)
- Storage Size (kWac)
- Number of Projects
- Connection Year
- Connection Month
- Connection Day
- Data Year

**Target Variable**

- Annual Energy Production (kWh)

---

## 🤖 Machine Learning Model

**Algorithm Used**

- Random Forest Regressor

The model is deployed using a Scikit-learn Pipeline, which includes:

- Missing Value Imputation
- Standard Scaling
- One-Hot Encoding
- Random Forest Regression

---

## 📈 Model Performance

| Metric | Value |
|---------|-------|
| MAE | **4.15** |
| RMSE | **9.99** |
| R² Score | **0.9999** |

---

## 🖥️ Streamlit Application Features

- Interactive User Interface
- Automatic Feature Processing
- Instant Annual Energy Prediction
- Dropdown Selection for Categorical Features
- Date Selection
- Numerical Inputs
- Machine Learning Prediction in Real-Time

---

## 📁 Project Structure

```text
Predicting-Solar-Energy-Production/
│
├── app.py
├── predicting_solar_energy_production.py
├── Predicting_Solar_Energy_Production.ipynb
├── solar_energy_prediction.pkl
├── solar_data_full.csv
├── requirements.txt
├── README.md
├── feature_importance.csv
├── Model_Metrics.csv
├── predictions.csv
├── Predicting_Solar_Energy_Production.pptx
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Predicting-Solar-Energy-Production.git
```

Go to project directory

```bash
cd Predicting-Solar-Energy-Production
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run app.py
```

---

## 🧪 Input Features

The Streamlit application accepts the following inputs:

- Data Date
- Connection Date
- Utility
- City
- County
- ZIP Code
- Division
- Substation
- Circuit ID
- Developer
- Metering Method
- PV Size (kWdc)
- PV Size (kWac)
- Storage Size (kWac)
- Number of Projects

The application automatically generates:

- Connection Year
- Connection Month
- Connection Day
- Data Year

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib
- Jupyter Notebook

---

## 📷 Application Preview

### Home Page

_Add a screenshot here_

Example:

```text
images/home_page.png
```

### Prediction Result

_Add a screenshot here_

Example:

```text
images/prediction_result.png
```

---

## 💡 Future Improvements

- Deploy on AWS/Azure
- Add Interactive Charts
- Real-Time Solar API Integration
- Multiple Machine Learning Models
- Model Comparison Dashboard
- Explainable AI (SHAP)

---

## 👨‍💻 Author

**Dipanjan**

Data Scientist | Machine Learning Enthusiast

### GitHub

https://github.com/dipanjank2015

### LinkedIn

https://www.linkedin.com/in/dipanjankarmakar-ds/

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!