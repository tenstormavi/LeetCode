"""
Given a number 'x', and a range of 'y' and 'z', please find the count of all the numbers 'n' in that range, such
that the product of the number 'n' and 'x' does not contain any digit from the number 'n'.

Eg.
x = 2, y = 10, z = 15

2 * 10 = 20 // invalid since product contains 0 from 10
2 * 11 = 22 // valid
2 * 12 = 24 // invalid
2 * 13 = 26 // valid
2 * 14 = 28 // valid
2 * 15 = 30 // valid

Output = 4

Constraint: All the inputs will be integers and below 10^5
"""


def nonRepeatingDigitProductCount(x, y, z):
    count = 0
    for rang in range(y, z + 1):
        prod = x * rang
        flag = True
        for i in list(str(rang)):
            if i in list(str(prod)):
                flag = False
                break
        if flag:
            count += 1
    return count


print(nonRepeatingDigitProductCount(x=2,y=10,z=15))
