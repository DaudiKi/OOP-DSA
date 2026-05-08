# OOP Foundations for Data Structures – Assignment 1 

## Repository Structure

```
.
├── node_basics.py   # Node class + manual linking
├── linked_list.py   # LinkedList class with append/display/search
└── README_Daudi -189657.md     # Conceptual answers
```

---

## How to Run

```bash
python node_basics.py
python linked_list.py
```

No third-party libraries are required; everything uses plain Python 3.

---

## Part 4: Concept Questions

### 1. What is the role of a class in a linked list?

A class acts as a **blueprint** for the building blocks of a linked list.
There are typically two classes involved:

- **`Node`** – defines what a single element looks like (it holds a piece of data
  and a reference to the next node).
- **`LinkedList`** – defines the list itself and the operations you can perform on
  it (append, search, delete, display, etc.).

Without classes we would have to manage raw variables and pointers by hand for
every node, which would quickly become unmanageable. By bundling data and
behaviour together inside a class, we get reusable, readable, and maintainable
code.

---

### 2. What is the difference between a node and a linked list?

| | **Node** | **Linked List** |
|---|---|---|
| What it is | A single container | A chain of containers |
| What it stores | One value + a pointer to the next node | A reference to the *head* node (the first one) |
| Analogy | A single train carriage | The entire train |

A **node** only knows about itself and the node that comes immediately after it.
A **linked list** knows about the whole chain — it keeps track of the head node
and provides methods to work with the entire sequence.

---

### 3. Why do we use `None` in `next`?

`None` is Python's way of saying "there is nothing here."  Setting
`next = None` in a node signals that **this node is the last one in the list** —
there is no node after it.

It also serves as the **stopping condition** when traversing the list:

```python
current = self.head
while current is not None:   # keep going until we fall off the end
    print(current.data)
    current = current.next
```

Without `None` as a sentinel value, the traversal loop would have no way to
know when it had reached the end, and it would crash or loop forever.

---

### 4. How is a linked list different from a Python list?

| Feature | **Python list** | **Linked list** |
|---|---|---|
| Memory layout | Contiguous block (like an array) | Scattered nodes connected by pointers |
| Index access | O(1) – instant (`my_list[3]`) | O(n) – must walk from head |
| Insert / delete at start | O(n) – all items must shift | O(1) – just update a pointer |
| Insert / delete at end | O(1) amortised | O(n) – must walk to the tail |
| Memory overhead | Low (stores values only) | Higher (each node also stores a pointer) |
| Dynamic resizing | Handled automatically | Handled naturally by pointer reassignment |

**Summary:** Python lists are better when you need fast random access by index.
Linked lists are better when you frequently insert or remove items at the
beginning (or middle) of the sequence.

---

### 5. Why is OOP useful for data structures?

OOP brings several advantages when implementing data structures:

1. **Encapsulation** – The internal details (how nodes are linked, where the head
   is) are hidden inside the class. Users of the class only call `append()` or
   `search()` without needing to know how they work internally.

2. **Abstraction** – Complex pointer manipulation is wrapped in simple method
   names. `ll.append(42)` is far clearer than writing the traversal and linking
   code every time.

3. **Reusability** – Once a `LinkedList` class is written and tested, it can be
   imported and reused in any project without rewriting the logic.

4. **Extensibility** – You can extend the class (e.g., add a `delete()` method or
   subclass it to create a `DoublyLinkedList`) without changing existing code.

5. **Readability** – Grouping related data and behaviour under one class name
   makes the code easier to read, understand, and debug.

These same benefits apply equally to trees, stacks, queues, and graphs —
essentially every data structure taught in this course.
