def confirm_rent(rent_list: list) -> bool:
    """
    :param rent_list: Список с часами аренды
    :return: Подтверждаем возможность аренды если нет пересечений по часам
    """
    rent_time = [0] * 24
    for renter in rent_list:
        time_rent = renter[0]
        while time_rent != renter[1]:
            # Увеличиваем производительность
            if rent_time[time_rent]:
                return False
            rent_time[time_rent] += 1
            time_rent += 1
    return not(any(hour > 1 for hour in rent_time))


def sort_list(list_to_sort: list) -> list:
    """
    :param list_to_sort: Массив который нужно отсортировать. Со значениями от 13 до 25
    :return: Отсортированный массив
    """
    start = 13
    finish = 26
    new_list_index = [0] * finish
    new_list = []
    for el in list_to_sort:
        new_list_index[el] += 1
    for i in range(start, finish):
        for el_times in range(new_list_index[i]):
            new_list.append(i)
    return new_list


def complexity_algo(arr):
    a = len(arr) - 1  # 2*O(1)
    out = list()  # O(1)
    while a > 0:  # O(1)
        out.append(arr[a])  # 2*O(1)
        a = a // 1.7  # O(1)
    out.merge_sort()  # O(n log n)

    # Общая сложность O(n log n)




