n = 385916

# Введите ваше решение ниже
n1 = n % 10
n = n // 10
n2 = n % 10
n = n // 10
n3 = n % 10
res1 = n1+n2+n3

n4 = n % 10
n = n // 10
n5 = n % 10
n = n // 10
res2 = n4+n5+n

if res1 == res2:
    print('yes')
else:
    print('no')