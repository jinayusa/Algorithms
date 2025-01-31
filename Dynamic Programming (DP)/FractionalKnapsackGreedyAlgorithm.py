# Fractional Knapsack using Greedy Approach

# Time Complexity: O(n log n) (Sorting items by value/weight ratio)
# Space Complexity: O(1)

def fractional_knapsack(weights, values, capacity):
    """
    Function to compute the maximum value in Fractional Knapsack using a Greedy Algorithm.
    :param weights: List of item weights
    :param values: List of item values
    :param capacity: Maximum knapsack capacity
    :return: Maximum value that can be obtained
    """
    items = sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True)  # Sort by value/weight ratio
    max_value = 0

    for weight, value in items:
        if capacity >= weight:  # Take full item
            capacity -= weight
            max_value += value
        else:  # Take fraction of the item
            max_value += value * (capacity / weight)
            break

    return max_value


# Example Usage:
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print(f"Maximum value in Fractional Knapsack: {fractional_knapsack(weights, values, capacity)}")
