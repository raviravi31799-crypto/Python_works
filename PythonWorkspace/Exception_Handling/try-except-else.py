try:
    a=int(input("Enter num1:"))
    b=int(input("Enter num2:"))
    c=a/b
    print(c)
except(ZeroDivisionError):
    print("Can't divide by zero")
else:
    print("Successfully executed")#execute when no exeption occurs

#multiple except statements can be used

try:
    a=int(input("Enter num1:"))
    b=int(input("Enter num2:"))
    c=a/b
    print("a/b=",c)
except NameError:
    print("This is value Error")
except Exception:
    print("Can't divide by zero")
    print(Exception)#prints the exception message
else:
    print("Successfully executed")#execute when no exeption occurs



