from typing import List


def extreme_insertion_index(nums: List[int], target: int, left):
    lo, hi = 0, len(nums)

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > target or (left and target == nums[mid]):
            hi = mid
        else:
            lo = mid + 1
    return lo


def search_range(nums: List[int], target: int) -> List[int]:
    left = extreme_insertion_index(nums, target, True)

    if left == len(nums) or nums[left] != target:
        return [-1, -1]

    return [left, extreme_insertion_index(nums, target, False)-1]


if __name__ == '__main__':
    nums = [1, 2, 5, 5, 5, 9]
    target = 5
    result = search_range(nums, target)
    print(f'what is the result -> {result}')
