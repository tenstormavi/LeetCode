"""
You are given an array/list of ‘N’ integers. You are supposed to return the maximum sum of the subsequence
with the constraint that no two elements are adjacent in the given array/list.

Note:
A subsequence of an array/list is obtained by deleting some number of elements (can be zero) from the
array/list, leaving the remaining elements in their original order.

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 500
1 <= N <= 1000
0 <= ARR[i] <= 10^5
Where 'ARR[i]' denotes the 'i-th' element in the array/list.
Time Limit: 1 sec.

Sample Input 1:
2
3
1 2 4
4
2 1 4 9

Sample Output 1:
5
11

Explanation to Sample Output 1:
In test case 1, the sum of 'ARR[0]' & 'ARR[2]' is 5 which is greater than 'ARR[1]' which is 2 so the answer is 5.

In test case 2, the sum of 'ARR[0]' and 'ARR[2]' is 6, the sum of 'ARR[1]' and 'ARR[3]' is 10, and the sum of
'ARR[0]' and 'ARR[3]' is 11. So if we take the sum of 'ARR[0]' and 'ARR[3]', it will give the maximum sum of
sequence in which no elements are adjacent in the given array/list.

Sample Input 2:
2
5
1 2 3 5 4
9
1 2 3 1 3 5 8 1 9

Sample Output 2:
8
24

Explanation to Sample Output 2:
In test case 1, out of all the possibilities, if we take the sum of 'ARR[0]', 'ARR[2]' and 'ARR[4]', i.e. 8,
it will give the maximum sum of sequence in which no elements are adjacent in the given array/list.

In test case 2, out of all the possibilities, if we take the sum of 'ARR[0]', 'ARR[2]', 'ARR[4]', 'ARR[6]'
and 'ARR[8]', i.e. 24 so, it will give the maximum sum of sequence in which no elements are adjacent in the
given array/list.
"""


# Recursion - TLE
def maximumNonAdjacentSum(nums):
    # Write your code here.
    def solve(nums, idx):
        if idx < 0:
            return 0

        # If the array has only one element, max sum can be
        # the number only which is at 0 index
        if idx == 0:
            nums[0]

        # Approach: There are two choices at every index either include the
        # current index or exclude the current index. If current index is included
        # its value will get added and index will jump 2 (i+2 or n-2) times as adjacent value is
        # not allowed to take. if Current index is not included its sum will not get added and
        # index will jump only 1 (i+1 or n-1) as taking adjacent value is possible now.
        incl = solve(nums, idx - 2) + nums[idx]
        excl = solve(nums, idx - 1) + 0

        # we want to return maximum possible among both path
        return max(incl, excl)

    res = solve(nums, idx=len(nums) - 1)
    return res


# Recursion + Memoization
def maximumNonAdjacentSum(nums):
    # Write your code here.
    def solve(nums, idx, dp):
        if idx < 0:
            return 0

        # If the array has only one element, max sum can be
        # the number only which is at 0 index
        if idx == 0:
            nums[0]

        if dp[idx] != -1:
            return dp[idx]

        # Approach: There are two choices at every index either include the
        # current index or exclude the current index. If current index is included
        # its value will get added and index will jump 2 (i+2 or n-2) times as adjacent value is
        # not allowed to take. if Current index is not included its sum will not get added and
        # index will jump only 1 (i+1 or n-1) as taking adjacent value is possible now.
        incl = solve(nums, idx - 2, dp) + nums[idx]
        excl = solve(nums, idx - 1, dp) + 0

        # we want to return maximum possible among both path
        dp[idx] = max(incl, excl)
        return dp[idx]

    dp = [-1] * len(nums)
    res = solve(nums, len(nums) - 1, dp)
    return res
