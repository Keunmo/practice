# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.data = []
        self.length = k

        
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if len(self.data) == self.length: return False
        else:
            self.data.insert(0,value)
            return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if len(self.data) == 0:
            return False
        else:
            self.data.pop()
            return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if len(self.data) == 0:
            return -1
        else:
            return self.data[-1]

        
    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if len(self.data) == 0:
            return -1
        else:
            return self.data[0]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if len(self.data) == 0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if len(self.data) == self.length:
            return True
        else:
            return False
        """
        Checks whether the circular queue is full or not.
        """
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()