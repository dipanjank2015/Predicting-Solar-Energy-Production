import streamlit as st
import pandas as pd
import joblib

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="Solar Energy Production Prediction",
    page_icon="☀️",
    layout="centered"
)

# ----------------------------------------------------
# Load Model
# ----------------------------------------------------
model = joblib.load("solar_energy_prediction.pkl")

# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------
df = pd.read_csv("solar_data_full.csv", low_memory=False)

# ----------------------------------------------------
# Title
# ----------------------------------------------------
st.title("☀️ Solar Energy Production Prediction")

st.markdown("---")

st.subheader("Project Details")

# ----------------------------------------------------
# Dates
# ----------------------------------------------------
data_date = st.date_input("Data Date")

connection_date = st.date_input("Connection Date")

# ----------------------------------------------------
# Categorical Inputs
# ----------------------------------------------------
utility = st.selectbox(
    "Utility",
    sorted(df["Utility"].dropna().unique())
)

city = st.selectbox(
    "City",
    sorted(df["City"].dropna().unique())
)

county = st.selectbox(
    "County",
    sorted(df["County"].dropna().unique())
)

division = st.selectbox(
    "Division",
    sorted(df["Division"].dropna().unique())
)

substation = st.selectbox(
    "Substation",
    sorted(df["Substation"].dropna().unique())
)

circuit = st.selectbox(
    "Circuit ID",
    sorted(df["Circuit_ID"].dropna().astype(str).unique())
)

developer = st.selectbox(
    "Developer",
    sorted(df["Developer"].dropna().unique())
)

metering = st.selectbox(
    "Metering Method",
    sorted(df["Metering Method"].dropna().unique())
)

# ----------------------------------------------------
# Numeric Inputs
# ----------------------------------------------------
zip_code = st.number_input(
    "Zip Code",
    min_value=0.0,
    value=float(df["Zip"].median())
)

pv_kwdc = st.number_input(
    "PV Size (kWdc)",
    min_value=0.0,
    value=float(df["PV_kWdc"].median())
)

pv_kwac = st.number_input(
    "PV Size (kWac)",
    min_value=0.0,
    value=float(df["PV_kWac"].median())
)

storage = st.number_input(
    "Storage Size (kWac)",
    min_value=0.0,
    value=float(df["Storage_kWac"].median())
)

projects = st.number_input(
    "Number of Projects",
    min_value=1,
    value=int(df["Projects"].median())
)

# ----------------------------------------------------
# Derived Features
# ----------------------------------------------------
connection_year = connection_date.year
connection_month = connection_date.month
connection_day = connection_date.day

data_year = data_date.year

# ----------------------------------------------------
# Prediction
# ----------------------------------------------------
if st.button("Predict"):

    input_df = pd.DataFrame({

        "Data_Date": [pd.Timestamp(data_date)],

        "Connection_Date": [pd.Timestamp(connection_date)],

        "Utility": [utility],

        "City": [city],

        "County": [county],

        "Zip": [zip_code],

        "Division": [division],

        "Substation": [substation],

        "Circuit_ID": [circuit],

        "Developer": [developer],

        "Metering Method": [metering],

        "PV_kWdc": [pv_kwdc],

        "PV_kWac": [pv_kwac],

        "Storage_kWac": [storage],

        "Projects": [projects],

        "Connection_Year": [connection_year],

        "Connection_Month": [connection_month],

        "Connection_Day": [connection_day],

        "Data_Year": [data_year]

    })

    prediction = model.predict(input_df)

    st.success("Prediction Completed Successfully!")

    st.markdown("---")

    st.metric(
        label="Predicted Annual Energy Production",
        value=f"{prediction[0]:,.2f} kWh"
    )

    st.markdown("### Model")
    st.info("Random Forest Regressor")

    st.markdown("### Features Used")
    st.write(input_df)