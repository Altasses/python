# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# Найдите количество и выведите его.
# list_1 = [1, 2, 3, 4, 5]
# k = 3

data = [int(i) for i in input('введите случайный ряд чисел: ').split()]
print(data)
k = int(input('какое число посчитать? '))
count = data.count(k)
print(count)

# count = 0
# for i in range(len(list_1)):
#     if list_1[i] == k:
#         count += 1
# print(count)