# make calculator

a = float(input("Enter first number: "))
b = float(input("enter seconf number: "))
op = input("Enter operator (+, -, *, /,  %, **):")

if op == '+':
    print(a + b)
elif op =='-':
    print(a - b)
elif op == '*' :
    print(a * b)
elif op == '/':
    print(a / b)
elif op == '**':
    print(a ** b)
else:
    print("invalid operator")


