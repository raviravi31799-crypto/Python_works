num=2
def demo():
    global num #Resolved unbound local error with global keyword
    num=num*2
    print("Num:",num)
demo()
print("num:",num)