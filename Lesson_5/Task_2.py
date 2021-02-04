from collections import deque
keys = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def func(a):
    if a == 'A' or a == 'B' or a == 'C' or a == 'D' or a == 'E' or a == 'F':
        return keys[a]
    else:
        return int(a)


def say(y):
    if y == 0:
        return 'первое'
    else:
        return 'второе'


result = 0
for _number in range(0, 2):
    number = input(f'Введите {say(_number)} число: ')
    _num16 = deque(f'{number}')
    num16 = ''
    for i in _num16:
        num16 = f'{i}{num16}'
    num = 0
    for x in range(0, len(num16)):
        num = num + (func(num16[x]) * (16 ** x))
    result = result + num
print(result)