from random import randint

a = [randint(1,10) for i in range(5)]
b = [randint(1,10) for i in range(5)]
print(f"{a} первый список")

print(f"{b} второй список")

cpis1 = a+b
print(f"{cpis1} Два списка в одном")

cpis2 = sorted(set(cpis1), key=cpis1.index)
print(f"{cpis2} Два списка в одном без повторений")

cpis3 = [a[i] for i in range(len(a)) if a[i] in b]
print(f"{cpis3} Общие элементы двух списков")

cpis4 = sorted(list(set(a)) + list(set(b)), key=cpis1.index)
print(f"{cpis4} Уникальные элем с двух списков")

cpis5 = [min(cpis1), max(cpis1)]
print(f"{cpis5} Минимальное и максимальное значение списков")