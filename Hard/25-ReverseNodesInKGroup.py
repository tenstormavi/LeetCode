"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes
is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
    The number of nodes in the list is n.
    1 <= k <= n <= 5000
    0 <= Node.val <= 1000
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # solution 1: Iterative
        if k == 1:
            return head

        def find_end(cur, k):
            while k > 1 and cur.next:
                cur = cur.next
                k -= 1
                if k == 1:
                    return cur
            return None

        def reverse(start, end):
            prev = None
            cur = start
            new_group_start = end.next
            while cur != new_group_start:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next

        new_head = ListNode()
        prev_group = new_head
        while head:
            group_start = head
            group_end = find_end(group_start, k)
            if not group_end:
                # not enough nodes to make a new group
                break
            # save link to the next group start
            next_group_start = group_end.next
            # reverse the current group
            reverse(group_start, group_end)
            # group_end is the start of the reversed group
            prev_group.next = group_end
            # group_start is the end of the reversed group
            prev_group = group_start
            # link current reversed group with the next group
            group_start.next = next_group_start
            # move current point to the start of the next group
            head = next_group_start

        return new_head.next

        # Solution 2: Recursive
        # Check if we need to reverse the group
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next

        # Reverse the group
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # After reverse, we know that `head` is the tail of the group.
        # And `curr` is the next pointer in original linked list order
        head.next = self.reverseKGroup(curr, k)
        return prev
