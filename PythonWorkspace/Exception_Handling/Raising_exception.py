try:
    num=int(input("Enter the integer:"))
   # if(num<=0): 
      #  raise ValueError("Negative number!")
except ValueError as e:
    print(e)#prints error message
print("Handled successfully")