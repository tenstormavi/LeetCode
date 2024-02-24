"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an
array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
    1 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti <= endi <= 10^4
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # TC - O(nlog(n))

        # Sort the intervals based on the start to figure out the overlapping
        intervals.sort(key=lambda x: x[0])

        output = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = output[-1][1]

            if start <= last_end:
                # Overlapping is there, need to merge
                # max because of cases like [1, 5], [2, 4]
                output[-1][1] = max(last_end, end)
            else:
                # No overlapping, just add in output
                output.append([start, end])

        return output
