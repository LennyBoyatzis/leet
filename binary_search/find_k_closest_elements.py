from typing import List


# Time Complexity O(n log n)
# Space Complexity O(k)

def sort_elements_from_target(arr: List[int], k_nums: int, target: int):
     differences = sorted(arr, key=lambda x: abs(target - x))[:k_nums]
     return sorted(differences)


def binary_search(arr: List[int], target: int):
    left, right = 0, len(arr) - 1

    while left <= right:
        pivot = left + (right - left) // 2

        if arr[pivot] == target:
            return pivot
        elif arr[pivot] > target:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1

# Runtime Complexity
# O(log n + k)
# O(log n) - for binary search
# O(k) - for shrinking to k elements

# Space Complexity
# O(k) - generate and return sublist


def find_closest_elements(arr: List[int], k_nums: int, target: int):
    left, right = 0, len(arr) - 1

    if target < arr[left]:
        return arr[:k_nums]

    if target > arr[right]:
        return arr[-k_nums:]

    target_index = binary_search(arr, target)

    if target_index >= 0:
        left = max(0, target_index - k_nums - 1)
        right = min(len(arr) - 1, target_index + k_nums - 1)

    while (right - left) + 1 != k_nums:
        left_diff = abs(arr[left] - target)
        right_diff = abs(arr[right] - target)

        if left_diff > right_diff:
            left += 1
        else:
            right -= 1

    return arr[left: right + 1]


if __name__ == '__main__':
    nums = [0, 0, 1, 2, 3, 3, 4, 7, 7, 8]
    k_nums = 3
    target = 5
    result = find_closest_elements(nums, k_nums, target)
    print(f'result -> {result}')
