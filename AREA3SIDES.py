#FIND THE AREA OF TRIANGLE WHOSE 3 SIDES ARE GIVEN#
import math
a= int (input("Enter the Base ="))
b= int (input("Enter the Height="))
c= int (input("Enter the Altitude = "))
s=a+b+c/2
m=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("AREA =",m)