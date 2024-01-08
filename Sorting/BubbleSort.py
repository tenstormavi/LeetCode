"""
Bubble Sort

Ref:
1. https://www.youtube.com/watch?v=nmhjrI-aW5o&ab_channel=GeeksforGeeks
2. https://www.youtube.com/watch?v=xcPFUCh0jT0&ab_channel=ApnaCollege
3. https://www.youtube.com/watch?v=p6I7LIUqQnU&ab_channel=Log2Base2%C2%AE
"""

# Approach:
# Repeatedly swap two adjacent elements if they are in the wrong order.

nums = [5,1,4,2,8,9]

print("Unsorted array: ", nums)
for i in range(len(nums)):
    for j in range(0, len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print("Sorted array: ", nums)
