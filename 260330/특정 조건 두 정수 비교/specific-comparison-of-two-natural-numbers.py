inp = input()
arr = inp.split()
A = int(arr[0])
B = int(arr[1])

if A<B:
    print('1', end=" ")
else: 
    print('0', end=" ")

if A==B:
    print('1')
else:
    print('0')