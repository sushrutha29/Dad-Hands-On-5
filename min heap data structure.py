class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) >> 1

    def left(self, i):
        return (i << 1) + 1

    def right(self, i):
        return (i << 1) + 2

    def build_min_heap(self, arr):
        self.heap = arr[:]
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        small = i
        l = self.left(i)
        r = self.right(i)

        if l < len(self.heap) and self.heap[l] < self.heap[small]:
            small = l
        if r < len(self.heap) and self.heap[r] < self.heap[small]:
            small = r

        if small != i:
            self.heap[i], self.heap[small] = self.heap[small], self.heap[i]
            self.heapify(small)

    def push(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return root

# Example 1
heap1 = MinHeap()
heap1.build_min_heap([23, 18, 3, 19, 25])
print("Example 1 - Original heap:", heap1.heap)
heap1.push(15)
print("Example 1 - Heap after push(15):", heap1.heap)
popped_value1 = heap1.pop()
print(f"Example 1 - Popped value: {popped_value1}")
print("Example 1 - Heap after pop:", heap1.heap)
print("\n")

# Example 2
heap2 = MinHeap()
heap2.build_min_heap([3, 5, 9, 2, 24])
print("Example 2 - Original heap:", heap2.heap)
heap2.push(10)
print("Example 2 - Heap after push(10):", heap2.heap)
popped_value2 = heap2.pop()
print(f"Example 2 - Popped value: {popped_value2}")
print("Example 2 - Heap after pop:", heap2.heap)
print("\n")

# Example 3
heap3 = MinHeap()
heap3.build_min_heap([21, 14, 32, 18, 27])
print("Example 3 - Original heap:", heap3.heap)
heap3.push(15)
print("Example 3 - Heap after push(15):", heap3.heap)
popped_value3 = heap3.pop()
print(f"Example 3 - Popped value: {popped_value3}")
print("Example 3 - Heap after pop:", heap3.heap)
