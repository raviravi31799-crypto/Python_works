def circle(radius):
    print("area of circle:",3.14*radius*radius)
def rectangle(length,breadth):
   print( "area=",length*breadth )
def square(side):
    print("area=",side*side   )

while True:
    print("Menu driven program")
    print("1.Area of circle")
    print("2.Area of rectangle")
    print("3.Area of square")
    print("4.Exit")
    choice= int(input("Enter choice:"))
    if choice==1:
        radius=int(input("Enter radius:"))
        circle(radius)
    elif choice==2:
        length=int(input("Enter length:"))
        breadth=int(input("Enter breadth:"))
        rectangle(length,breadth)
    elif choice==3:
        side=int(input("Enter side:"))
        square(side)
    elif choice==4:
        break
    else:
        print("invalid")