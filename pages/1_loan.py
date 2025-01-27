import streamlit as st
import pandas as pd

st.title('Study Loan Calculator')
st.caption("""This calculator helps you to calculate the monthly payment for study loan.
               Please note that this might not be the exact amount as the actual calculation might be different.""")

def calculate_monthly_payment(loan_amount, years, initial_monthly_payment, discount_rate=0):
    balance = loan_amount - initial_monthly_payment * 120 # remaining balance after 10 years

    # Calculate monthly payment after 10 years
    monthly_payment = balance / (12 * (years - 10)) # monthly payment for the remaining years

    return monthly_payment

def create_monthly_payment_table(loan_amount, years, initial_monthly_payment, discount_rate=0):
    monthly_payment = initial_monthly_payment
    total_payment = 0
    table = []

    for i in range(1, years + 1):
        if i <= 10:
            total_payment += monthly_payment * 12
        else:
            if discount_rate > 0:
                discounted_amount = loan_amount * discount_rate
            else:
                discounted_amount = loan_amount
            monthly_payment = calculate_monthly_payment(discounted_amount, years, initial_monthly_payment, discount_rate)
            
            total_payment += monthly_payment * 12

        table.append([i, monthly_payment, total_payment])

    return table

def calculate_loan_balance(loan_amount, total_payment):
    debt_balance = []
    for values in total_payment:
        amount = values[1] * 12
        loan_amount -= amount
        # If the loan balance is negative, set it to 0
        if loan_amount < 0:
            loan_amount = 0
        debt_balance.append(loan_amount)

    return debt_balance

col1, col2 = st.columns(2)

with col1:
    loan_amount = st.number_input('Loan Amount', value=400000)
    years = st.number_input('Years', value=25)

with col2:
    initial_monthly_payment = st.number_input('Initial Monthly Payment', value=600)
    discount_rate = st.selectbox('Discount Rate', ["No discount", "50%", "75%"], )

    if discount_rate == "No discount":
        discount_rate = 0
    elif discount_rate == "50%":
        discount_rate = 0.5
    elif discount_rate == "75%":
        discount_rate = 0.25

total_payment = create_monthly_payment_table(loan_amount, years, initial_monthly_payment, discount_rate)
debt_balance = calculate_loan_balance(loan_amount, total_payment)

tab1, tab2, tab3 = st.tabs(['Info', 'Loan Table', 'Chart'])
with tab1:
    final_amount = loan_amount * discount_rate if discount_rate > 0 else loan_amount
    diff = (total_payment[-1][1] - initial_monthly_payment) / initial_monthly_payment * 100
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Final amount", value=final_amount)
    with col2:
        st.metric(label="Monthly payment after 10 years", value=f"{total_payment[-1][1]:.2f}", 
                    delta=f"{diff:.2f} %", delta_color="inverse")
            
with tab2:
    df = pd.DataFrame(total_payment, columns=['Years', 'Monthly Payment', 'Total Payment'])
    st.dataframe(df, hide_index=True)

with tab3:
    annual_payments = [item[2] for item in total_payment]

    
    st.line_chart(annual_payments)