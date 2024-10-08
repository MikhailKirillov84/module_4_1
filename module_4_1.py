from fake_math import divide as f_d  #метод позволяет импортировать из модуля(fake_math) переменную(divide) и поменять(as) название этой переменной = (f_d)
from true_math import divide as t_d  #метод позволяет импортировать из модуля(true_math) переменную(divide) и поменять(as) название этой переменной = (t_d)

result1 = f_d(69, 3)  #переменная(result1) принимает функцию(f_d) с двумя параметрами, т.к. эта функция в модуле(fake_math) записана с 2-я параметрами(first, second)
result2 = f_d(3, 0)   #переменная(result2) ---""---
result3 = t_d(49, 7)  #переменная(result3) принимает функцию(t_d) с двумя параметрами, т.к. эта функция в модуле(true_math) записана с 2-я параметрами(first, second)
result4 = t_d(15, 0)  #переменная(result4) ---""---

print(result1)
print(result2)
print(result3)
print(result4)


