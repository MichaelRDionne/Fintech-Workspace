'''This script contains a variety of financial calculator 
functions needed to determiine loan qualifications '''

def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income):

    '''calculates user's monthly debt-to-income ratio'''

    monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income)
    return monthly_debt_ratio


def calculate_loan_to_value_ratio(loan_amount, home_value):
    
    """calculates user's loan_to_value_ratio"""

    loan_to_value_ratio = int(loan_amount) / int(home_value)
    return loan_to_value_ratio

    