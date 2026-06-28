#Python Project-Simple Calculator

def addition(a,b): #Function 1 for addition.
    print("Result:",a+b)
def subtraction(a,b): #Function 2 for subtraction.
    print("Result:",a-b)
def multiplication(a,b): #Function 3 for multiplication.
    print("Result:",a*b)
def division(a,b): #Function 4 for division.
    print("Result:",a/b)

print('''-----Python Calculator-----

Welcome to the Python Calculator!!! Here is your list of options-


Menu
-----------------
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exit
-----------------''') #Displaying the menu to the user.

while True:
    try: #Try and except blocks to handle value and zero divsion errors.
        choice=int(input("Enter your choice:"))
        if choice==1:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))
            addition(num1,num2)
        elif choice==2:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))
            subtraction(num1,num2)
        elif choice==3:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))
            multiplication(num1,num2)
        elif choice==4:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))
            division(num1,num2)
        elif choice==5:
            print("Exited successfully! Thank you for using the Python Calculator.")
            break
        else:
            print("Invalid choice. Please enter one of the options from the menu provided.")
    except ValueError:
        print("Please enter an integer or a decimal number.")
    except ZeroDivisionError:
        print("Division by zero is not possible. Please enter a valid second number for division.")
    
            
            
        
                






    
