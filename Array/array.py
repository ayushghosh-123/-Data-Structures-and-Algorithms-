# import array as arr
from array import *

# make an array
val = array('d',[1,2,3,4,5,6,9,9.5])
# val = array('u',['a', 'b', 'c'])

# for print an array 
# for i in range (0,len(val)):
#     print(val[i], end=' ')

# print('\n')

# for x in val:
#     print(x, end=',')

# print('\n')

# print(val.typecode)

# reverse any array 
# val.reverse()
# for i in range (0,len(val)):
#     print(val[i], end=' ')

# insert at any position 
val.insert(0, 50)
# for i in range (0,len(val)):
#     print(val[i], end=' ')

# INSERT A ELEMT IN LAST
val.append(10)

#  update or over write
val[2] = 100

# clone an oldarray to new one
Arraynewone = array(val.typecode, (x for x in val))


# delete any elememnt in array
# Arraynewone.pop(3)
Arraynewone.remove(4)

# for i in range (0,len(Arraynewone)):
#     print(Arraynewone[i], end=' ')

# SLICING ARRAY
abc = val[2:5]

# for reversing al of this 
x = val [::-1]

# for i in range (0,len(abc)):
#     print(abc[i], end=' ')

# user based input the n number size of array
# arr = array('i', [])
# n = int(input('enter the number: '  ))

# for i in range (0,n):
#     arr.append(int(input('Enter next Input: ')))

# for x  in arr:
#     print(x, end=' ')


#searching the array element in the araayList
arr = array('i', [12, 23, 45, 234, 134, 235])
i = arr.index(134)
print("print the index: ", i)

