# Activity Selection using Greedy Algorithm

# Time Complexity: O(n log n) (Sorting)
# Space Complexity: O(1)

def activity_selection(activities):
    """
    Function to select the maximum number of activities that don't overlap.
    :param activities: List of tuples (start_time, end_time)
    :return: List of selected activities
    """
    # Step 1: Sort activities based on finish time
    activities.sort(key=lambda x: x[1])

    selected_activities = []
    last_end_time = 0

    for start, end in activities:
        if start >= last_end_time:  # Step 2: Select non-overlapping activities
            selected_activities.append((start, end))
            last_end_time = end  # Update the end time of the last selected activity

    return selected_activities


# Example Usage:
activities = [(1, 3), (2, 5), (4, 6), (6, 8), (5, 9), (7, 9)]
print(f"Selected Activities: {activity_selection(activities)}")
