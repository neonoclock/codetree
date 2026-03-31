arr = ["apple", "banana", "grape", "blueberry", "orange"]
ch = input()

cnt = 0

for word in arr:
    if word[2] == ch or word[3] ==ch:
        print(word)
        cnt += 1

print(cnt)