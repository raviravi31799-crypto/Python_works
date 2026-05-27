try:
    a=int(input("Enter num1:"))
    b=int(input("Enter num2:"))
    c=a/b
    print(c)
except(ZeroDivisionError):
    print("Can't divide by zero")
else:
    print("Successfully executed")#execute when no exeption occurs
finally:
    print("Always executed")#Executed everytime irrespective of exception
