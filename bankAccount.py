class BankAccount:
    def __init__ (self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def desposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f'Se ha depositado {amount}. Saldo actual {self.balance}')
        else:
            print('No se puede depositar, cuenta inactiva')

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f'Se ha retirado {amount}. Saldo actual {self.balance}')
    
    def deactivate_account(self):
        self.is_active = False
        print('Cuenta desactivada')

    def activate_account(self):
        self.is_active = True
        print('Cuenta activada')

account_1 = BankAccount('Ana', 500)
account_2 = BankAccount('Luis', 1000)

#Llamada a los métodos
account_1.desposit(200)
account_2.desposit(100)
account_1.deactivate_account()
account_1.desposit(50)
account_1.activate_account()
account_1.desposit(600)