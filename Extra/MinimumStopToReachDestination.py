"""
Ninja bought a plane that can cover a distance of at most ‘K’ units in one flight. Now, the ninja wants to show this
plane to his best friend, whose house lies at point (X, 0) on the x-axis. There are multiple airports on the x-axis
marked by 1. If there is no airport at any point, then it is marked as 0.

Given an integer array ‘AIRPORTS’ of size ‘N’ containing the information about airports on the x-axis, can you find
the minimum number of stops that must be taken by the plane to reach the destination (X,0) on the x-axis. If the
destination is unreachable, return -1. The plane starts from the origin (0, 0).

For example:
You are given AIRPORTS = [1, 1, 1, 0, 1, 0], ‘K’ = 2 and ‘X’ = 4.
The answer will be 1. The plane makes its first stop at (2, 0) and then reaches the destination (4, 0) in the next
fight. Hence, the total number of stops is 1.

Sample Input 1:
6 2 4
1 1 1 0 1 0

4 3 3
1 0 1 1

Sample Output 1:
 1
 0


Constraints:
1 <= N <= 5000
1 <= K < N
1 <= X < N
0 <= AIRPORTS[i] <= 1
"""

from typing import List


def minStops(n: int, k: int, x: int, airports: List[int]) -> int:
    # write your code here
    if (airports[x] == 0):
        return -1

    stops = 0
    i = 0
    while i < n - k:
        j = i + k
        while j > i and not airports[j]:
            j -= 1

        if j == i:
            return -1

        if x <= j:
            break

        stops += 1
        i = j
    return stops