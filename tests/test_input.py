from input_module import get_input_matrix


def test_get_input_matrix():
    matrix = get_input_matrix()
    assert isinstance(matrix, list)
    assert len(matrix) == 3
