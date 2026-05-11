import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

# load dataset
df = pd.read_csv("insurance_data.csv")

# training data
X = df[['age']]
y = df['bought_insurance']

# train model
model = LogisticRegression()
model.fit(X, y)

# app title
st.title("Insurance Prediction App")

# user input
age = st.number_input("Enter Age")

# predict button
if st.button("Predict"):

    prediction = model.predict([[age]])

    if prediction[0] == 1:
        st.success("Person Will Buy Insurance")
    else:
        st.error("Person Will NOT Buy Insurance")