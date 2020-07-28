"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
counter = 1
finalNum = 0
total = 0
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def twentyNums(nums, counter):
    total = 0
    for i in nums:
        if counter % i == 0:
            total += 1
    return total

while total != 20:
    total = twentyNums(nums, counter)
    if total == 20:
        finalNum = counter
    else:
        counter += 1
    #print("counter = " + str(counter) + ", total = " + str(total))

print(finalNum)

