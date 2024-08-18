from heapq import heappush, heappop

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Initialize a min heap to store the k largest elements
        self.min_heap = []
        # Store the size k to know the kth largest value
        self.k = k
        # Add the initial elements to the heap
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Add the new value to the min heap
        heappush(self.min_heap, val)
        # If the size of the heap exceeds k, remove the smallest element
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        # The root of the min heap is the kth largest value
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)