#Números pares e impares

def pares(limit):
    a = 0
    while a < limit + 1:
        yield a
        a += 2

def impares(limit):
    a = 1
    while a < limit + 1:
        yield a
        a += 2
print('''Números pares''')        
for number in pares(5):
    print(number)

print('''Números impares''')  
for number in impares(5):
    print(number)