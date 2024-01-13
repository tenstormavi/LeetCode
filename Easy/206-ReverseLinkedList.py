"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Return head for empty head or only head
        if not head or not head.next:
            return head

        # Initialize prev pointer as NULL
        prev = None

        # Initialize the curr pointer as the head
        cur = head

        # Run a loop till curr points to NULL
        while cur:
            # Initialize next pointer as the next pointer of curr
            next = cur.next

            # Now assign the prev pointer to curr’s next pointer.
            cur.next = prev

            # Assign curr to prev, next to curr
            prev = cur
            cur = next

        # Return the prev pointer to get the reverse linked list
        return prev
