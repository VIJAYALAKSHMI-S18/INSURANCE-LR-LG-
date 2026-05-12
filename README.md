# INSURANCE-LR-LG
# Insurance Purchase Prediction System

## Overview

This project is a Machine Learning-based web application that predicts whether a person is likely to purchase insurance based on their age. The model is built using Logistic Regression and deployed using Streamlit for interactive user input and prediction.

## Problem Statement

To build a classification model that predicts insurance purchase decisions based on demographic data (age).

## Dataset

- Input Feature: Age  
- Target Variable: Bought Insurance (0 = No, 1 = Yes)

## Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Streamlit  

## Machine Learning Model

- Algorithm: Logistic Regression  
- Purpose: Binary Classification  
- Output: Probability of insurance purchase

## Project Workflow

1. Data Loading and Preprocessing  
2. Exploratory Data Analysis  
3. Model Training using Logistic Regression  
4. Model Evaluation  
5. Model Serialization using Pickle  
6. Web App Development using Streamlit  

## Model File

The trained model is saved as:

- `model.pkl`

## Installation

Install required dependencies using:

```bash
pip install -r requirements.txt