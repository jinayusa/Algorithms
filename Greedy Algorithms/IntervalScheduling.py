# Interval Scheduling using Greedy Algorithm

# Time Complexity: O(n log n) (Sorting)
# Space Complexity: O(1)

def interval_scheduling(intervals):
    """
    Function to select the maximum number of non-overlapping intervals.
    :param intervals: List of tuples (start_time, end_time)
    :return: List of selected intervals
    """
    # Step 1: Sort intervals based on finish time
    intervals.sort(key=lambda x: x[1])

    selected_intervals = []
    last_end_time = float('-inf')

    for start, end in intervals:
        if start >= last_end_time:  # Step 2: Select non-overlapping intervals
            selected_intervals.append((start, end))
            last_end_time = end  # Update the end time of the last selected interval

    return selected_intervals


# Example Usage:
intervals = [(1, 3), (2, 5), (4, 6), (6, 8), (5, 9), (7, 9)]
print(f"Selected Intervals: {interval_scheduling(intervals)}")
