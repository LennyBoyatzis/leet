from typing import List
from collections import defaultdict


# How can you tell if 2 words are anagrams?
def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    return len(set(word1) - set(word2)) == 0


def group_anagrams(strs: List[str]) -> List[List[str]]:
    group = defaultdict(list)

    for word in strs:
        count = sum([ord(char) for char in word])
        group[count].append(word)

    result = []

    for key, anagrams in group.items():
        result.append(anagrams)

    return result


if __name__ == '__main__':
    words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    result = group_anagrams(words)

    print(f'result {result}')
