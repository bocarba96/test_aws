"""
Your module description
Autor: Bocar BA
Email: babocarba96@gmail.com
"""

myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

firstString = "Bocar"
secondString = "BA"
thirdString = firstString +" "+ secondString
print(thirdString)

name = input("What is your name? ")
print(name)

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("L'animal : {}\nColor: {}".format(animal,color))
