"""list=[]
n=int(input("Enter the number of elements on the list:"))
for i in range(0,n):
    print("Enter element no-{}:".format(i+1))
    element=int(input())
    list.append(element)#adding element
print("The created list:",list)


#using split
n=int(input("Enter the number of elements:"))
list=input("Enter the elements separated by commas:").split(',')
print("The list is:",list)

#using split and map function
t=list(map(int,input("Enter the list elements:").split()))
print("The list created:",t)


#Logical comprehension 
ele=[x**2 for x in range(5)]
ele1=[x for x in range(5)]
print(ele)
print(ele1)


#using eval()


#Passing list as argument to function
def increment(list2):
    for i in range(0,len(list2)):
        list2[i]+=5
    print("Reference of list inside function",id(list2))
list1=[10,20,30,40,50]
print(list1)
print("Reference of list1 before call:",id(list1))
increment(list1)
print("The list after function call:")
print(list1)


#
def increment(list2):
    print("Reference of list inside the function before assignment:",id(list2))
    list2=[1,2,3,4,5]
    for i in range(0,len(list2)):
        list2[i]+=5
    print("Reference of list inside function after assignment:",id(list2))
list1=[10,20,30,40,50]
print(list1)
print("Reference of list1 before call:",id(list1))
increment(list1)
print("Reference if list after function call:",id(list1))
print("The list after function call:")
print(list1)
"""
#Menu driven list operations
list=[10,20,30,40,50]
while True:
    print("List operations")
    print("1.Append an element")
    print("2.Insert an element")
    print("3.Append a list to the given list")
    print("4.Modify an existing element")
    print("5.Delete an existing element from its position")
    print("6.Delete an existing element with a given value")
    print("7.Sort the list in ascending order")
    print("8.Sort the list in descending order")
    print("9.Display the list")
    print("10.Exit")
    choice=int(input("Enter choice:"))
    if choice==1:
       element=int(input("Element:"))
       list.append(element)
       print("Appended an element to the list:",list)
    elif choice==2:
     list.insert(0,5)
     print("Inserted an element to the list:",list)
    elif choice==3:
     list1=input("Enter list:")
     list.extend(list1)
     print("Appended a list to existing list:",list)
    elif choice==4:
      ele=int(input())
      index=int(input())
      list(index)==ele
      print(list)
    elif choice==5:
       index=int(input("Enter index:"))
       list.pop(index)
       print("list after deleting element with position:",list)
    elif choice==6:
       element=int(input("Enter element:"))
       list.remove(element)
       print("List after removing the given element:",list)
    elif choice==7:
       list.sort()
       print("Sorted list in ascending order:",list)
    elif choice==8:
       list.sort(reverse=True)
       print("Sorted list in descending order:",list)
    elif choice==9:
       print("The list is:",list)
    elif choice==10:
       print("Exit")
       break
else:
   print("Invalid choice")