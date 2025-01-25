import streamlit as st
import pandas
import plotly.express as px
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')

# Where USD is the base currency you want to use
#url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

# Making our request
#response = requests.get(url)
#data = response.json()

#EURO_TO_MYR = data['conversion_rates']['MYR']

EURO_TO_MYR = 4.6

    


ANNUAL_INCOME = 50000
NON_TAXABLE_INCOME = 12096

# Insurance rate (Deducted from Gross)
HEALTH_INSURANCE_RATE = 0.079
PENSION_RATE = 0.093
UNEMPLOYMENT_INSURANCE_RATE = 0.013
EXTRA_INSURANCE_RATE = 0.023

# Tax rate (Deducted from Taxable Income)
INCOME_TAX_RATE = 0.18


def calculate_net_salary(annual_salary, non_taxable_income, health_insurance_rate, pension_rate, unemployment_insurance_rate, extra_insurance_rate, income_tax_rate):
    monthly_salary = annual_salary / 12
    health_insurance = monthly_salary * health_insurance_rate
    pension = monthly_salary * pension_rate
    unemployment_insurance = monthly_salary * unemployment_insurance_rate
    extra_insurance = monthly_salary * extra_insurance_rate
    taxable_income = monthly_salary - non_taxable_income / 12
    income_tax = taxable_income * income_tax_rate
    net_salary = monthly_salary - health_insurance - pension - unemployment_insurance - extra_insurance - income_tax
    return net_salary


def plot_sunburst_charts():
    labels = ['Health Insurance', 'Pension', 'Unemployment Insurance', 'Extra Insurance', 'Income Tax', 'Net Salary']
    parents = ['Monthly Contribution', 'Monthly Contribution', 'Monthly Contribution', 'Monthly Contribution', 'Monthly Contribution', '']
    values = [
        ANNUAL_INCOME * HEALTH_INSURANCE_RATE / 12,
        ANNUAL_INCOME * PENSION_RATE / 12,
        ANNUAL_INCOME * UNEMPLOYMENT_INSURANCE_RATE / 12,
        ANNUAL_INCOME * EXTRA_INSURANCE_RATE / 12,
        (ANNUAL_INCOME / 12 - NON_TAXABLE_INCOME / 12) * INCOME_TAX_RATE,
        calculate_net_salary(ANNUAL_INCOME, NON_TAXABLE_INCOME, HEALTH_INSURANCE_RATE, PENSION_RATE, UNEMPLOYMENT_INSURANCE_RATE, EXTRA_INSURANCE_RATE, INCOME_TAX_RATE)
    ]

    df = pandas.DataFrame({'labels': labels, 'parents': parents, 'values': values})

    fig = px.sunburst(df, path=["parents", "labels"], values='values', labels=["labels", "values"])
    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
    st.plotly_chart(fig)




st.title('Income Calculator')
st.caption("""This calculator helps you to calculate how much you can save from your monthly income.""")

col1, col2, col3 = st.columns(3)

with col1:
    COUNTRY = st.selectbox('Country', ['Germany', 'Malaysia'])

with col2:
    NET_MONTHLY_INCOME = st.number_input('Monthly Net Income', value=3000)

with col3:
    savings = st.slider("How much do you want to save?", max_value=100, value=10, step=5, format="%d %%")

#net_salary = calculate_net_salary(ANNUAL_INCOME, NON_TAXABLE_INCOME, HEALTH_INSURANCE_RATE, PENSION_RATE, UNEMPLOYMENT_INSURANCE_RATE, EXTRA_INSURANCE_RATE, INCOME_TAX_RATE)

if COUNTRY == 'Germany':
    net_salary_rm = NET_MONTHLY_INCOME * 4.6

    col1, col2, col3= st.columns(3)

    with col1:
        st.metric(label='Net Salary (RM)', value=f"RM {net_salary_rm:.2f}")
        

    with col2:
        st.metric(label='Savings (€)', value=f"{NET_MONTHLY_INCOME * savings / 100:.2f} €")

    with col3:
        st.metric(label='Savings', value=f"RM {net_salary_rm * savings / 100:.2f}")

if COUNTRY == "Malaysia":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label='Net Salary (RM)', value=f"RM {NET_MONTHLY_INCOME:.2f}")

    with col2:
        st.metric(label='Savings', value=f"RM {NET_MONTHLY_INCOME * savings / 100:.2f}")


#plot_sunburst_charts()

    