numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
notprime = []
for z in numbers:
    for x in range(2, z//2+1):           #Перебор делителей от 2 до половины числа включительно
        c=z%x
        if c == 0:                       #Деление списка на простые и не простые с помощью остатка от деления
            notprime.append(z)

            break
    else:
        prime.append(z)
print('not prime', notprime)
print('prime', prime)