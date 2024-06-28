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




#---------------------------------------------------------------


#to do list project by #stalk
to_do_list = []


def add(task):
    to_do_list.append(task)


def remove(task):
    to_do_list.remove(task)


def veiw():
    for task in to_do_list:
        print(task)


while True:
    print("\nTo-Do List Options:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add(task)

    elif choice == "2":
        task = input("Enter task to remove: ")
        remove(task)

    elif choice == "3":
        veiw()

    elif choice == "4":
        print("fuck off my friend :)")
        break

    else:
        print("Invalid choice, please choose again.")
