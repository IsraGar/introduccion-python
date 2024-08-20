#Fibonacci

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
        
for number in fibonacci(15):
    print(number)