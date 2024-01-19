"""
Alice and Bob have a different total number of candies. You are given two integer arrays aliceSizes and
bobSizes where aliceSizes[i] is the number of candies of the ith box of candy that Alice has and bobSizes[j]
is the number of candies of the jth box of candy that Bob has.

Since they are friends, they would like to exchange one candy box each so that after the exchange, they both
have the same total amount of candy. The total amount of candy a person has is the sum of the number of
candies in each box they have.

Return an integer array answer where answer[0] is the number of candies in the box that Alice must
exchange, and answer[1] is the number of candies in the box that Bob must exchange. If there are multiple
answers, you may return any one of them. It is guaranteed that at least one answer exists.

Example 1:
Input: aliceSizes = [1,1], bobSizes = [2,2]
Output: [1,2]

Example 2:
Input: aliceSizes = [1,2], bobSizes = [2,3]
Output: [1,2]

Example 3:
Input: aliceSizes = [2], bobSizes = [1,3]
Output: [2,3]

Constraints:
    1 <= aliceSizes.length, bobSizes.length <= 10^4
    1 <= aliceSizes[i], bobSizes[j] <= 10^5
    Alice and Bob have a different total number of candies.
    There will be at least one valid answer for the given input.
"""


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # Solution 1:
        aliceSum = bobSum = 0
        for i in aliceSizes:
            aliceSum += i
        for i in bobSizes:
            bobSum += i

        # After exchange the sum should be same
        total_required = (aliceSum + bobSum) // 2
        for aliceGiven in aliceSizes:
            # if alice is giving his candies one by one
            needed_from_bob = total_required - (aliceSum - aliceGiven)
            if needed_from_bob in bobSizes:
                return [aliceGiven, needed_from_bob]
        return [0, 0]

        # Solution 2:
        delta = (sum(aliceSizes) - sum(bobSizes)) // 2
        aliceSizes = set(aliceSizes)
        for size in set(bobSizes):
            if delta + size in aliceSizes:
                return [delta + size, size]
