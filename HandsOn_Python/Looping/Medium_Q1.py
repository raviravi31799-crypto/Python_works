num=int(input("Enter the num:"))
even=0
odd=0
for i in range(0,num+1):
    if(i%2==0):
        even+=i
    else:
        odd+=i
print(odd,even)
    

