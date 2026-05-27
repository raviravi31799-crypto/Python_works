str=input("Enter string:")
string=""
char='/*@&!^$%'
for i in range(len(str)):
    if str[i] in char:
        string=string+'#'
    else:
        string=string+str[i]
print(string)