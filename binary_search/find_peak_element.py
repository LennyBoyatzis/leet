from typing import List


def search(nums: List[int], left: int, right: int):
    if left == right:
        return left

    pivot = left + (right - left) // 2

    if nums[pivot] > nums[pivot + 1]:
        return search(nums, left, pivot)
    return search(nums, pivot + 1, right)


def find_peak_element(nums: List[int]):
    return search(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    nums = [1, 2, 1, 3, 5, 6, 4]
    result = find_peak_element(nums)
    print(f'result -> {result}')
