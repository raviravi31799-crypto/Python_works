num=int(input("Enter num:"))
c=0
if(num<=1):
    print("Not a prime")
for i in range(2,num):
    if(num%i)==0:
        c+=1
if c==0:
    print("Yes")
else:
    print("No")