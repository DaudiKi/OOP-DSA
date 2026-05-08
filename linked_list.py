# Part 3: Simple Linked List
# A LinkedList class built using the Node class


class Node:
    """A single node that holds data and a reference to the next node."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list supporting append, display, and search."""

    def __init__(self):
        self.head = None   # The list starts empty; head points to nothing

    def append(self, data):
        """Add a new node with the given data at the end of the list."""
        new_node = Node(data)

        # If the list is empty, the new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, walk to the last node and attach the new node there
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        """Print all values in the list from head to tail."""
        if self.head is None:
            print("The list is empty.")
            return

        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next

        print(" -> ".join(elements) + " -> None")

    def search(self, data):
        """
        Search for a value in the list.
        Returns the 0-based index if found, or -1 if not found.
        """
        current = self.head
        index = 0
        while current is not None:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1


# ---------------------------------------------------------------------------
# Demo / manual test
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    ll = LinkedList()

    # Append some values
    for value in [5, 15, 25, 35, 45]:
        ll.append(value)

    print("Linked list after appending 5 values:")
    ll.display()

    # Search for values
    print()
    for target in [25, 99]:
        result = ll.search(target)
        if result != -1:
            print(f"  search({target}) -> found at index {result}")
        else:
            print(f"  search({target}) -> not found in list")

    # Edge case: empty list
    print()
    empty = LinkedList()
    print("Display on empty list:")
    empty.display()
    print(f"search(10) on empty list -> index {empty.search(10)}")
