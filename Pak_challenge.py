"""
Write a program that will ask the user to enter in three legs of a triangle and then test to see if the triangle is
"""
a = int(input("Please enter side a: "))
b = int(input("Please enter side b: "))
c = int(input("Please enter side c: "))
    
if (a**2 + b**2 == c**2):
    print ("This is a RIGHT triangle.")
    
elif (a**2 + b**2 < c**2):
    print ("This is an OBTUSE triangle.")
    
elif (a**2 + b**2 > c**2):
    print ("This is an ACUTE triangle.")
    
else:
    print ("This is NOT a right triangle.")