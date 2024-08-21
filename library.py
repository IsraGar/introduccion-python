class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f'El libro {self.title} ha sido prestado')
        else:
            print(f'El libro {self.title} no está disponible')

    def return_book(self):
        self.available = True
        print(f'El libro {self.title} ha sido devuelto')

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f'El libro {book.title} no esta disponible')

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f'El libro {book.title} no está en tu lista de prestados')

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_books(self, book):
        self.books.append(book)
        print(f'El libro {book.title} ha sido agregado')

    def register_user(self, user):
        self.users.append(user)
        print(f'El usuario {user.name} ha sido registrado')

    def show_available_books(self):
        print(f'Libros disponibles:')
        for book in self.books:
            if book.available:
                print(f'{book.title} por {book.author}')

#Crear los libors
book_1 = Book('El principito', 'Antoine de Saint-Exupery')
book_2 = Book('1984', 'George Orwell')
book_3 = Book('El ángel número doce', 'OG Mandino')

#Crear usuario
user_1 = User('Isra', '001')
user_2 = User('Carli', '002')

#Crear la biblioteca
library = Library()
library.add_books(book_1)
library.add_books(book_2)
library.add_books(book_3)
library.register_user(user_1)
library.register_user(user_2)

#Mostrar libros
library.show_available_books()

#Realizar prestamo
user_1.borrow_book(book_1)

#Mostrar libros
library.show_available_books()

#Devolver libro
user_1.return_book(book_1)

#Mostrar libros
library.show_available_books()