"""tuple=10,
print(type(tuple))

tuple1=(10,3.14,'ram',[1,2,3])
print(type(tuple1[3]))


#edit/modify
tuple=(10,20,30,40,50)
print("Reference of tuple:",id(tuple))
tuple=(100,)+tuple[1:]
print(tuple)
print("Reference of modified tuple:",id(tuple))

addr='monty@python.org'
print(type(addr))
uname,domain=addr.split('@')
print(uname,domain)

quot,rem=divmod(7,3)
print(quot)
print(rem)


#Dictinary creation
dict={}
print(type(dict))
dict1={1:'apple',2:'ball'}
dict={1:"CSE",'name':'Ram',"list":[1,2,3],"tuple":(1,2,3)}
print(type)


print(dict())
numbers=dict(x=5,y=0)#using keyword arguments
print(numbers)
num1=dict({'x':5,'y':0})#using mapping
print(num1)
num2=dict([('x',5),('y',0)])#using iterable
print(num2)       
       
       
#nested dictionaries
Family={"child1":{'name':'Ram','year':2004},'child2':{'name':'Renu','year':2006}}
print(type(Family))
print(Family['child1']['name'])

#modify/change
dict={"brand":"Ford","year":1990}
dict["year"]=2002
print(dict)


#Adding element
dict={"brand":"Ford","year":1990}
#print(dict)
#dict['color']='Red'
for x in dict:   #traversal
    print(x,dict[x])

"""
#Keys() and values
dict={"brand":"Ford","year":1990}
"""print(dict.keys())
print(dict.values())
print(dict.pop(1))
print(dict.popitem())
print(dict.get('brand'))
print(copy())"""
d2={"year":2000}
print(dict.update(d2))
d1={'model':2002}
dict.update(d1)
print(dict)


#Dictionary comprehension
squares={x:x*x for x in range(5)}
print(squares)