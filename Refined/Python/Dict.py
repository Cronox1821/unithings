empty_dict = dict()
default_dict = {
    'name': 'John',
    'surname': 'Doe',
    'age': 31,
    'id': 1,
    'salary': 2000,
    'sector': 3
}

identifier = 'temp'
nest_dict = {identifier: default_dict}

for item, value in nest_dict.items():
    print(f'identifier:{item}')

    for j in value:
        print(f'{j.capitalize():9}:{value[j]}')

print('-'*100)
from tabulate import tabulate
table = nest_dict.get(identifier)

table_data = [[key.capitalize(),table[key]] for key in table.keys()] 
print(key for key in table.keys())
print(table_data)
print(table)
print(tabulate(table_data,headers=['Key','Value'],tablefmt='grid'))
