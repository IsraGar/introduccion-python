def greet(name, lastname = 'Sin apellido'):
    print('Hola', name, lastname)

greet('Isra', 'Garcia')
greet('Joss')
greet(lastname='Garcia', name='Isra')