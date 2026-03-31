arr = list(map(int, input().split()))

cnt3 = 0
cnt5 = 0

for i in arr:
    if i % 3 ==0:
        cnt3 += 1
    if i % 5 ==0:
        cnt5 += 1

print(cnt3, cnt5)