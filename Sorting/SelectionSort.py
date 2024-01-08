"""
Selection Sort

Ref:
1. https://www.youtube.com/watch?v=xWBP4lzkoyM&ab_channel=GeeksforGeeks
2. https://www.youtube.com/watch?v=dQa4A2Z0_Ro&ab_channel=ApnaCollege
"""

# Approach:
# Find the minimum element in an unsorted array and swap it with the element at the beginning.

nums = [12,45,23,51,19,8]

print("Unsorted array: ", nums)
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[j] < nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
print("Sorted array: ", nums)
