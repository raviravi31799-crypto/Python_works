Weight=float(input("Weight in Kilograms:"))
Height=float(input("Height in metres:"))
if((Weight<=0) & (Height<=0)):
    print("Enter valid weight and height")

else:
    BMI=Weight/(Height*Height)
    print("BMI:",BMI)