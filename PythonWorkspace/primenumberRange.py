low=int(input("Enter the lower limit:"))
high=int(input("Enter the upper limit:"))
print("Prime numbers between low and high:")
for num in range(low,high+1):
    if(num>1):
        for i in range(2,i):
            if(num%i)==0:
                break
            else: #for-else
                print(num)
      
