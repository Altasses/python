# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

data = [int(i) for i in input('введите числа: ').split()]
k = 0
for i in range(1, len(data)):
    if data[i] > data[i -1]:
        k += 1
print(k)