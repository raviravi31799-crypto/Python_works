"""file=open("myfile.txt",'r')
#var=file.read(20)
var=file.read(-20) # file.read()# both prints pr reads the whole content of file
print(var)
file.close()

#readline(n)
file=open("myfile.txt",'r')
var=file.readline(20)
print(var)
file.close()

#readlines
file=open("myfile.txt",'r')
var=file.readlines()
print(var)
file.close()

#split function in readlines

file=open("myfile.txt",'r')
var=file.readlines()
for line in var:
    word=line.split()
    print(word)


file=open("myfile.txt",'r')
var=file.readline()
for line in var:
    word=line.split()
    print(word)#need to use iteration to print the whole content"""

#splitlines function in readlines

file=open("myfile.txt",'r')
var=file.readlines()
for line in var:
    word=line.splitlines()
    print(word)