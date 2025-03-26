class Node:
    """
    A class to represent a node in a singly linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """
    A class to represent a singly linked list.
    """
    def __init__(self):
        self.head = None

    def traversal(self):
        """
        Traverses and prints the linked list.
        """
        if self.head is None:
            print("Singly linked list is empty")
        else:
            a = self.head
            while a is not None:
                print(a.data, end=" -> ")
                a = a.next
            print("None")

    def insert_at_beginning(self, data):
        """
        Inserts a new node at the beginning of the linked list.
        """
        try:
            nb = Node(data)
            nb.next = self.head
            self.head = nb
        except Exception as e:
            print("Error inserting at the beginning:", e)

    def insert_at_end(self, data):
        """
        Inserts a new node at the end of the linked list.
        """
        try:
            ne = Node(data)
            if self.head is None:
                self.head = ne
                return
            a = self.head
            while a.next is not None:
                a = a.next
            a.next = ne
        except Exception as e:
            print("Error inserting at the end:", e)

    def insert_at_middle(self, position, data):
        """
        Inserts a new node at a specified position in the linked list.
        """
        try:
            if position < 1:
                raise ValueError("Position must be greater than 0.")
            nc = Node(data)
            a = self.head
            for i in range(1, position - 1):
                if a is None:
                    raise ValueError("Position out of bounds.")
                a = a.next
            nc.next = a.next
            a.next = nc
        except Exception as e:
            print("Error inserting in the middle:", e)

    def delete_in_beginning(self):
        """
        Deletes the first node of the linked list.
        """
        try:
            if self.head is None:
                raise ValueError("List is empty. Nothing to delete.")
            a = self.head
            self.head = a.next
            a.next = None
        except Exception as e:
            print("Error deleting at the beginning:", e)

    def delete_in_last(self):
        """
        Deletes the last node of the linked list.
        """
        try:
            if self.head is None:
                raise ValueError("List is empty. Nothing to delete.")
            if self.head.next is None:
                self.head = None
                return
            prev = self.head
            a = self.head.next
            while a.next is not None:
                a = a.next
                prev = prev.next
            prev.next = None
        except Exception as e:
            print("Error deleting at the end:", e)

    def delete_in_middle(self, position):
        """
        Deletes a node at a specified position in the linked list.
        """
        try:
            if position < 1:
                raise ValueError("Position must be greater than 0.")
            if self.head is None:
                raise ValueError("List is empty. Nothing to delete.")
            if position == 1:
                self.delete_in_beginning()
                return
            prev = self.head
            a = self.head.next
            for i in range(1, position - 1):
                if a is None or a.next is None:
                    raise ValueError("Position out of bounds.")
                a = a.next
                prev = prev.next
            prev.next = a.next
            a.next = None
        except Exception as e:
            print("Error deleting in the middle:", e)

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_beginning(5)
    sll.insert_at_end(10)
    sll.insert_at_end(15)
    print("Initial linked list:")
    sll.traversal()

    print("Inserted 2 at the beginning:")
    sll.insert_at_beginning(2)
    sll.traversal()

    print("Inserted 20 at the end:")
    sll.insert_at_end(20)
    sll.traversal()

    print("Inserted 12 in the middle (position 3):")
    sll.insert_at_middle(3, 12)
    sll.traversal()

    print("Deleted first element:")
    sll.delete_in_beginning()
    sll.traversal()

    print("Deleted last element:")
    sll.delete_in_last()
    sll.traversal()

    print("Deleted element from the middle (position 3):")
    sll.delete_in_middle(3)
    sll.traversal()
