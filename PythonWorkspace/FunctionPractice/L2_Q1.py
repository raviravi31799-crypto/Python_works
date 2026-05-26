def Even(a,b):
    sum=0
    for i in range(a,b):
        if(i%2==0):
            sum+=i
    return sum

def Odd(a,b):
    Odd=0
    for i in range(a,b):
        if(i%2!=0):
            Odd+=i
    return Odd
num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
Evensum=Even(num1,num2)
Odd=Odd(num1,num2)
print("The sum of odd numbers from ",num1 ,"to",num2 ,"is:",Odd)
print("The sum of even numbers from ",num1 ,"to",num2 ,"is:",Evensum)
print("The absolute difference between the two sums is:",abs(Evensum-Odd))