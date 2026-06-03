num=int(input("Enter the num:"))
sum=0
for i in range(num,0,-1):
    print(i,end=" ")
    sum+=i
print(sum)