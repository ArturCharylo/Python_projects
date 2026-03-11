import random
from typing import List

class BinarySearch:
    def __init__(self, length: int):
        self.arr: List[int] = []
        self.set_array(length)

    def set_array(self, length: int) -> None:
        """Initializes and sorts the array to allow efficient searching."""
        self.arr = sorted([random.randint(0, 100) for _ in range(length)])

    def get_array(self) -> List[int]:
        return self.arr

    def bs(self, target: int) -> int:
        """Standard Binary Search implementation on a pre-sorted array."""
        left = 0
        right = len(self.arr) - 1

        while left <= right:
            mid = (right + left) // 2

            if self.arr[mid] < target:
                left = mid + 1
            elif self.arr[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    def is_pair(self, target: int) -> bool:
        """Checks if two numbers in the array sum up to the target using two pointers."""
        left = 0
        right = len(self.arr) - 1

        while left < right:
            current_sum = self.arr[left] + self.arr[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return False

    def remove_duplicates(self) -> int:
        """Removes duplicates from the sorted array and resizes it."""
        if not self.arr:
            return 0

        write = 1
        # The array must be sorted for this logic to work correctly
        for read in range(1, len(self.arr)):
            if self.arr[read] != self.arr[read - 1]:
                self.arr[write] = self.arr[read]
                write += 1
        
        # Actually resize the array to the number of unique elements
        self.arr = self.arr[:write]
        return write

# Example usage
if __name__ == "__main__":
    bs_obj = BinarySearch(20)
    print("Array (Sorted at start):", bs_obj.get_array())
    
    target = 42
    result = bs_obj.bs(target)
    print(f"Target {target} found at index: {result}")

    pair_exists = bs_obj.is_pair(target)
    print(f"Does a pair for target {target} exist? {pair_exists}")

    unique_count = bs_obj.remove_duplicates()
    print(f"Array after removing duplicates (Size {unique_count}):", bs_obj.get_array())