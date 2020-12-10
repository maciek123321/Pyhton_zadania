from zad5_1 import Complexx
import re

def parsing(equation):
    equation_numbers = re.findall(r'-?\d+', equation)
    equation_operator = re.findall(r'-?\D+', equation)[2][3]
    return Complexx(int(equation_numbers[0]), int(equation_numbers[1])), \
           Complexx(int(equation_numbers[2]), int(equation_numbers[3])), \
           equation_operator

equation = "(2+3i) + (1+5i)" # equation example, space on the both sides of the operator is neccessary, complex numers have to be in brackets

x, y, operator = parsing(equation)
if operator == '+':
    print(f"({x})+({y})={x + y}")
elif operator == '*':
    print(f"({x})*({y})={x * y}")
elif operator == '-':
    print(f"({x})-({y})={x - y}")



