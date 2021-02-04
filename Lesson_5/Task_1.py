from collections import deque
number_company = int(input('Кол-во компаний: '))
middle = 0
names = {}
middle_comps = {}
small = deque()
big = deque()
for i in range(number_company):
    name = input('Название компании: ')
    names[i+1] = name
    crt1 = int(input('Первый квартал: '))
    crt2 = int(input('Второй квартал: '))
    crt3 = int(input('Третий квартал: '))
    crt4 = int(input('Четвертый квартал: '))
    if number_company > 1:
        print('-' * 20)
    middle_comp = (crt1 + crt2 + crt3 + crt4) / 4
    middle_comps[i+1] = middle_comp
    middle = middle + middle_comp
middle = middle / number_company
print('-' * 40)
print(f'Средняя прибыль компаний: {middle}')
for num in range(number_company):
    if middle_comps[num+1] < middle:
        small.append(names[num+1])
    else:
        big.append(names[num + 1])
print('Убыточные компании:')
for i in range(len(small)):
    print(small[i])
print('-' * 20)
print('Успешные компании:')
for i in range(len(big)):
    print(big[i])






