def my_pow(x, n):
    if n == 0:
        return 1.0

    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    while n > 0:
        if n % 2 == 1:
            result = result * x
            x = x * x
            n = (n - 1) / 2
        else:
            x = x * x
            n = n / 2
    return result


if __name__ == '__main__':
    x = 2
    n = 10
    result = my_pow(x, n)
    print(f'result {result}')
