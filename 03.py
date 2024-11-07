# Exercise 3 --> Rotate Array: Rotate the elements of an array to the right by a given number of steps.

given_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_the_right = 3

def rotate(array, steps):
    n = len(array)
    steps = steps % n
    rotated_array = array[-steps:] + array[:-steps]
    return rotated_array

result = rotate(given_array, to_the_right)
print("The given array is: ", given_array)
print("The result is: ", result)

# OUTPUT:

'''

The given array is:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
The result is:  [8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7]

'''
