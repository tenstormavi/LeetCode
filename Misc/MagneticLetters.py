"""
It is your little brother Louie's birthday in a few days.So you decided to buy a magnetic letterbox for him as a
present. Louie wants to construct two strings using all the letters in the box. Your task is to determine whether he
can construct both strings using all of the letters in the box or no. InputThe first and the second line of the input
contain two strings S, and S2, representing the strings that Louie wants to construct.The third line of the input
contains string R representing all the letters in the magnetic lettersDOX.

Note: Strings only contain uppercase Latin lettersOutputPrint
"Yes" if Louie can construct given strings using all the letters in the box .Otherwise, print "No".
Print answer without the quotes.

"""
from collections import Counter


def solve(s1, s2, r):
    freq = Counter(r)

    s1 = list(s1)
    s2 = list(s2)

    for c in s1:
        if freq[c] > 0:
            freq[c] -= 1
        else:
            return "No"

    for c in s2:
        if freq[c] > 0:
            freq[c] -= 1
        else:
            return "No"

    # print(freq)
    for count in freq.values():
        if count > 0:
            return "No"
    return "yes"

print(solve("SAM", "JOHN", "SAMJOHN"))
print(solve("SAM", "JOHN", "SAMLJOHN"))
print(solve("SAM", "JOHN", "SMJOHN"))
