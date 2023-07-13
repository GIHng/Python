from operator import itemgetter

data = [
    ("hansj", 31, 111),
    ("kim", 32, 222),
    ("an", 34, 666),
    ("bang", 23, 444),
    ("jin", 3, 333),
]
for name in sorted(data, key=itemgetter(0)):
    print(name)