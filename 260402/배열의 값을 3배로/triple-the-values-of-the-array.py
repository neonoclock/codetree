import sys 
input = sys.stdin.readline 

# Write your code here 
# A, B = map(int, input().split()) 
# print(A + B)


for i in range(3):
    arr = list(map(int, input().split()))
    for j in range(3):
        print(arr[j]*3, end=' ')
    print()
