'''
Task 1: Create a Dictionary of Student Marks

    Problem Statement: Write a Python program that:
        1.   Creates a dictionary where student names are keys and their marks are values.
        2.   Asks the user to input a student's name.
        3.   Retrieves and displays the corresponding marks.
        4.   If the student’s name is not found, display an appropriate message.

    Expected Output:
  
    Enter the student name : vishnu 
    vishnu marks : 80

    If the student does not exist in the dictionary:

    Enter the student name : vishnu
    student not found

'''

student ={
    "vishnu" : 80,
    "anand" : 70,
    "karan" : 80
}


name = input("Enter the student name :")

if name in student:
    print(f"{name} marks :{student[name]}")
else:
    print("Student not found")