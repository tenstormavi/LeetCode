"""
Insertion Sort

Ref:
1. https://www.youtube.com/watch?v=OGzPmgsI-pQ&ab_channel=GeeksforGeeks
2. https://www.youtube.com/watch?v=3GC83dh4cf0&ab_channel=ApnaCollege
"""

# Approach:
# Insert an element from an unsorted array into its correct position in a sorted array.

nums = [12,45, 23, 51, 19, 8]

print("Unsorted array: ", nums)
for i in range(1, len(nums)):
    current = nums[i]
    j = i-1
    while nums[j] > current and j >= 0:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = current
print("Sorted array: ", nums)
