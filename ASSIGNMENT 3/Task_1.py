'''
    Task 1: Calculate Factorial Using a Function 


        Problem Statement: Write a Python program that:
            1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
            2.   Returns the calculated factorial.
            3.   Calls the function with a sample number and prints the output.
        
        Expected Output:
        For example, if the function is called with 5, it should return:

        Enter a number : 5
        factorial of 5 is : 120

'''

# using factorial 

n = int(input("Enter a number :"))
def fact(n):
    if n<2:
        return 1
    else:
        return n*(fact(n-1))
    
result = fact(n)

print(f"Factorial of {n} is : {result}")


# using loop
n = int(input("Enter a number :"))
fac = 1
for i in range(n,1,-1):
    if i < 2:
       fac = 1
    else:
        fac *=i
print(f"Factorial of {n} is : {fac}")