from typing import List
import string

alphabet = string.ascii_lowercase


def next_greatest_letter(letters: List[str], target: str):
    left, right = 0, len(letters)

    while left < right:
        pivot = left + (right - left) // 2
        if letters[pivot] <= target:
            left = pivot + 1
        else:
            right = pivot
    return letters[left % len(letters)]


if __name__ == '__main__':
    letters = ['c', 'f', 'j']
    target = 'j'
    result = next_greatest_letter(letters, target)
    print(f'result {result}')
