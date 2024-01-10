"""
Quick Sort

Ref:
1. https://www.youtube.com/watch?v=QXum8HQd_l4
"""


def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    # Swap the pivot element
    i += 1
    array[i], array[high] = array[high], array[i]

    # pivot index
    return i


def quicksort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pidx = partition(array, low, high)

        # Recursive call on the left of pivot
        quicksort(array, low, pidx - 1)

        # Recursive call on the right of pivot
        quicksort(array, pidx + 1, high)


nums = [12, 45, 23, 51, 19, 8]
print("Unsorted array: ", nums)
quicksort(nums, 0, len(nums) - 1)
print("Sorted array: ", nums)
