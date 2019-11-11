from typing import List

OUT_OF_BOUNDS = 2147483647


class Reader():
    def __init__(self):
        self.array = [x for x in range(0, 10000, 2)]

    def get(self, k):
        if k > len(self.array) - 1:
            return OUT_OF_BOUNDS
        return self.array[k]


def search(reader: Reader, target: int):
    left, right = 0, 1

    while reader.get(right) < target:
        left = right
        right = right * 2

    while left <= right:
        pivot = left + (right - left) // 2
        pivot_val = reader.get(pivot)

        if pivot_val == target:
            return pivot
        if pivot_val > target:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1

    print(f'left {left}')
    print(f'right {right}')


if __name__ == '__main__':
    nums = [1, 2, 1, 3, 5, 6, 4]
    reader = Reader()
    target = 1000
    result = search(reader, target)
    print(f'result -> {result}')
