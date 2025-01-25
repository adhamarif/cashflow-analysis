import streamlit as st
import pandas as pd

def calculate_investment_growth(principal, monthly_deposit, annual_interest_rate, months):
    monthly_balance = []
    total_deposits = []
    deposit_amount = 0

    for i in range(1, months + 1):
        principal = (principal + monthly_deposit) * (1 + annual_interest_rate / 12)
        monthly_balance.append(principal)
        deposit_amount += monthly_deposit
        total_deposits.append(deposit_amount)

    annual_balance = [monthly_balance[i] for i in range(11, len(monthly_balance), 12)]
    annual_deposits = [total_deposits[i] for i in range(11, len(total_deposits), 12)]
    years_invested = [i for i in range(1, len(annual_balance) + 1)]

    return annual_balance, annual_deposits, years_invested

st.title('Investment Growth Calculator')
st.caption("""This calculator helps you to calculate the growth of your investment over time.""")

col1, col2 = st.columns(2)

with col1:
    PRINCIPAL = st.number_input('Initial Investment', value=1000)
    MONTHLY_DEPOSIT = st.number_input('Monthly Deposit', value=100)

with col2:
    ANNUAL_INTEREST_RATE = st.number_input('Annual Interest Rate (%)', value=5)
    n = st.number_input('Number of years', value=25) * 12


annual_balance, annual_deposits, years_invested = calculate_investment_growth(PRINCIPAL, MONTHLY_DEPOSIT, ANNUAL_INTEREST_RATE / 100, n)

df = pd.DataFrame({'Years': years_invested, 'Annual Deposits': annual_deposits, 'Annual Balance': annual_balance})
tab1, tab2 = st.tabs(['Chart', 'Table'])

with tab1:
    st.line_chart(df[['Annual Deposits', 'Annual Balance']])

with tab2:
    st.dataframe(df, hide_index=True)