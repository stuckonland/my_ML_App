{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5b32931d-2e74-4af4-b517-68bc898d1a8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1290b075-300a-4c89-bf96-9bfaa7eacb68",
   "metadata": {},
   "outputs": [],
   "source": [
    "with st.sidebar:\n",
    "    Income = st.number_input(\"Income (1 = Less than $10,000, 2 = 10 to under $20,000, 3 = 20 to under $30,000, 4 = 30 to under $40,000, 5 = 40 to under $50,000, 6 = 50 to under $75,000, 7 = 75 to under $100,000, 8 = 100 to under $150,000, 9 = $150,000 or more)\", 1, 9)\n",
    "    Education = st.number_input(\"Education (1 = Less than high school (Grades 1-8 or no formal schooling), 2 = High school incomplete (Grades 9-11 or Grade 12 with NO diploma), 3 = High school graduate (Grade 12 with diploma or GED certificate), 4 = Some college, no degree (includes some community college), 5 = Two-year associate degree from a college or university, 6 = Four-year college or university degree/Bachelor's degree (e.g., BS, BA, AB), 7 =  Some postgraduate or professional schooling, no postgraduate degree (e.g. some graduate school) 8 = Postgraduate or professional degree, including master's, doctorate, medical or law degree (e.g., MA, MS, PhD, MD, JD))\", 1, 8)\n",
    "    Parent = st.number_input(\"Parent (0=no, 1=yes)\", 0, 1)\n",
    "    Married = st.number_input(\"Married (0=no, 1=yes)\", 0, 1)\n",
    "    Female = st.number_input(\"Female (0=no, 1=yes)\", 0, 1)\n",
    "    Age = st.number_input(\"Age (low=1 to high=98)\", 1, 98)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
