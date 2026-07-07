print("CALCULATOR")
x=int(input("Enter first number: "))
y=int(input("Enter Second number: "))
op=input("choose an operation(+,-,*,/):")
result=None
match op:
    case "+":
        result=x+y
    case "-":
        result=x-y
    case "*":
        result=x*y
    case "/":
        if y==0 :
           print("Error. cant divide by zero")
        else:
            result=x/y
    case _:
        print("enter a valid operation")
if result is not None:
    print(f"The answer is: {result}")