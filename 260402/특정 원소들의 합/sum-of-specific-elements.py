import sys
input = sys.stdin.readline

arr = []

for i in range(4):
    row = list(map(int, input().split()))
    arr.append(row)

x = 0

for i in range(4):
    for j in range(4):
        if j <= i:
            x += arr[i][j]

print(x)