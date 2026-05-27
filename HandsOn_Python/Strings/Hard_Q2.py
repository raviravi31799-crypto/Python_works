str1=input("Enter string:")
str2=input("Enter string2:")
str3="" 
for i in range(len(str1)):
    str3 += str1[i] + str2[-(i+1)]
print(str3)