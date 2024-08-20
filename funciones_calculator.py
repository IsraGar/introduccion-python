def add(a, b):
    return a + b

def subs(a , b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def calculator():
    while True:
        print('Seleccione una operación')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicación')
        print('4. División')
        print('5. Salir')
        option = int(input('Ingresa tu opción {1,2,3,4,5}'))
        if option == 5:
            print('Saliste de la calculadora')
            break
        if option in [1, 2, 3, 4]:
            num1 = float(input('Ingrese el primer número'))
            num2 = float(input('Ingrese el segundo número'))

            if option == 1:
                print('La suma es:', add(num1, num2))
            elif option == 2:
                print('La resta es:', subs(num1, num2))
            elif option == 3:
                print('La multiplicación es:', mult(num1, num2))
            elif option == 4:
                print('La división es:', div(num1, num2))
            else:
                print('Opción no válida')


calculator()