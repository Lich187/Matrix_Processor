# Импортируем функции из модуля обработки (для расчета вектора и сохранения в файл)
from processing_module import calculate_row_products, save_processed_to_json
# Импортируем функцию из модуля вывода (чтобы потом прочитать файл и показать результат)
from output_module import load_and_display

# Драйвер нужен для восходящей стратегии: он имитирует работу модуля ввода
test_matrix = [[1, 2, 3], [4, 5, 6]]
print("Драйвер: Передаем тестовую матрицу в модуль обработки...")

# Вызываем цепочку: обработка -> запись в JSON -> чтение и вывод
result = calculate_row_products(test_matrix)
save_processed_to_json(result)
load_and_display()
