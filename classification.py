import streamlit as st
import pandas as pd
import numpy as np
df = pd.read_csv('https://raw.githubusercontent.com/amirulerfn/jie43202/refs/heads/main/Toddler%20Autism%20dataset%20July%202018.csv')
st.write(df)