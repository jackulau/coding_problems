# Problem: Design Dynamic Array (Resizable Array)
# Platform: neetcode
# Difficulty: Easy
# Language: python
# Synced: 2026-05-12T02:49:25.287Z
class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None: