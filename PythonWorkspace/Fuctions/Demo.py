#Function definition
def add_mul(num1,num2,num3):
    out=(num1+num2)*num3
    return out
a=int(input("Integer1:"))
b=int(input("Integer2:"))
c=int(input("Integer3:"))
result=add_mul(a,b,c)#function call
print(result)