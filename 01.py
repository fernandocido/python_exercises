# Exercise 1 --> Remove Duplicates: Write a function to remove duplicate elements from an array.

def remove_duplicates(array):
    unique_elements = []
    for element in array:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

fruits = ["apple", "banana", "apple", "banana", "grapes", "mango", "grapes", "cherry", "oranges"]
unique_fruits = remove_duplicates(fruits)

print(fruits)
print(unique_fruits)
