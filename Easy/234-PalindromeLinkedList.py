"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
    The number of nodes in the list is in the range [1, 10^5].
    0 <= Node.val <= 9
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Solution: Using Two Pointer -> Time: O(n), Space: O(1)
        if not head:
            return True

        # Find the mid of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        prev = None
        cur = slow
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

        # Solution: Using Recursion -> Time: O(n), Space: O(n)
        def recursivePal(head):
            # Base Condition
            if not head:
                return True
            right = recursivePal(head.next)
            self.left = self.left.next
            if right and self.left.val == head.val:
                return True
            return False

        self.left = ListNode()
        self.left.next = head
        return recursivePal(head)

        # Solution: Using stack -> Time: O(n), Space: O(n)
        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next

        curr = head
        while curr:
            if curr.val != stack.pop():
                return False
            curr = curr.next
        return True
