def valid_perfect_square(num: int) -> bool:
    if num < 2:
        return True

    left, right = 2, num // 2

    while left <= right:
        pivot = left + (right - left) // 2
        pivot_squared = pivot**2

        if pivot_squared == num:
            print(f'pivot is {pivot}')
            return True
        elif pivot_squared > num:
            right = pivot - 1
        else:
            left = pivot + 1
    return False


if __name__ == '__main__':
    num = 4
    result = valid_perfect_square(num)
    print(f'result {result}')
