total=int(input("Enter animals count:"))
deer=int(input())
rabbit=int(input())
birds=int(input())
squirrels=int(input())
count=(deer+rabbit+birds+squirrels)
if(total>count):
    print("Baby lion is mischievous")
elif(total==count):
    print("Baby lion is well behaved")
else:
    print("Counted Wrongly")
