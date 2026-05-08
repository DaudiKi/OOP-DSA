# Part 2: Basic OOP Practice
# Creating a Node class and manually linking nodes


class Node:
    """A single node that holds data and a reference to the next node."""

    def __init__(self, data):
        self.data = data   # The value stored in the node
        self.next = None   # Pointer to the next node (None by default)


# --- Manually create 3 nodes ---
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# --- Link the nodes together ---
node1.next = node2   # node1 -> node2
node2.next = node3   # node2 -> node3
# node3.next remains None (end of the chain)

# --- Traverse and print values ---
print("Traversing manually linked nodes:")
current = node1
while current is not None:
    print(f"  Node data: {current.data}")
    current = current.next

print("\nDone traversing.")
