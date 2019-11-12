from typing import List


def two_sum(numbers: List[int], target):
    left, right = 0, len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    result = two_sum(numbers, target)
    print(f'result -> {result}')
