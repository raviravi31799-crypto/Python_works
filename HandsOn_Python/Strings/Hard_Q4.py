str=input("Enter string:")
word=str.split()
smallest=word[0]
for i in word:
    if len(i)<len(smallest):
        smallest=i
print("smallest string:",smallest)