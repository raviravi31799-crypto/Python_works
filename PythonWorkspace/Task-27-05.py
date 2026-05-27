def dictionary(dic1,dic2,dic3):
       a= dic1.values()
       b=dic2.values()
       c=dic3.values()
       return a,b,c
   

dict1=input("Enter the input1:")
dict2=input("Enter the input2:")
dict3=input("Enter the input3:")
result=dictionary(dict1,dict2,dict3)
print(result)

