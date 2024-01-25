"""

"""


class MedianFinder:

    def __init__(self):
        # Approach: we have to sort the array everytime an element gets added
        # which can worst take O(n), to reduce the time can use 2 heaps.

        # Small - maxHeap, Large - minHeap O(log(n))
        # Conditions: heaps should be equal size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # Always push in small heap first
        heappush(self.small, -1 * num)

        # make sure every num in small is <= every num in large
        if (small and large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heappop(self.small)
            heappush(self.large, val)

        # Size uneven?
        if len(self.small) > len(self.large) + 1:
            val = -1 * heappop(self.small)
            heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heappop(self.large)
            heappush(self.small, -1 * val)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()