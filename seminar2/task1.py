# # # По данному целому неотрицательному n вычислите значение n! N! = 1*2**3* ... *N
# #  (произведение всех чисел от 1 до N) 0! =1
# input 5
# output 120

n = int(input('введите число: '))
count = 1
i = 0
while i != n:
    i += 1
    print(i)
    count *= i

print(count)
