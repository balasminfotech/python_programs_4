print("Welcome to calculator App !!!!")

# while 1:
print("Please select below option to perform calculation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
while 1:
    choice=int(input("Enter your chice :  "))
    print(choice)
    if choice ==1:
        value_1=int(input("Enter first number : "))
        value_2=int(input("Enter second number : "))
        print("Output is ", value_1+value_2)
    elif choice ==2:
        value_1=int(input("Enter first number : "))
        value_2=int(input("Enter second number : "))
        print("Output is ", value_1-value_2)
    elif choice ==3:
        value_1=int(input("Enter first number : "))
        value_2=int(input("Enter second number : "))
        print("Output is ", value_1*value_2)
    elif choice ==4:
        value_1=int(input("Enter first number : "))
        value_2=int(input("Enter second number : "))
        print("Output is ", value_1/value_2)
    elif choice ==5:
        print("Exiting")
        break

