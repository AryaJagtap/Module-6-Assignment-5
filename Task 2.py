______________________________________________________________________________
# Task 2: Demonstrate List Slicing
'''
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''
______________________________________________________________________________

list1 = list(range(1,11))
print(list1)

extract = list1[:5]
print("Extracted first five elements:",extract)

extract.reverse()
print("Reversed extracted elements:", extract)

