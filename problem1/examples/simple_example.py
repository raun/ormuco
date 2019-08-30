from src import is_overlap


def test_is_overlap():
    result = is_overlap(1, 5, 2, 6)
    assert result is True
