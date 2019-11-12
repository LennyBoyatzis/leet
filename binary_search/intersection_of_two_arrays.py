from typing import List


# O(n + m)
def intersection(nums1: List[str], nums2: List[str]):
    """Computes the intersection of two arrays"""
    return list(set(nums1).intersection(set(nums2)))


# O(n x m)
def brute_force(nums1: List[str], nums2: List[str]):
    intersection = []
    for index, num in enumerate(nums1):
        if num in nums2 and num not in intersection:
            intersection.append(num)
    return intersection


if __name__ == '__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    result = brute_force(nums1, nums2)
    print(f'result {result}')
