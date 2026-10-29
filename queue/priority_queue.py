class PriorityQueue:

    def __init__(self):
        self.heap = []

    # Move element upward
    def heapify_up(self, i):

        while i > 0:

            parent = (i - 1) // 2

            # Compare priorities
            if self.heap[i][0] <= self.heap[parent][0]:
                break

            # Swap child and parent
            self.heap[i], self.heap[parent] = \
                self.heap[parent], self.heap[i]

            i = parent

    # Move element downward
    def heapify_down(self, i):

        n = len(self.heap)

        while True:

            left = i * 2 + 1
            right = i * 2 + 2

            largest = i

            # Check left child
            if left < n and self.heap[left][0] > self.heap[largest][0]:
                largest = left

            # Check right child
            if right < n and self.heap[right][0] > self.heap[largest][0]:
                largest = right

            # Correct position found
            if largest == i:
                break

            # Swap
            self.heap[i], self.heap[largest] = \
                self.heap[largest], self.heap[i]

            i = largest

    # Add element
    def enqueue(self, value, priority):

        self.heap.append((priority, value))

        # Heapify up from newly added element
        self.heapify_up(len(self.heap) - 1)

    # Remove highest priority element
    def dequeue(self):

        if not self.heap:
            return None

        # Highest priority is at root
        root = self.heap[0]

        # Remove last element
        last = self.heap.pop()

        # If heap still has elements
        if self.heap:

            # Move last element to root
            self.heap[0] = last

            # Restore Max Heap
            self.heapify_down(0)

        return root

    # View highest priority element
    def peek(self):

        if not self.heap:
            return None

        return self.heap[0]

    # Check whether queue is empty
    def is_empty(self):

        return len(self.heap) == 0

    # Display heap
    def display(self):

        print(self.heap)


# Create Priority Queue
pq = PriorityQueue()

# Add elements
pq.enqueue("A", 3)
pq.enqueue("B", 5)
pq.enqueue("C", 2)
pq.enqueue("D", 7)

# Display
print("Priority Queue:")
pq.display()

# Peek
print("Highest Priority:", pq.peek())

# Dequeue
print("Dequeue:", pq.dequeue())
print("Dequeue:", pq.dequeue())
print("Dequeue:", pq.dequeue())
print("Dequeue:", pq.dequeue())

# Check empty
print("Is Empty:", pq.is_empty())