def addNatural(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + addNatural(n - 1)
    
print(addNatural(6))