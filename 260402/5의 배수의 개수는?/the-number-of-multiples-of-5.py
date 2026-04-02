import sys
input = sys.stdin.readline

arr1 = []

for i in range(4):
    for j in range(4):
        row = list(map(int, input().split()))
        arr1.append(row)

cnt = 0

for i in range(4):
    for j in range(4):
        if arr1[i][j]%5==0:
            cnt += 1
print(cnt)