class Stack:
    """
    A class to represent a stack using a list.
    """
    def __init__(self):
        self.values = []
    
    def push(self, x):
        """
        Pushes an element onto the stack.
        """
        try:
            self.values = [x] + self.values
        except Exception as e:
            print("Error pushing element:", e)
    
    def pop(self):
        """
        Pops the top element from the stack.
        """
        try:
            if not self.values:
                raise IndexError("Pop from empty stack.")
            return self.values.pop(0)
        except Exception as e:
            print("Error popping element:", e)

if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    print("Stack after pushes:", s.values)
    print("Popped element:", s.pop())
    print("Stack after pop:", s.values)