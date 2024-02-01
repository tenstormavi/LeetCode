"""
There is a computer network consisting of n servers, or nodes, numbered from 1 to n, and each node has a security
value security_val[J]. A hacker must choose a starting node, start jumping through the network compromising servers
along the way until reaching the end. From node x, the hacker can jump to node (x + k). If node (x+ k) does not exist,
the jump is out of the network and the hack ends. Initially, the hacker has access to 0 servers with 0 security value.
The security value at each compromised node is added to the hacker's security value sum, and values may be negative.
The task is to choose the starting node optimally such that the hacker compromises servers with the maximum possible
security value sum.

Example:
Given, n = 5, security_val = [2, -3, 4, 6, 1], and k = 2.
Choose node index = 1 as starting node
2 + 4 + 1 = 7
The security value sum is security_val[1] + security_val[3] + security_val[5] = 2 + 4 + 1 = 7.
"""


def solve(nums, k):
    n = len(nums)
    dp = [0] * (n)
    for i in range(n - 1, -1, -1):
        if i + k < n:
            dp[i] = nums[i] + (dp[i + k])
        else:
            dp[i] = nums[i]
    # print(dp)
    return max(dp)


print(solve([2, -3, 4, 6, 1], 2))
print(solve([1], 1))
print(solve([-3, -5, -1, -8, -4, -5], 3))
print(solve([0, 0, 0, 0, 0], 3))
print(solve([2, -3, 4, 6, 1], 1))
