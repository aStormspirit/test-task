#1. Написать функцию, которая принимает на вход список целых чисел и возвращает новый список, содержащий только уникальные элементы из исходного списка.

def unique_list(input_list: list) -> list:
    unique_list = []
    for x in input_list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

#2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум) и возвращает список всех простых чисел в заданном диапазоне.
def prime_list(min_num: int, max_num: int) -> list:
    prime_list = []
    for num in range(min_num, max_num + 1):
        if num >= 2:
            for i in range(2, num // 2):
                if (num % i) == 0:
                    break
            else:
                prime_list.append(num)
    return prime_list


#3. Создать класс Point, который представляет собой точку в двумерном пространстве. Класс должен иметь методы для инициализации координат точки, вычисления расстояния до другой точки, а также для получения и изменения координат.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y


#4. Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.
def sort_strings(input_list: list) -> list:
    sorted_list = sorted(input_list, key=len)
    sorted_list.reverse()
    return sorted_list