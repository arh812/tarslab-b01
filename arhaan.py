x=int(input("enter  first number: "))
y=int(input("enter second number: "))
op =input("enter operator (+, -, *,/): ")
if op == "+":
    result = x + y
    print(f"Result: {x} + {y} = {result}")

elif op == "-":
    result = x - y
    print(f"Result: {x} - {y} = {result}")

elif op == "*":
    result = x * y
    print(f"Result: {x} * {y} = {result}")

elif op == "/":
    if y != 0:
        result = x / y
        print(f"Result: {x} / {y} = {result}")










