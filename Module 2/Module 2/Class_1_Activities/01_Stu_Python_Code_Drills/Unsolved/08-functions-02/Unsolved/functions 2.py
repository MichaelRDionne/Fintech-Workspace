# Define a function "warble" that takes in a string as an argument, adds " arglebargle" to the end of it, and returns the result.
def warble(input_string):
    return input_string+' arglebargle'
    

# Print the result of calling your "warble" function with the argument "hello".
print (warble('hello'))

# Define a function "wibble" that takes a string as an argument, prints the argument, prepends "wibbly " to the argument, and returns the result
def wibble(input_string):
    print(input_string)
    return'wibbly '+input_string

# Print the result of calling your "wibble" function with the argument "bibbly"
some_text=wibble('bibbly')
print(some_text)

# Define a function "print_sum" that takes in two numbers as arguments and prints the sum of those two numbers.
def print_sum(a, b):
    print(a+b)

some_number=print_sum(5,10)
print(some_number)


# Define a function "return_sum" that takes in two numbers as arguments and returns the sum of those two numbers
def return_sum(a, b):
    return a+b


# Define a function "triple_sum" that takes in 3 arguments and returns the sum of those 3 numbers.
def triple_sum(a,b,c):
    return a+b+c
    

"""
Define a function "dance_party" that takes in a string as an argument,
then prints "dance!", then updates the string by calling "wibble" function
with that argument, followed by "warble" function with that argument,
then returns the updated stringdef dance_party(string_param):

"""

# Print the result of calling your "dance_party" function with your name as the argument
