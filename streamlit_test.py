import streamlit as st 
pip install scikit-learn

with st.sidebar:
    Income = st.number_input("Income (1 = Less than 10,000, 2 = 10 to under 20,000, 3 = 20 to under 30,000, 4 = 30 to under 40,000, 5 = 40 to under 50,000, 6 = 50 to under 75,000, 7 = 75 to under 100,000, 8 = 100 to under 150,000, 9 = 150,000 or more)", 1, 9)
    Education = st.number_input("Education (1 = Less than high school (Grades 1-8 or no formal schooling), 2 = High school incomplete (Grades 9-11 or Grade 12 with NO diploma), 3 = High school graduate (Grade 12 with diploma or GED certificate), 4 = Some college, no degree (includes some community college), 5 = Two-year associate degree from a college or university, 6 = Four-year college or university degree/Bachelor's degree (e.g., BS, BA, AB), 7 =  Some postgraduate or professional schooling, no postgraduate degree (e.g. some graduate school) 8 = Postgraduate or professional degree, including master's, doctorate, medical or law degree (e.g., MA, MS, PhD, MD, JD))", 1, 8)
    Parent = st.number_input("Parent (0=no, 1=yes)", 0, 1)
    Married = st.number_input("Married (0=no, 1=yes)", 0, 1)
    Female = st.number_input("Female (0=no, 1=yes)", 0, 1)
    Age = st.number_input("Age (low=1 to high=98)", 1, 98)


TestA = [Income, Education, Parent, Married, Female, Age]

import pandas as pd
import numpy as np

s = pd.read_csv('https://raw.githubusercontent.com/stuckonland/my_ML_App/main/social_media_usage.csv')
def clean_sm(x): #function that returns a boolean for positive use
    return np.where(x == 1, 1, 0)
data = {'col1': [0, 1, 0], 'col2': [1, 0, 1]} #New dataframe to test
toy_df = pd.DataFrame(data)
cleaned_df = toy_df.apply(clean_sm) #testing the new dataframe
ss = s.assign(sm_li=lambda x: clean_sm(x['web1h'])) # creates a new column called 'sm_li' that tests whether the respondant is on linkedin
ss = ss.dropna() 
ss['income'] = np.where((ss['income'] >= 1) & (ss['income'] <= 9), ss['income'], np.nan)
ss['education'] = np.where((ss['educ2'] >= 1) & (ss['educ2'] <= 8), ss['educ2'], np.nan)
ss['parent'] = np.where(ss['par'] == 1, 1, 0)
ss['married'] = np.where(ss['marital'].isin([1, 2]), 1, 0)
ss['female'] = np.where(ss['gender'] ==2,1, 0)
ss['age'] = np.where((ss['age'] <= 98) & (ss['age'] >= 0), ss['age'], np.nan)
ss = ss.dropna() #drops NA
ss = ss[['income', 'education', 'parent', 'married', 'female', 'age', 'sm_li']]
correlation_matrix = ss.corr()


from sklearn.model_selection import train_test_split
ss.reset_index(drop=True, inplace=True)
ss.dropna(inplace=True)

y = ss['sm_li'].reset_index(drop=True).dropna()
x = ss.drop('sm_li',axis=1).reset_index(drop=True).dropna()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=123)

from sklearn.linear_model import LogisticRegression

logreg_model = LogisticRegression(class_weight='balanced', random_state=123)

logreg_model.fit(x_train, y_train)

y_pred = logreg_model.predict(x_test)

prob1 = logreg_model.predict_proba([TestA])

prob1_class1 = prob1[0, 1]

print(f'\nProbability of LinkedIn use for the defined person: {prob1_class1:.4f}')    
