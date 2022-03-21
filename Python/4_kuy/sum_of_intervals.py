def sum_of_intervals(intervals: list) -> int:
    result: set = set()
    for interval in intervals:
        result.update(range(interval[0], interval[1]))
    return len(result)


if __name__ == "__main__":
    print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
    print(sum_of_intervals([(1, 5), (6, 10)]))
    print(sum_of_intervals([(1, 5), (1, 5)]))
