import json
from output_module import load_and_display


def test_load_and_display_success(tmp_path, capsys):
    # Создаём временный JSON-файл
    file = tmp_path / "test_data.json"
    file.write_text(json.dumps({"vector_b": [10, 20]}), encoding="utf-8")

    load_and_display(str(file))
    captured = capsys.readouterr()
    assert "Итоговый вектор B -> [10, 20]" in captured.out


def test_load_and_display_fail(capsys):
    # Проверяем обработку исключения (файла нет)
    load_and_display("nonexistent_file.json")
    captured = capsys.readouterr()
    assert "Ошибка! Файл с данными не найден" in captured.out
