import pandas as pd
import warnings
import streamlit as st

data = pd.read_excel("Dip.xlsx",sheet_name=0)

st.set_page_config(layout='wide')




st.markdown("<h1 style='text-align: center;'>**CALIBRATION CHART: 20KL HORIZONTAL  UNDER GROUND  TANK **</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;'>**A V R AGENCY**</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>*INDIAN OIL CORPORATION LTD*</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    A = st.number_input('**Key in the DIP Value**')

if st.button('CONVERT'):
    B=int(A)
    C=data[data['DIP']==B]
    C['Remainder'] = ((A-B)*10)
    C['Rem_value'] = (C['Remainder']*C['DIFF'])
    C['Final'] = C['Volume']+C['Rem_value']
    C['Final_Rounded'] = round(C['Final'],2)
    with col2:
        st.write(C['Final_Rounded'].values)
        st.dataframe(C)
