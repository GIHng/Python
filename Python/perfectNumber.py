sum = 0
cnt = 0

for i in range(2, 1001):
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            sum += j
    if sum == i:
        cnt +=1
    sum = 1

print(cnt)