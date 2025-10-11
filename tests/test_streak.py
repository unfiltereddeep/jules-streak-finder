from streak_finder.streak import find_streak

def test_empty_list():
    assert find_streak([], "a") == 0

def test_no_streaks():
    assert find_streak(["a", "b", "c"], "d") == 0

def test_single_streak():
    assert find_streak(["a", "a", "b", "c"], "a") == 2

def test_multiple_streaks():
    assert find_streak(["a", "a", "b", "a", "a", "a"], "a") == 3

def test_streak_at_beginning():
    assert find_streak(["a", "a", "a", "b", "c"], "a") == 3

def test_streak_at_end():
    assert find_streak(["b", "c", "a", "a", "a"], "a") == 3

def test_no_item_in_list():
    assert find_streak(["b", "c", "d"], "a") == 0
