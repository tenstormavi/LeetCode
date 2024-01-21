"""
You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

Return an array of right interval indices for each interval i. If no right interval exists for
interval i, then put -1 at index i.

Example 1:
Input: intervals = [[1,2]]
Output: [-1]
Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:
Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.

Example 3:
Input: intervals = [[1,4],[2,3],[3,4]]
Output: [-1,2,-1]
Explanation: There is no right interval for [1,4] and [3,4].
The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.

Constraints:
    1 <= intervals.length <= 2 * 10^4
    intervals[i].length == 2
    -10^6 <= starti <= endi <= 10^6
    The start point of each interval is unique.
"""


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        result = [-1] * n

        def binary_search(val):
            if sorted_intervals[n - 1][0][0] < val:
                return -1

            low, high = 0, len(intervals)
            while low < high:
                mid = low + (high - low) // 2
                if sorted_intervals[mid][0][0] >= val:
                    high = mid
                else:
                    low = mid + 1
            return sorted_intervals[low][1]

        # Save the indices first
        sorted_intervals = []
        for idx, interval in enumerate(intervals):
            sorted_intervals.append([interval, idx])
        sorted_intervals.sort()

        print(sorted_intervals)

        for i in range(n):
            result[i] = binary_search(intervals[i][1])
        return result
