class Error(Exception):
    "Base class for other exceptions"
    pass
class ValueTooSmallError(Error):
    "Raised when the input value is too small"
    pass
class ValueTooLargeError(Error):
    "Raised when the input value is too large"
    pass


number=10
while True:
    try:
        num=int(input("Enter number:"))
        if num<number:
            raise ValueTooSmallError
        elif num>number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("The value is too small,try again!!")
    except ValueTooLargeError:
        print("The value is too large,try again!!")
print("Congratulations!You guessed it correctly.")
    

