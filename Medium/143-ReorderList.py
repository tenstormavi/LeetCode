"""
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
    The number of nodes in the list is in the range [1, 5 * 10^4].
    1 <= Node.val <= 1000
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def reverse(head, prev=None):
            cur = None
            while head:
                cur = head
                head = head.next
                cur.next = prev
                prev = cur
            return cur

        def merge(first, second):
            if not first or not second:
                return

            first_next = first.next
            second_next = second.next

            first.next = second
            if first_next:
                second.next = first_next

            merge(first_next, second_next)


        if not head:
            return head

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        second = slow.next
        slow.next = None

        # Reverse the second half
        reversed_second = reverse(second)

        # Solution: Iterative
        cur = head
        while reversed_second:
            next = cur.next
            cur.next = reversed_second
            cur = next

            reversed_second_next = reversed_second.next
            reversed_second.next = next
            reversed_second = reversed_second_next

            # Solution: Recursive
        merge(head, reversed_second)
