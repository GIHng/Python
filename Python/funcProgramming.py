li = [i for i in range(5)]  # 0부터 4까지 리스트를 생성.

temp = []

for x in li:
    temp.append(x * x)

print(temp)


def f(x):
    return x * x


temp = list(map(f, li))  c
print(temp)  # map 이용한 변환.

temp = list(map(lambda x : x*x, li))  # 처리할 내용이 한 줄 이므로 lambda로 처리함.
