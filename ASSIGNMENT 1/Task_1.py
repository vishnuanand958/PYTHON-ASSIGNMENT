'''
Task 1: Perform Basic Mathematical Operations -

Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.

 Expected Output:
 The output should include the result of each operation performed, for example:
    Enter first number - 5
    Enter second number -10
    
    Addition - 15
	Subtraction - -5
	Multiplication - 50
	Division - 0.5
'''

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number:"))

print("Addition: ",num1+num2)
print("Subtraction: ",num1-num2)
print("Multiplication: ",num1*num2)
print("Division: ",float(num1/num2))