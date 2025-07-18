import random


class BinarySearch:
    def __init__(self, length):
        self.arr = []
        self.set_array(length)

    def set_array(self, length):
        self.arr = [random.randint(0, 100) for _ in range(length)]

    def get_array(self):
        return self.arr

    def bs(self, target):
        arr = sorted(self.arr)
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (right + left) // 2

            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1

    def is_pair(self, target):
        arr = sorted(self.arr)
        left = 0
        right = len(arr) - 1

        while left <= right:
            if (arr[left] + arr[right]) == target:
                return True  # Found a pair that matches the target
            # In case the target is lower than the sum of arr elements is lower than the target shift left pointer by one to the right
            elif (arr[left] + arr[right]) < target:
                left += 1
            # This code will only exectue once the sum of arr elements is greater than the target
            # It'll shift the right pointer by one to the left
            else:
                right -= 1
        # return False if target not found before
        return False


# Przykład użycia
bs_obj = BinarySearch(20)
print("Array (Unsorted):", bs_obj.get_array())
target = 42
result = bs_obj.bs(target)
print(f"Target {target} found at index (After sorting): ", result)

# Przykład urzycia Two pointers
result = bs_obj.is_pair(target)
print(result)
