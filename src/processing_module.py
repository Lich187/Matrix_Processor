import json

def calculate_row_products(matrix):
    result = []
    for row in matrix:
        # Важно: начинаем с 1, иначе умножение на 0 обнулит всё
        product = 1
        for num in row:
            # Умножаем текущее произведение на каждое следующее число в строке
            product *= num
        # Как только прошли всю строку, сохраняем итоговое произведение в вектор
        result.append(product)
    return result

def save_processed_to_json(vector_b, filename="matrix_data.json"):
    # Открываем файл для записи ("w"). Кодировка utf-8 нужна для корректной работы с текстом.
    with open(filename, "w", encoding="utf-8") as f:
        # Превращаем наши данные в формат JSON и записываем в файл.
        # В словаре сохраняем сам вектор и метку этапа (stage), чтобы понимать, что это результат.
        json.dump({"vector_b": vector_b, "stage": "processed"}, f)
    # Выводим сообщение в терминал для проверки, что файл успешно записался.
    print("Модуль обработки: Вектор B сохранен в JSON.")
