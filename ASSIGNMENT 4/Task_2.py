'''
Task 2: Write and Append Data to a File
 
    Problem Statement: Write a Python program that:
        1.   Takes user input and writes it to a file named output.txt.
        2.   Appends additional data to the same file.
        3.   Reads and displays the final content of the file.
   


'''
with open("output.txt","w") as f:

    name = input("Enter text to write to the file :")
    f.write(name)
    print("Data successfully written to output.file")

    app = input("Enter additional text to append :")
    f.write("\n"+app)
    print("Data succesfully append")

with open("output.txt","r") as f:
    data = f.readlines()

print("final content of output.txt : ")

for i in data:
    print(i)