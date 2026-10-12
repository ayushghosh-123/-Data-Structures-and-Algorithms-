def bubbleSort(a):
    n = len(a)
    for i  in range(n):
        for j in range(0, n-1-i):
            if(a[j] > a[j+1]):
                a[j],a[j+1] = a[j+1], a[j]

a = [1, 2, 4, 5, 3, 6]
bubbleSort(a)
print(a)