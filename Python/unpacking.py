def collect(a, b):
    print(a, end=" ")
    print(b)


collect(10, 20)
collect(*[100, 200])
collect(*{'key1': 100, "key2":200})
collect(**{"a": 100, "b": 200})

