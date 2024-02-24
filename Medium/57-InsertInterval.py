"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start
and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval
newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still
does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
    0 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti <= endi <= 10^5
    intervals is sorted by starti in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 10^5
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                # the new interval's range is before the other
                # New interval end time less than current's start time
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                # the new interval range is after the current interval
                res.append(intervals[i])
            elif newInterval[0] <= intervals[i][1] or newInterval[1] >= intervals[i][0]:
                # New interval's start time is less then interval's end time
                # New interval's end time is greater than interval's start time
                # Overlapping is there
                # There could be further overlapping so not appending right now. eg. [[1,2], [3, 4]] new = [0, 3]
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        # If the first if block never execute then we never added the new interval to result
        res.append(newInterval)

        return res
