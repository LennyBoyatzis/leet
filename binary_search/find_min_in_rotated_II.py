from typing import List


def find_min(nums: List[int]):
    left, right = 0, len(nums) - 1

    if nums[left] < nums[right]:
        return left

    while left < right:
        pivot = left + (right - left) // 2

        if nums[pivot] < nums[right]:
            right = pivot
        elif nums[pivot] > nums[right]:
            left = pivot + 1
        else:
            right -= 1
    return nums[left]


if __name__ == '__main__':
    nums = [3, 3, 3, 3, 3, 3, 3, 3, 1, 3]
    # nums = [3, 4, 5, 6, 9, 12, 21, 1, 2]
    result = find_min(nums)
    print(f'result -> {result}')
