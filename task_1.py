"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
наименования предприятий, чья прибыль ниже среднего.
"""
from collections import deque, defaultdict

number_of_companies = int(input('Введите количество предприятий: '))
number_of_companies_buffer = number_of_companies
middle = 0
company_keys = deque()

while number_of_companies > 0:
    company_temp = input('Введите название компании: ')
    company_keys.append(company_temp)
    number_of_companies -= 1


grossbuh = dict.fromkeys(company_keys)
grossbuh_summ = dict.fromkeys(company_keys)

for i in company_keys:
    first = int(input(f'Введите прибыль компании {i} за первый квартал: '))
    second = int(input(f'Введите прибыль компании {i} за второй квартал: '))
    three = int(input(f'Введите прибыль компании {i} за третий квартал: '))
    four = int(input(f'Введите прибыль компании {i} за четвертый квартал: '))
    grossbuh[i] = [first, second, three, four]

for key in grossbuh.keys():
    grossbuh_summ[key] = sum(grossbuh[key])

for key in grossbuh_summ.keys():
    middle = middle + grossbuh_summ[key] / number_of_companies_buffer

above = deque()
below = deque()

for key in grossbuh_summ.keys():
    if grossbuh_summ[key] >= middle:
        above.append(key)
    else:
        below.append(key)

print(f'Прибыль {list(above)} больше средней, а {list(below)} меньше средней')
