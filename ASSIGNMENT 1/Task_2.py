'''
Task 2: Create a Personalized Greeting
    Problem Statement: Write a Python program that:
        1.  Takes a user's first name and last name as input.
        2.  Concatenates the first name and last name into a full name.
        3.  Prints a personalized greeting message using the full name.
Expected Output:
    The program should output a greeting like:
    Enter first name : vishnu
    Enter Second name : Anand

    Hello, vishnu anand! Welcome to the python program


'''

first = input("Enter first name:")
second = input("Enter second name:")

print(f"Hello, {first} {second}! Welcome in the python program")