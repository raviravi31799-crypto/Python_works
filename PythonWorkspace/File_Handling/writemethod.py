file=open("myfile.txt",'w')

line=file.write("Hey,Good afternoon!! This is Jothika Ravi\n")
print(line)
file.write(str(58))#cannot write a integer only str can be written 
file.close()


#writelines()method
file=open("myfile.txt",'w')
lines=["Hello everyone\n","How are you?\n","I am good here\n"]
file.writelines(lines)
file.close()
