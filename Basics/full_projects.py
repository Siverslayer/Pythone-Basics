# this project is going to be  in Calculator
num1 = int(input("please enter your first number: "))
num2 = int(input("please enter your second number: "))
oper = input("enter you operator: ")

if oper == "+":
    print("= ",num1+num2)
elif oper == "-":
    print("= ",num1-num2)
elif oper == "*":
    print("= ",num1*num2)
elif oper == "/":
    print("= ",num1/num2)
elif oper == "%":
    print("= ",num1%num2)
else: print("you didn't select the right operator!!!!")
