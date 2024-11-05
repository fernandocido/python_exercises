# Exercise 4 --> Merge Sorted Arrays: Merge two sorted arrays into one sorted array without using the sorted() function.

array1 = [1, 3, 5]
array2 = [2, 4, 6]

def merge(array1, array2):
    i, j = 0, 0
    merged = [] 

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged.append(array1[i])
            i += 1
        else:
            merged.append(array2[j])
            j += 1

    while i < len(array1):
        merged.append(array1[i])
        i += 1
    
    while j < len(array2):
        merged.append(array2[j])
        j += 1

    return merged

result = merge(array1, array2)
print("array1 is: ", array1)
print("array2 is: ", array2)
print("The merged array is: ", result)
