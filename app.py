import streamlit as st

loan_page = st.Page("pages/1_loan.py", title="Study loan", icon=":material/calculate:")
compounding_page = st.Page("pages/2_compounding.py", title="Compounding", icon=":material/show_chart:")
income_page = st.Page("pages/3_income.py", title="Income", icon=":material/credit_score:")

pg = st.navigation([loan_page, compounding_page, income_page])
st.set_page_config(page_title="Home", page_icon=":material/home:")
pg.run()