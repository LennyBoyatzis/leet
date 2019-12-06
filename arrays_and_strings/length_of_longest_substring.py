def length_of_longest_substring(s: str) -> int:
    n = len(s)
    unique_chars = set()
    longest_length = 0

    for char in s:
        if char not in unique_chars:
            unique_chars.add(char)
            longest_length = max(longest_length, len(unique_chars))
        else:
            longest_length = max(longest_length, len(unique_chars))
            unique_chars = set(char)

    return longest_length


if __name__ == '__main__':
    string = 'aaaaaabbb'
    string2 = 'bbbbb'
    string3 = "dvdf"
    result = length_of_longest_substring(string3)
    print(f'result {result}')
