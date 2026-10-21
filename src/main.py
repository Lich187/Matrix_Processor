# Импортируем библиотеку json для чтения данных из промежуточного файла
import json

# Импортируем функции из наших модулей:
# - модуль ввода (генерирует матрицу и сохраняет её)
# - модуль обработки (считает вектор B и сохраняет результат)
# - модуль вывода (читает результат и показывает на экране)
from input_module import get_input_matrix, save_input_to_json
from processing_module import calculate_row_products, save_processed_to_json
from output_module import load_and_display

def main():
    print("=== ЗАПУСК (Ветка master) ===")
    # Имя файла-посредника, через который модули будут общаться
    filename = "matrix_data.json"

    # --- ЭТАП 1: ВВОД ---
    # Вызываем модуль ввода. Он создает матрицу и сохраняет её в JSON-файл
    matrix = get_input_matrix()
    save_input_to_json(matrix, filename)

    # --- ЭТАП 2: ОБРАБОТКА ---
    # Открываем файл, который только что создал модуль ввода, и читаем его
    with open(filename, "r", encoding="utf-8") as f:
        # Загружаем данные из файла в переменную data (получаем словарь Python)
        data = json.load(f)

    # Достаем матрицу по ключу "matrix" и передаем в функцию обработки. Получаем вектор B.
    processed = calculate_row_products(data["matrix"])
    # Сохраняем полученный вектор обратно в файл для следующего модуля
    save_processed_to_json(processed, filename)

    # --- ЭТАП 3: ВЫВОД ---
    # Вызываем модуль вывода. Он прочитает итоговый файл и покажет вектор на экране
    load_and_display(filename)

    print("=== ИНТЕГРАЦИЯ ЗАВЕРШЕНА ===")

# Эта проверка нужна, чтобы функция main() запускалась только при прямом запуске файла
if __name__ == "__main__":
    main()
