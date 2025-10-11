def find_streak(data, item):
    """
    Finds the longest streak of a given item in a list.

    Args:
        data: A list of items.
        item: The item to find the streak of.

    Returns:
        The length of the longest streak of the item.
    """
    max_streak = 0
    current_streak = 0
    for i in data:
        if i == item:
            current_streak += 1
        else:
            if current_streak > max_streak:
                max_streak = current_streak
            current_streak = 0
    if current_streak > max_streak:
        max_streak = current_streak
    return max_streak
