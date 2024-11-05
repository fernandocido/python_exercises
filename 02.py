# Exercise 2 --> Find Pairs with Target Sum: Given an array and a target sum, find all pairs that add up to the target.

target_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 10

def find_pairs(target_array, target_sum):
    seen = set()
    pairs = []

    for num in target_array:
        complement = target_sum - num
        if complement in seen:
            pairs.append((min(num, complement), max(num, complement)))
        seen.add(num)
    return pairs

result = find_pairs(target_array, target_sum)
print(result)
