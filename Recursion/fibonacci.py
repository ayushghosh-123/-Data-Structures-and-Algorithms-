def Fibonnaci(n):
    if n == 1 or n == 2:
        return 1
    return Fibonnaci(n-2)+Fibonnaci(n-1)

print(Fibonnaci(7))