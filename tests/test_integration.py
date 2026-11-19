import os
import json
from main import main


def test_full_integration():
    # Запускаем главную функцию (она связывает все модули)
    main()

    # Проверяем, что файл с результатами создался
    assert os.path.exists("matrix_data.json")

    # Открываем файл и проверяем, что программа посчитала всё верно
    with open("matrix_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Ожидаемый результат для матрицы [[2, 2, 2], [1, 2, 3], [5, 2, 1]]
    assert data["vector_b"] == [8, 6, 10]
