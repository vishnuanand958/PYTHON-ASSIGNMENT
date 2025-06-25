'''
    Task 2: Using the Math Module for Calculations
    
        Problem Statement: Write a Python program that:
            1.   Asks the user for a number as input.
            2.   Uses the math module to calculate the:
            o   Square root of the number
            o   Natural logarithm (log base e) of the number
            o   Sine of the number (in radians)
            3.   Displays the calculated results.
        Expected Output:
            For example, if the user enters 25, the output should be:
            
            Enter a number : 25
            squre root : 5.0
            logarithm : 3.2188758248682006
            sine : -0.13235175009777303

'''

from math import *

n = int(input("Enter a number :"))
squre = sqrt(n)
loga =log(n)
sine = sin(n)

print("Squre root : ",squre)
print("logarithmo :",loga)
print("sine :",sine)