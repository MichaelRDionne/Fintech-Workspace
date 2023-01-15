# Loan Qualifier Application

This is a Python command-line interface application that allows users to see qualifying loans from lenders quickly and easily. The application works by taking in a `daily_rate_sheet` of loan criteria from various loan providers, asking the user a number of questions to evaluate their loan eligibility, and then returning a list of qualifying loans.

---

## Technologies

This project leverages Python 3.7 with the following packages:

* [Fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [Questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

* [PyTest](https://docs.pytest.org/en/stable/) - For basic assertion testing of financial calculators and filters, and filio.


---

## Installation Guide

Before running the application, first install the following dependencies.

```python
  pip install fire
  pip install questionary
  pip install pytest
```

---

## Examples

Upon launching the loan qualifier application, you will be greeted with the following prompts.

![Loan Qualifier Prompts](../Images/loan_qualifier.png)



---

## Usage

To use the loan qualifier application, clone the repository and run the **app.py** with the following:

```python
python app.py
```

---

## Contributors

Brought to you by ET Home Loans.

---

## License

MIT
