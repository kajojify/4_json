import json


def load_data(filepath):
    """Декодирует json-данные в Python-объект. Возвращает список,
    элементами которого являются словари(dicts), предоставляющие 
    информацию об алкогольных магазинах Москвы."""

    with open(filepath) as f:
        return json.load(f)


def pretty_print_json(data):
    """Сериализует data в json-формат.
    Выводит в консоль содержимое файла filepath в удобочитаемом
    формате с отступом в 4 пробела."""

    print(json.dumps(data, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    filepath = input("Введите путь к файлу json --- ")
    try:
        alcohol_data = load_data(filepath)
    except FileNotFoundError:
        print("Нет такого файла или директории! Завершение программы.")
        exit()
    pretty_print_json(alcohol_data)
