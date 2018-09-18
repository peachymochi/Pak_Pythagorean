"""
Write a program that will ask the user to enter their name and respond with a greeting using this name.
Then ask make the program ask the user to enter values for a and b in order to calculate c.
"""

#Name and Greeting
name = input("Please enter your name: ")
print ("Hello, " + name + "!")

#Length of Legs
print ("Please enter the lengths of the legs 'a' and 'b' of the right triangle in order to calculate the value of 'c': ")

a = float(input("a: "))
b = float(input("b: "))


#calculating the lenght of the hypotenuse "c"
c = (a**2 + b**2)**(1/2)
print ("The value of 'c' is " +str(c) + " which is also called the hypotenuse.")