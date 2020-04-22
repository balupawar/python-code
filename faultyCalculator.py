# create faulty calculator
# balu pawar
# 25/6 = 44
# 88+44 = 0
#10-10 =12
print("Enter first number:")
number1= int(input())
print("choose operation on number , + ,- / , *")
operator = input()
print("Enter Second Number")
number2 = int(input())

if number1 == 26 and operator == '/' and number2== 6:
    print("44")
elif number1 == 88 and operator == '+' and number2 == 44:
    print("0")
elif number1 == 10 and operator == '-' and number2 == 12:
    print("12")
elif operator == '+':
    addition = number1 + number2
    print(addition)
elif operator == '-':
    substraction = number1 - number2
    print(substraction)
elif operator == '*':
    multiplication = number1/number2
    print(multiplication)
elif operator == '/':
     division = number1 / number2
     print(division)
elif operator == '%':
    modulus = number1 % number2
    print(modulus)
else:
    print("please insert correct input")
