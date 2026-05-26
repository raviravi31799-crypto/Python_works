a=int(input("Classes held:"))
b=int(input("Classes attended:"))

percentage=b/a
if(percentage>=75):
    print(percentage+"%","Allowed")
elif(percentage<75 ):
    c=str(input("medical cause:"))
    print(percentage+"%", "Not Allowed")
elif(percentage<75 and c=="Y"):
    print(percentage+"%","Allowed")
