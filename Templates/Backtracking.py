"""
BackTracking Template
"""

# Backtracking == DFS on a tree

# Time Complexity:
# For each node there are a maximum of 2 children. The height of the tree is n.
# The number of nodes is 2^n-1 or O(2^n). It takes O(n) to join the n characters at each leaf node.
# So the overall time complexity is O(2^n*n).

# Space Complexity:
# We store 2^n strings in total, each with a length of n so this gives us O(2^n*n) space.
# In addition, our recursion depth is O(n). Adding the two together, we still get a
# space complexity of O(2^n*n).

"""
TEMPLATE:

function dfs(start_index, path):
  if is_leaf(start_index):
    report(path)
    return

  for edge in get_edges(start_index):
    path.add(edge)
    dfs(start_index + 1, path)
    path.pop()
"""

# For all 2-letter words composed using only 'a' and 'b':
# ["aa", "ab", "ba", "bb"]

def letter_combination(n):
    def dfs(start_index, path, used):
        if start_index == n:
            res.append(path[:])
            return

        for i, letter in enumerate(['a','b']):
            if used[i]:
                continue
            path.append(letter)
            # used[i] = True
            dfs(start_index+1, path, used)
            path.pop()
            used[i] = False

    res = []
    dfs(0, [], [False] * n)
    return res


if __name__ == '__main__':
    n = 2
    res = letter_combination(n)
    for line in sorted(res):
        print(line)
