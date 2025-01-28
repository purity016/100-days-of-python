# building a calculator to get a grips with python.
# the program does the following:

print("1. add")
print("2.division")
print("3.subtraction")
print("4.multiplication")

operation = input()

# this is my addition logic
if operation == "1":
    num_1 = input("enter first number;")
    num_2 = input("enter second number;")
    print("The sum is "+ str(int(num_1) + int(num_2)))
elif operation == "2":
    num_1 = input("enter first number")
    num_2 = input("enter second number")
    print("The division is "+ str(int(num_1) / int(num_2)))
elif operation == "3":
    num_1 = input("enter first number")
    num_2 = input("enter second number")
    print("The subtraction is" + str(int(num_1) - int(num_2)))
elif operation == "4":
    num_1 = input("enter first number") 
    num_2 = input("enter second number")
    print("The multiplication is"+ str(int(num_1) * int(num_12)))
elif operation == "5" 
    num_1 = input ("enter first number")
    num_2 = input ("enter second number")
    print("The module is") + str(int(num_1) mod int(num_2)
else:       
    print("calculator shutting down")
