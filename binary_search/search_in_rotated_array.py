from typing import List


def find_rotation(nums: List[int]) -> int:
    """Finds index of the rotation in a sorted array"""
    left, right = 0, len(nums) - 1

    if nums[left] < nums[right]:
        return 0

    while left <= right:
        pivot = left + (right - left) // 2

        if nums[pivot] > nums[pivot + 1]:
            return pivot + 1
        elif nums[pivot] < nums[left]:
            right = pivot - 1
        else:
            left = pivot + 1


def find_target(nums: List[int], left: int, right: int, target: int) -> int:
    while left <= right:
        pivot = left + (right - left) // 2

        if nums[pivot] == target:
            return pivot
        elif nums[pivot] > target:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1


def search(nums: List[int], target: int) -> int:
    """Performs binary search on list containing one rotation"""

    n = len(nums)

    if n == 0:
        return -1

    if n == 1:
        return 0 if nums[0] == target else -1

    left, right = 0, len(nums) - 1
    rotation_index = find_rotation(nums)

    if rotation_index == 0:
        return find_target(nums, left, right, target)

    if nums[left] <= target <= nums[rotation_index - 1]:
        return find_target(nums, left, rotation_index, target)

    if nums[rotation_index] <= target <= nums[right]:
        return find_target(nums, rotation_index, right, target)

    return -1


if __name__ == '__main__':
    nums = [1, 3]
    target = 0
    result = search(nums, target)
