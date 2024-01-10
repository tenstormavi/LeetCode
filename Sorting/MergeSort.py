"""
Merge Sort

Ref:
1. https://www.youtube.com/watch?v=6pV2IF0fgKY
2. https://www.youtube.com/watch?v=mB5HXBb_HY8&t=449s
3. https://www.youtube.com/watch?v=unxAnJBy12Q
"""

import sys

# the setrecursionlimit function is used to modify the default recursion
# limit set by python. Using this, we can increase the recursion limit
# to satisfy our needs

sys.setrecursionlimit(10 ** 6)


def merge(nums, si, mid, ei):
    ans = []
    idx1 = si
    idx2 = mid + 1

    while idx1 <= mid and idx2 <= ei:
        # compare and save in new list
        if nums[idx1] < nums[idx2]:
            ans.append(nums[idx1])
            idx1 += 1
        else:
            ans.append(nums[idx2])
            idx2 += 1

    # Copy the remaining elements if any
    while idx1 <= mid:
        ans.append(nums[idx1])
        idx1 += 1

    # Copy the remaining elements if any
    while idx2 <= ei:
        ans.append(nums[idx2])
        idx2 += 1

    # Put the result in original list
    for i in ans:
        nums[si] = i
        si += 1


def mergeSort(nums, si, ei):
    # Base case
    if si >= ei:
        return

    # Same as mid = (si + ei) / 2 but avoids overflow for large si and ei
    mid = si + (ei - si) // 2

    # Sort first and second halves
    mergeSort(nums, si, mid)
    mergeSort(nums, mid+1, ei)
    merge(nums, si, mid, ei)


nums = [12,45,23,51,19,8]
print("Unsorted array: ", nums)
mergeSort(nums, 0, len(nums)-1)
print("Sorted array: ", nums)
