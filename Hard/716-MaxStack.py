"""
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:
    MaxStack() Initializes the stack object.
    void push(int x) Pushes element x onto the stack.
    int pop() Removes the element on top of the stack and returns it.
    int top() Gets the element on the top of the stack without removing it.
    int peekMax() Retrieves the maximum element in the stack without removing it.
    int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element,
    only remove the top-most one.

You must come up with a solution that supports O(1) for each top call and O(logn) for each other call.

Example 1:
Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation
MaxStack stk = new MaxStack();
stk.push(5);   // [5] the top of the stack and the maximum number is 5.
stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, 5] the stack did not change.
stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [5, 1] the stack did not change.
stk.peekMax(); // return 5, [5, 1] the stack did not change.
stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
stk.top();     // return 5, [5] the stack did not change.

Constraints:
    -10^7 <= x <= 10^7
    At most 105 calls will be made to push, pop, top, peekMax, and popMax.
    There will be at least one element in the stack when pop, top, peekMax, or popMax is called.
"""
from collections import defaultdict
from sortedcontainers import SortedList
from heapq import heappop, heappush


# Solution 1: Using inbuilt python sorted containers library

class MaxStack:

    def __init__(self):
        self.stack = SortedList()
        self.values = SortedList()
        self.cnt = 0

    def push(self, x: int) -> None:
        # O(log(n))
        self.stack.add((self.cnt, x))
        self.values.add((x, self.cnt))
        self.cnt += 1

    def pop(self) -> int:
        # O(1)
        idx, num = self.stack.pop()
        self.values.remove((num, idx))
        return num

    def top(self) -> int:
        # O(1)
        return self.stack[-1][1]

    def peekMax(self) -> int:
        # O(1)
        return self.values[-1][0]

    def popMax(self) -> int:
        # O(log(n))
        num, idx = self.values.pop()
        self.stack.remove((idx, num))
        return num


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

###############################################################################
# Solution 2: Using Doubly Linkedlist + hashmap + max heap

class DoubleLinkedList:

    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None


class MaxStack:

    def __init__(self):
        self.stack = DoubleLinkedList(float('-inf'))
        self.tail = self.stack
        self.heap = []
        self.cache = defaultdict(list)

    def push(self, x: int) -> None:
        # O(log(n))
        node = DoubleLinkedList(x)

        # update the tail
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

        # Insert into max heap
        heappush(self.heap, -x)

        # Add node to cache map
        self.cache[x].append(node)

    def pop(self) -> int:
        # O(1)
        # pop from stack
        num = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None

        # remove from cache
        self.cache[num].pop()
        if not self.cache[num]:
            del self.cache[num]

        return num

    def top(self) -> int:
        # O(1)
        return self.tail.val

    def peekMax(self) -> int:
        # O(log(n))
        # during the pop(), we didn't remove the element from heap
        # So here is to remove the poped elements from heap
        while -self.heap[0] not in self.cache:
            heappop(self.heap)

        return -self.heap[0]

    def popMax(self) -> int:
        # O(log(n))
        # get the top-most node from map
        num = self.peekMax()
        node = self.cache[num].pop()
        if not self.cache[num]:
            del self.cache[num]

        # update the tail reference
        if node == self.tail:
            self.tail = self.tail.prev

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        return num

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
