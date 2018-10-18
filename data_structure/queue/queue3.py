#implementation of queue with two stacks
from stack1 import LStack

class SQueue:
    def __init__(self):
        self.first = LStack()
        self.second = LStack()

    def empty(self):
        if self.first.empty() and self.second.empty():
            return True
        return False

    def enqueue(self, data):
        self.first.push(data)

    def dequeue(self):
        if self.empty():
            return None
        
        if self.second.empty():
            while not self.first.empty():
                self.second.push(self.first.pop())

        return self.second.pop()

    def peek(self):
        if self.empty():
            return None

        if self.second.empty():
            while not self.first.empty():
                self.second.push(self.first.pop())
        
        return self.second.peek()

if __name__ == "__main__":
    q= SQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    while not q.empty():
        print(q.dequeue(), end= '  ')