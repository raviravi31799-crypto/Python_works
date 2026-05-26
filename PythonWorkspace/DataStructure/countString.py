Str=input("Enter string:")
totaldigits=0
totalLetters=0
special=0
for s in Str:
    if s.isnumeric():
        totaldigits+=1
    if s.isalpha():
        totalLetters+=1
    else:
       special+=1
print("Total letters:",totalLetters)
print("Total digits:",totaldigits)
print("Total special characters:",special)