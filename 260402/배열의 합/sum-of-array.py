import sys
input = sys.stdin.readline

arr = []

for i in range(4):
    row = list(map(int, input().split()))
    arr.append(row)
    
for i in range(4):
    print(sum(arr[i]))
