# Initial imports

from pathlib import Path
import csv
from qualifier.utils.fileio import load_csv
from qualifier.utils.calculators import (calculate_monthly_debt_ratio, calculate_loan_to_value_ratio)



# This function loads a CSV file with the list of banks and available loans information
# from the file defined in `file_path`
def load_bank_data(file_path):
    csvpath = Path(file_path)
    return load_csv(csvpath)


# This function is the main execution point of the application. It triggers all the business logic.
def run():
    # Set the file path of the CSV file with the banks and loans information
    file_path = Path("./data/daily_rate_sheet.csv")
    # Load the latest Bank data
    bank_data = load_bank_data(file_path)

    # This print statement will display all of the bank data that is provided.
    print(f"bank_data: {bank_data}")

    # The following lines, set the applicant's information and implements the following user story:
    # As a customer,
    # I want to provide my financial information
    # so that I can apply for a loan
    credit_score = 750
    debt = 5000
    income = 20000
    loan_amount = 100000
    home_value = 210000

    # Calculate the Monthly Debt Ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)

    print(f"The monthly deb to income ratio is {monthly_debt_ratio:.02f}.")

    # Calculate the Loan to Value
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan_amount, home_value)

    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")



run()
