"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

Follow up: Could you do this in one pass?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Approach 1: Reverse the linkedlist and remove the first nth node

        # Approach 2: Use two pointer and create an offset of n node between them
        # Then remove the node next to left pointer

        slow = fast = head

        # Move fast to nth position
        for i in range(n):
            fast = fast.next

        # Check if fast exists -> in case of [1] and n = 1
        if not fast:
            return head.next

        # Move both slow and fast pointer till fast reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Delete the next pointer of slow, i.e the nth element from the end
        slow.next = slow.next.next

        return head