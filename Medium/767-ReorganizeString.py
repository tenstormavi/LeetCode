"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.

Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""

Constraints:
    1 <= s.length <= 500
    s consists of lowercase English letters.
"""

from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        # Approach: Storing characters sorted by their frequency in descending order.
        # Taking out the character with maximum frequency and having a lock on it until the next selection.
        count = Counter(s) # Hashmap, count each character

        heap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(heap)

        res = ""

        # Approach 1:
        prev = None
        while heap or prev:
            if prev and not heap:
                return ""

            cnt, char = heappop(heap)
            res += char
            cnt += 1 # should be minus since negative hence adding

            if prev:
                heappush(heap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]
        return res

        # Approach 2:
        while len(heap) >= 2:
            cnt1, char1 = heappop(heap)
            res += char1

            cnt2, char2 = heappop(heap)
            res += char2

            if cnt1 + 1 < 0:
                heappush(heap, [cnt1 + 1, char1])

            if cnt2 + 1 < 0:
                heappush(heap, [cnt2 + 1, char2])

        if heap:
            cnt, char = heappop(heap)
            if -cnt > 1:
                return ""
            res += char
        return res
