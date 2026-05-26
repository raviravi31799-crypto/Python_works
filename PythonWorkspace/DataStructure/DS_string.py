"""Greet="Welcome"
length=len(Greet)
print(length)
del(Greet)

#Traversal
Greet="Welcome"
for i in Greet:
    print(i)

#While
Greet="Welcome"
index=0
while index<len(Greet):
    letter=Greet[index]
    print(letter)
    index=index+1


#Slicing
str="Good Day"
print(str[-3:-1])#first index is greater return empty string


#Step in slicing
str="Hello" 
print(str[4:0:-2])

str="Good Day"
print(str[::-2])

#String operators
str="Hello"
str1="World"
print(str+str1)
print(str*3)
txt="Hard work never fails"
if"work" in txt:
    print("Yes,present")
else:
    print("No,not present")

#Edit/modify
str="Hello World"
str[0]='J'
print(str)



# As they are (strings) immutable thus raises type error
#can be modifies as the following
str="Hello World!"
#str1='J'+str[1:]
#str1='J'+str[6:]
str1='J' +str[-6:-1]
print(str1)
"""
#Built-in methods
#find
word="Good Day"
index=word.find('a')
print(index)
index1=word.find('Da')
print(index1)
word="Banana"
print(word.find('na',3))
#upper
word="Good Day"
print(word.upper())
#Lowercase conversion
print(word.lower())

#replace
word="Good Day"
print(word.replace('Good','Happy'))

#count(occurrence of character)
word="Python Programming"
print("count:",word.count('o'))
print("Capitalized:",word.capitalize())

#isalnum(checks alphanumeric characters)
str="Jo123"
print("contains alphanumeric:",str.isalnum())
str1="Joravi"
print("contains only alphabets:",str1.isalpha())#isalpha

#endswith and startswith
word="Python programming"
print(word.startswith('Python'))
print(word.endswith('ing'))