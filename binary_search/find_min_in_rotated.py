from typing import List


def find_min(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    n = len(nums)

    if n == 1:
        return nums[left]

    if nums[left] < nums[right]:
        return nums[left]

    while left < right:
        pivot = left + (right - left) // 2

        if nums[pivot] > nums[pivot + 1]:
            return nums[pivot + 1]
        elif nums[pivot] < nums[left]:
            right = pivot - 1
        else:
            left = pivot + 1


if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    result = find_min(nums)
    print(f'what is the result {result}')
