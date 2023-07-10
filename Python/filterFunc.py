ar = ["123", "2123", '312312', '12', None]

def f1(x):
    return x != None

ar = list(filter(f1, ar)) # None을 제거한 후.

def f(x):
    return len(x) >= 3

result = list(filter(f, ar))

print(result)