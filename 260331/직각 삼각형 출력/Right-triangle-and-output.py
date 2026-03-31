N = int(input())

for i in range(0, N+1):
    for j in range(i):
        if i%2==0:
            continue
        print("*", end="")
    print()