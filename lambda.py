add = lambda a, b: a + b
print(add(10, 4))

mult = lambda a, b: a * b
print(mult(80, 5))

#Cuadrado de cada número
numbers = range(11)
squared_num = list(map(lambda x: x**2, numbers))
print('Cuadrados:', squared_num)

#Pares
even_num = list(filter(lambda x: x%2 == 0, numbers))
print('Pares:', even_num)