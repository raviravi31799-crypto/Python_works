"""t=list()#constructor returns a list
print(type(t))
str='aeiou'
t=list(str)
print(t)


#list deletion
list=[10,20,30,40,50]
del list[2]
print(list)
del list
print(list)

list=["Apple","Banana","Orange","Mango"]#Traversal in for loop using range and len function
for i in range(len(list)):
    print(list[i])

"""
#List sorting
list=["Apple","Orange","Banana","Mango","Grapes"]
list.sort()#sort in ascending order
list.sort(reverse=True)#sort in descending order
print(list)

list=[10,35,80,97,43]
list.sort()#sort in ascending order
list.sort(reverse=True)#sort in descending order
print(list)

list=[10,20,40.32,31]
list1=sorted(list)
print(list1)

#copy()
list=[10,34,89,70]
list1=list.copy()#object is different
print(list)
print(list1)