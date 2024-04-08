import pickle
import streamlit as st
import pandas as pd
import numpy as np

# import the model
model = pickle.load(open('Model.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Credit Card Predictor")

columns = ['Gender', 'Has a car', 'Has a property', 'Children count', 'Income',
           'Employment status', 'Education level', 'Marital status', 'Dwelling',
           'Age', 'Employment length in years', 'Has a work phone', 'Has a phone',
           'Has an email', 'Job title', 'Family member count', 'Account age']

# Gender
gender = st.selectbox('Gender', ['Male', 'Female'])

# Has a Car
hasACar = st.selectbox('Has a Car', ["Yes", "No"])

# Has a Property
hasAProperty = st.selectbox('Has a Property', ["Yes", "No"])

# Children count
childrenCount = st.number_input('Children Count')

# Income
income = st.number_input('Income')

# Employment status
employmentStatus = st.selectbox('Employment Status', ['Working', 'Pensioner', 'Commercial associate', 'State servant'])

# Education level
educationLevel = st.selectbox('Education Level', ['Higher education', 'Secondary / secondary special', 'Other'])

# Marital status
maritalStatus = st.selectbox('Marital Status', ['Married', 'Single / not married', 'Civil marriage', 'Other'])

# Dwelling
dwelling = st.selectbox('Dwelling', ['House / apartment', 'Other'])

# Age
age = st.number_input('Age')

# Employment length in years
employmentLengthInYears = st.number_input('Employment length in years')

# Has a work phone
hasAWorkPhone = st.selectbox('Has a Work Phone', ['Yes', 'No'])

# Has a phone
hasAPhone = st.selectbox('Has a Phone', ['Yes', 'No'])

# Has an email
hasAnEmail = st.selectbox('Has an Email', ['Yes', 'No'])

# Job title
jobTitle = st.selectbox('Job Title', ['Sales staff', 'Unemployed', 'Accountants', 'Managers',
                                      'Core staff', 'High skill tech staff', 'Laborers', 'Drivers', 'Other'])

# Family member count
familyMemberCount = st.number_input('Family Member Count')

# Account age
accountAge = st.number_input('Account Age')

outputWithYesNo = [hasAWorkPhone, hasAPhone, hasAnEmail, hasACar, hasAProperty]
if st.button('Is Risk High'):
    # query
    # Setting the value of the parameter to number.
    if hasAWorkPhone == 'Yes':
        hasAWorkPhone = 1
    else:
        hasAWorkPhone = 0

    if hasAPhone == 'Yes':
        hasAPhone = 1
    else:
        hasAPhone = 0

    if hasAnEmail == 'Yes':
        hasAnEmail = 1
    else:
        hasAnEmail = 0

    if hasACar == "Yes":
        hasACar = 1
    else:
        hasACar = 0

    if hasAProperty == "Yes":
        hasAProperty = 1
    else:
        hasAProperty = 0

    query = np.array([gender, hasACar, hasAProperty, childrenCount, income,
                      employmentStatus, educationLevel, maritalStatus, dwelling,
                      age, employmentLengthInYears, hasAWorkPhone, hasAPhone,
                      hasAnEmail, jobTitle, familyMemberCount, accountAge])

    query = query.reshape(1, 17)
    st.title("Is Risk High:   " + str(int(model.predict(query)[0])))
