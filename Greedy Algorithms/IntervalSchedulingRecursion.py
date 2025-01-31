# Interval Scheduling using Recursion

# Time Complexity: O(n log n) (Sorting)
# Space Complexity: O(n) (Recursion stack)

def interval_scheduling_recursive(intervals, n, prev_end=0, index=0):
    """
    Recursive function to select the maximum number of non-overlapping intervals.
    :param intervals: List of (start_time, end_time)
    :param n: Number of intervals
    :param prev_end: End time of previously selected interval
    :param index: Current index in the intervals list
    :return: List of selected intervals
    """
    if index >= n:
        return []

    # Select the current interval if it doesn't overlap
    if intervals[index][0] >= prev_end:
        return [(intervals[index][0], intervals[index][1])] + interval_scheduling_recursive(
            intervals, n, intervals[index][1], index + 1)

    # Skip this interval and move to the next one
    return interval_scheduling_recursive(intervals, n, prev_end, index + 1)


# Example Usage:
intervals = [(1, 3), (2, 5), (4, 6), (6, 8), (5, 9), (7, 9)]
intervals.sort(key=lambda x: x[1])  # Sort intervals before passing
print(f"Selected Intervals (Recursive): {interval_scheduling_recursive(intervals, len(intervals))}")
