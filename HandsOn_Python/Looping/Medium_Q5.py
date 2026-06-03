num=int(input("Enter num:"))
even=0
odd=0


while num>0:
    rem=num%10
    if(rem%2==0):
        even+=rem
    else:
        odd+=rem
    num=num//10
print(even,odd)
