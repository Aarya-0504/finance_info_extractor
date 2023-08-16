import streamlit as st
import pandas as pd
import openai_func
c1,c2=st.columns([3,2])

financial_df=pd.DataFrame({
        "Measure":["company name","Stock", "Revenue","Net Income", "Eps"],
        "Value":["","","","",""]
    })

with c1:
    st.title("Financial Data Extraction Tool:")
    news_article=st.text_area("Paste your financial article here",height=200)
    extract=st.button("Extract")
    if extract:
        financial_df=openai_func.extract_financial_data(news_article)



with c2: 
    st.markdown("<br/>" * 6, unsafe_allow_html=True)  # Creates 5 lines of vertical space
    st.dataframe(financial_df,width=300)