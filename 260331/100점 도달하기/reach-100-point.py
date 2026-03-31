N = int(input())

for i in range (N, 101):
    if i>=90:
        print("A", end=" ")
    elif i>=80 and N<90:
        print("B", end=" ")
    elif i>=70 and N<80:
        print("C", end=" ")
    elif i>=60 and N<70:
        print("D", end=" ")
    else:
        print("F", end=" ")