def OddEven(num):
    Esum==0,Osum==0
    for i in range(0,num):
        if(i%2==0):
            Esum+=i
        else:
            Osum+=i   
    return Esum ,Osum

n=int(input("Enter number:"))
result=OddEven(n)
print("Even sum:"result"Odd sum:",result)