# Activity Selection using Recursion

# Time Complexity: O(n log n) (Sorting)
# Space Complexity: O(n) (Recursion stack)

def activity_selection_recursive(activities, n, prev_end=0, index=0):
    """
    Recursive function to select the maximum number of activities.
    :param activities: List of (start_time, end_time)
    :param n: Number of activities
    :param prev_end: End time of previously selected activity
    :param index: Current index in the activities list
    :return: List of selected activities
    """
    if index >= n:
        return []

    # Select the current activity if it doesn't overlap
    if activities[index][0] >= prev_end:
        return [(activities[index][0], activities[index][1])] + activity_selection_recursive(
            activities, n, activities[index][1], index + 1)

    # Skip this activity and move to the next one
    return activity_selection_recursive(activities, n, prev_end, index + 1)


# Example Usage:
activities = [(1, 3), (2, 5), (4, 6), (6, 8), (5, 9), (7, 9)]
activities.sort(key=lambda x: x[1])  # Sort activities before passing
print(f"Selected Activities (Recursive): {activity_selection_recursive(activities, len(activities))}")
