def personal_sum(numbers):
    results = 0
    incorrect_data = 0
    for i in numbers:
        try:
            results += i
        except TypeError as exc:
            print(f'Некорректный тип данных - <{i}>')
            incorrect_data += 1
        _tuple = (results, incorrect_data)
    return _tuple

def calculate_average(numbers):
    try:
        _tuple = personal_sum(numbers)
        return _tuple[0]/(len(numbers)-_tuple[1])
    except ZeroDivisionError:
        return 0
    except TypeError as exp:
        print('В numbers записан некорректный тип данных')
        return


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
