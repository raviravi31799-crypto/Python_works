#21/05/2026

""" #Example:Number datatype
num1=10
print(type(num1))
num=-2.0
print(type(num))
a=True
print(type(a))
b=2+5j
print(type(b))

#Sequence datatype
name='Jo'#String
print(type(name))
#List
list=[12,"Jo",22.8]
print(list)
print(type(list[1]))
a=(10,2.0,"Apple")#tuple
print(a)

#Set
set1={10,12.0,"Delhi"}
print(set1)
print(type(set1))

#None
var=None
print(type(var))
print(var)

#Dictionary--Mapping
Student={"Name":'Jo','Age':21,'Dept':'ECE'}
print(type(Student))
print(Student)
print(Student['Name']) #Accessed through keys



#Tokens--Literals(Boolean)
x=True+4
print("x is :",x)

y=False+10
print(y)

#Operators(Identity)
num=5
#print(type(num) is int) 
print(type(num) is str) 
num2=num
print(num is not num2)


#Membership
a=[1,2,3]
print('2' in a) #2 represented as string so it will return false 
print(4 not in a)

""" #multiline comment

#Typeconversion(Explicit)
num=10
num1=20
num2=(num+num1)
print(num2)
print(type(num2))
num3=float(num1+num)
print(num3)
print(type(num3))

#input()
name=input("Enter name:")
#age=input("Enter age:")
#print(type(age))   #takes as string , do type cast
age=int(input("Enter age:"))
print(type(age))



#print() function
#printing multiple values
x=5
y=10
print("The value of x is",x, "and y is ",y)

#f strings 
name="Alice"
age=30
print(f"My name is {name} and I am {age} years old.")

#Using the separator and end parameters
print("Apple","Orange","Mango","Banana",sep=",",end=".\n")
