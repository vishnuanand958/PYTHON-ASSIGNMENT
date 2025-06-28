'''
Task 2: Demonstrate List Slicining
    Problem Statement: Write a Python program that:
        1.   Creates a list of numbers from 1 to 10.
        2.   Extracts the first five elements from the list.
        3.   Reverses these extracted elements.
        4.   Prints both the extracted list and the reversed list

    Expected Output:
        Original list :[1,2,3,4,5,6,7,8,9,10]
        Extracted first five elements : [1,2,3,4,5]
        Reversed Extracted elements :[5,4,3,2,1]
'''
 
list_1 =[1,2,3,4,5,6,7,8,9,10]
extract = list_1[0:5]
print("Original lExtracted first five elements : ist : ",list_1)
print(f"Extracted first five elements : {extract}")

rev =[]
# use loop to print in reverse 
for i in range(len(extract),0,-1):
    rev.append(i)
print("Reversed Extracted elements : ",rev)