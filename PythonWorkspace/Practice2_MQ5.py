name=str(input("Enter name:"))
item=int(input("Enter items:"))
if(item<10):
    print(name,(item*12))
elif(item>=10 and item<=99):
    print(name,item*10)
else:
    print(name,item*7)
    
