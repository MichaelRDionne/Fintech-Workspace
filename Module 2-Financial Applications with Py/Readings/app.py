#import calculator as calc

#print(calc.add(2,2))

#can import the add function on its own (from calculator import add)

from calculator import sub,mul

sub_output = sub(5,3)

mul_output = mul(sub_output, 2)

print(f'The result of 5 minus 3 is {sub_output} and the result of {sub_output} times 2 is {mul_output}.')


