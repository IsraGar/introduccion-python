#Concesionario
#Compra y venta de autos
#Mostrar disponibles y precios

class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price
        self.is_available = True
    
    def active_car(self):
        self.is_available = True
        print(f'El auto {self.model} ahora esta disponible para venta')
    
    def deactive_car(self):
        self.is_available = False
        print(f'El auto {self.model} ya no esta disponible para venta')

class Customer:
    def __init__(self, name):
        self.name = name

    def buy_car(self, car):
        if car.is_available:
            print(f'El cliente {self.name} ha comprado el auto {car.model}')
            car.deactive_car()
        else:
            print(f'El auto {car.model} no esta disponible para venta')
    
    def sell_car(self, car):        
        print(f'El cliente {self.name} nos ha vendido el auto {car.model}')
        car.active_car()

class CarAgency:
    def __init__(self):
        self.cars = []
        self.users = []
    
    def add_cars(self, car):
        self.cars.append(car)
        print(f'El auto {car.model} ha sido agregado')

    def register_user(self, user):
        self.users.append(user)
        print(f'El usuario {user.name} ha sido registrado')

    def show_available_cars(self):
        print(f'***Autos disponibles***')
        for car in self.cars:
            if car.is_available:
                print(f'Auto: {car.model} | Precio: ${car.price}')

#Crear los autos
car_1 = Car('Mustang', 1000)
car_2 = Car('Camaro', 1200)
car_3 = Car('Jeep', 1500)

#Crear usuario
user_1 = Customer('Isra')
user_2 = Customer('Carli')

#Crear agencia
car_agency = CarAgency()
car_agency.add_cars(car_1)
car_agency.add_cars(car_2)
car_agency.add_cars(car_3)
car_agency.register_user(user_1)
car_agency.register_user(user_2)

car_agency.show_available_cars()

user_1.buy_car(car_1)
car_agency.show_available_cars()

user_1.buy_car(car_1)
car_agency.show_available_cars()

user_1.sell_car(car_1)
car_agency.show_available_cars()