class Vehicle:
    def __init__(self, brand, model, price):
        #Encapsulamiento
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
    
    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f'El vehículo {self.brand} ha sido vendido')
        else:
            print(f'El vehículo {self.brand} no esta disponible')
    
    #Abstracción
    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

#Herencia
class Car(Vehicle):
    #Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f'El motor del auto {self.brand} esta en marcha'
        else:
            return f'El auto {self.brand} no esta disponible'
    
    def stop_engine(self):
        if self.is_available:
            return f'El motor del auto {self.brand} se ha detenido'
        else:
            return f'El auto {self.brand} no esta disponible'

class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f'La bicicleta {self.brand} esta en marcha'
        else:
            return f'La bicicleta {self.brand} no esta disponible'
    
    def stop_engine(self):
        if self.is_available:
            return f'La bicicleta {self.brand} se ha detenido'
        else:
            return f'La bicicleta {self.brand} no esta disponible'

class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f'El motor del camión {self.brand} esta en marcha'
        else:
            return f'El camión {self.brand} no esta disponible'
    
    def stop_engine(self):
        if self.is_available:
            return f'El camión {self.brand} se ha detenido'
        else:
            return f'El camión {self.brand} no esta disponible'
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f'Lo siento, el vehículo {vehicle.brand} no esta disponible')
    
    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availability = "disponible"
        else:
            availability = "no disponible"
        
        print(f'El auto {vehicle.brand} tiene estatus {availability} y cuesta {vehicle.get_price()}')
    
class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f'El {vehicle.brand} ha sido agregado al inventario')

    def register_customer(self, cusotmer: Customer):
        self.customers.append(cusotmer)
        print(f'El cliente {cusotmer.name} ha sido registrado correctamente')
    
    def show_available_vehicles(self):
        print('***Autos disponibles en la tienda***')
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f'--Vehiculo: {vehicle.brand} | Precio: {vehicle.get_price()}')

car1 = Car('Toyota', 'Corolla', 20000)
bike1 = Bike('Yamaha', 'MT-07', 7000)
truck1 = Truck('Kenworth', 'T-680', 50000)

customer1 = Customer('Isra')

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)
dealership.register_customer(customer1)

#Autos disponibles
dealership.show_available_vehicles()

#Cliente
customer1.inquire_vehicle(car1)
customer1.buy_vehicle(car1)

#Autos disponibles
dealership.show_available_vehicles()