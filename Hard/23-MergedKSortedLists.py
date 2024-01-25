"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
    k == lists.length
    0 <= k <= 10^4
    0 <= lists[i].length <= 500
    -10^4 <= lists[i][j] <= 10^4
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 10^4.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Solution: using min heap
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        head = tail = ListNode()
        while heap:
            val, i = heappop(heap)
            tail.next = ListNode(val)
            tail = tail.next
            if lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        return head.next

        # Solution: using merge sort
        def mergeTwoList(list1, list2):
            new_head = tail = ListNode()
            while list1 and list2:
                if list1.val > list2.val:
                    tail.next = list2
                    list2 = list2.next
                else:
                    tail.next = list1
                    list1 = list1.next
                tail = tail.next

            if list1:
                tail.next = list1
            if list2:
                tail.next = list2

            return new_head.next

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(mergeTwoList(list1, list2))
            lists = mergedLists

        return lists[0]
