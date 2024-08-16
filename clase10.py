numbers = {1: 'uno', 2: 'dos', 3: 'tres'}
print(numbers[2])
information = {
    'nombre': 'Isra',
    'apellido': 'Garcia',
    'altura': 1.71,
    'edad': 28
}
print(information)
del information['edad']
print(information)
claves = information.keys()
print(claves)
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {
    'Isra' : {'nombre': 'Isra',
    'apellido': 'Garcia',
    'altura': 1.71,
    'edad': 28},
    'Marce' : {'nombre': 'Marce',
    'apellido': 'Hernandez',
    'altura': 1.60,
    'edad': 28},
    'Joce' : {'nombre': 'Joce',
    'apellido': 'Carmona',
    'altura': 1.50,
    'edad': 27}
}
print(contacts)
print(contacts['Joce'])