def add_mul(num1,num2,num3=4):#Must be followed like this
#def add_mul(num1=4,num2,num3):# parameter without a default follows parameter with a default(Error)
    out=(num1+num2)*num3
    return out
a=int(input("integer1:"))
b=int(input("integer2:"))
result=add_mul(a,b)
print(result)