from array import *

val = array('i', [1,3,5,6,7])

# print array element 
for i in val:
    print(i, end=' ')

print('\n')
# type of array 
print(val.typecode)


# val.reverse()
# for i in val:
#     print(i, end=' ')

for i in val[::-1]:
    print(i, end= ' ')

print('\n')
# clone 
newarray = array('i', (x for x in val))
for i in val[::-1]:
    print(i, end= ' ')

print('\n')

# n number of input 
val2 = array('i', [])
n = int(input('size of array: '))

for i in range (0,n):
    val2.append(int(input('enter the input: ')))

for i in val2[::-1]:
    print(i, end= ' ')