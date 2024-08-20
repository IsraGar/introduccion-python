#Crear un iterador para los números impares
#Limíte
limit = 10

#Creando iterador
odd_iter = iter(range(1, limit+1,2))

#Usando iterador
for num in odd_iter:
    print(num)