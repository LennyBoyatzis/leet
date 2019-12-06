from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        intervals.sort(key=lambda x: x[0])
        start, end = intervals[0][0], intervals[0][1]
        merged = []

        for next_start, next_end in intervals:
            if next_start > end:
                merged.append([start, end])
                start, end = next_start, next_end
            elif next_end > end:
                end = next_end

        merged.append([start, end])
        return merged


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = merge(intervals)
