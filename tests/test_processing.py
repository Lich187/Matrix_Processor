from processing_module import calculate_row_products, is_valid_matrix

# Тест 1: Расчёт вектора


def test_calculate_row_products():
    assert calculate_row_products([[1, 2, 3], [4, 5, 6]]) == [6, 120]

# Комбинаторное покрытие условий (проверяем 4 комбинации True/False)

# Комбинация 1: Список + Не пустой + Вложенные списки (True, True, True)


def test_is_valid_matrix_TTT():
    assert is_valid_matrix([[1, 2], [3, 4]]) is True

# Комбинация 2: Не список (False)


def test_is_valid_matrix_F():
    assert is_valid_matrix("not a list") is False

# Комбинация 3: Список + Пустой (True, False)


def test_is_valid_matrix_TF():
    assert is_valid_matrix([]) is False

# Комбинация 4: Список + Не пустой + Элементы не списки (True, True, False)


def test_is_valid_matrix_TTF():
    assert is_valid_matrix([1, 2, 3]) is False
