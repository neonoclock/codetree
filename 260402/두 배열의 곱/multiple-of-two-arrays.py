import sys
input = sys.stdin.readline


arr1 = []

while len(arr1) < 3:
    row = list(map(int, input().split()))
    if row:
        arr1.append(row)

arr2 = []

while len(arr2) < 3:
    row = list(map(int, input().split()))
    if row:
        arr2.append(row)

for i in range(3):
    for j in range(3):
        print(arr1[i][j] * arr2[i][j], end = ' ')
    print()