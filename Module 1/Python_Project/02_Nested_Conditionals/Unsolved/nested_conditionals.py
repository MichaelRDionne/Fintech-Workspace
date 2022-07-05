"""Nested Conditionals."""

# @TODO: Create variables with the initial ad price and company type
company_type = "startup"
ad_price = 10

# @TODO: Convert the following decision logic into valid Python code.
# if the ad price is affordable (less than 20):
if ad_price < 20:
    if company_type == "startup":
#     if the company is a startup:
        print(f"The expected profit is {500}")
#         print that the expected profit is 500
    elif company_type == "existing":
        print(f"The expected profit is {100}.")
#     elif the company is existing:
#         print that the expected profit is 100
#     else:
#         print that the company type is not specified
    else:
        print("The company type is not specified")
# else:
#     print that the ad price is too expensive
else:
    print("The price is too expensive")


