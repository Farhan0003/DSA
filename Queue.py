class Queue:
    """
    A class to represent a queue using a list.
    """
    def __init__(self):
        self.values = []
    
    def enqueue(self, x):
        """
        Adds an element to the end of the queue.
        """
        try:
            self.values.append(x)
        except Exception as e:
            print("Error enqueuing element:", e)
    
    def dequeue(self):
        """
        Removes and returns the front element of the queue.
        """
        try:
            if not self.values:
                raise IndexError("Dequeue from empty queue.")
            front = self.values[0]
            self.values = self.values[1:]
            return front
        except Exception as e:
            print("Error dequeuing element:", e)
    
    def peek(self):
        """
        Returns the front element of the queue without removing it.
        """
        try:
            if not self.values:
                raise IndexError("Peek from empty queue.")
            return self.values[0]
        except Exception as e:
            print("Error peeking element:", e)

if __name__ == "__main__":
    q1 = Queue()
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    print("Queue after enqueues:", q1.values)
    print("Dequeued element:", q1.dequeue())
    print("Queue after dequeue:", q1.values)
    print("Front element (peek):", q1.peek())