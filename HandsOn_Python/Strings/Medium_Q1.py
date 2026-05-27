tuple1=input("The original tuple1:")
tuple2=input("The original tuple2:")
concatenate=""
for i in range(len(tuple1)):
    concatenate+=(tuple1[0]+tuple2[0])
print("The concatenated tuple:",concatenate)