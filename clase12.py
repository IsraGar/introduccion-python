numbers = [1,2,3,4,5,6]
for i in numbers:
    if i == 3:
        continue
    print('Aquí i vale:', i)

for i in range(3,10):
    print(i)

fruits = ['manzana', 'pera', 'uva', 'naranja', 'mango']
for fruit in fruits:
    print(fruit)
    if fruit == 'naranja':
        print('\\\\naranja encontrada')

x = 0
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1