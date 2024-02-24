"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 10^9
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        # Get length
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        # Get the final rotation needed
        k = k % length
        if k == 0:
            return head

        # Move the pivot and rotate
        # Final cur will be at the pivot point
        # Pivot point = length - k - 1
        cur = head
        for i in range(length - k - 1):
            cur = cur.next

        new_head = cur.next
        cur.next = None
        tail.next = head

        return new_head
