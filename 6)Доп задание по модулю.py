import random
x = random.randint (3, 20)
print('Первое число:', x)
print('Пароль:', end=' ')
for o in range(1, x):
    for p in range(o + 1, x):
        if (o + p) <= x and x % (o+p) == 0:
            print(o, p, sep='', end='')