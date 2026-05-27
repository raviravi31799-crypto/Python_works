try:
    file=open("test.txt",'w')#this will(write mode) create file by its own and write
    try:
        file.write("This is my file")
    finally:#try should either followed by finally or except block
        print("Going to close the file")
        file.close()
except IOError:
    print("Error:can't find the file")
else:
    print("Executed when no exception occurs")
finally:
    print("Always executed")