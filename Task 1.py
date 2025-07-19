______________________________________________________________________________
# Task 1: Create a Dictionary of Student Marks
'''
Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''
______________________________________________________________________________

students = {"Alice" : 85, "Nick" : 75 , }

students_name = input("Enter the student's name :")

if students_name in students:
    print("{}'s marks :".format(students_name), students[students_name])
else:
    print("student not found")
