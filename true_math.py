
from math import inf          # Метод позволяет импортировать из встроенной библиотеки math (from math import inf) бесконечность(inf)
def divide(first, second):    # Создаем функцию(divide) с 2-я параметрами(first, second)
    if second == 0:           # Функция должна возвращать(return) результат деления(/) first на second,
        return inf            # но когда в second записан 0 - возвращать бесконечность.
    else:
        return first / second

# result3 = divide(49, 7)
# result4 = divide(15, 0)
# print(result3)
# print(result4)


