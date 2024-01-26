"""
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support
all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:
    void push(int x) Pushes element x to the top of the stack.
    int pop() Removes the element on the top of the stack and returns it.
    int top() Returns the element on the top of the stack.
    boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
    You must use only standard operations of a queue, which means that only push to back, peek/pop from front,
    size and is empty operations are valid.
    Depending on your language, the queue may not be supported natively. You may simulate a queue using a list
    or deque (double-ended queue) as long as you use only a queue's standard operations.

Example 1:
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

Constraints:
    1 <= x <= 9
    At most 100 calls will be made to push, pop, top, and empty.
    All the calls to pop and top are valid.

Follow-up: Can you implement the stack using only one queue?
"""


class MyStack:

    def __init__(self):
        # Solution - One queue
        self.q = deque()

        # Solution - Two queue
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # Solution - One queue
        self.q.append(x)

        # Solution - Two queue
        self.q1.append(x)

    def pop(self) -> int:
        # Solution - One queue
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

        # Solution - Two queue
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.popleft())

        popped_element = self.q1.popleft()

        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

        return popped_element

    def top(self) -> int:
        # Solution - One queue
        return self.q[-1]

        # Solution - Two queue
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.popleft())

        top_element = self.q1[0]

        self.q2.append(self.q1.popleft())

        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

        return top_element

    def empty(self) -> bool:
        # Solution - One queue
        return len(self.q) == 0

        # Solution - Two queue
        return len(self.q1) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
