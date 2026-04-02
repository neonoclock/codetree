import sys
input = sys.stdin.readline

arr1 = []

for i in range(3):
    row = list(map(int, input().split()))
    arr1.append(row)

arr2 = []

for i in range(3):
    row = list(map(int, input().split()))
    arr2.append(row)

for i in range(3):
    for j in range(3):
        print(arr1[i][j] * arr2[i][j], end = ' ')
    print()