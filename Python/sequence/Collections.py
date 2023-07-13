from collections import Counter

data = ["한식", "중식", "분식", "한식", "일식", "양식", "한식", "분식"]

counter = Counter(data)
print(counter)
print(dict(counter))

for data in counter:
    print(data, end='\t')
print()

print(counter.most_common(2))

# tuple의 목록
data = [("APPLE", 3), ("APPLE", 2),("ORANGE", 3), ("MANGO", 3), ("ORANGE", 5)]
counter = Counter()

# 데이터가 등장한 횟수 구하기
for name, count in data:
    counter[name] += 1
print('데이터가 등장한 횟수 구하기', dict(counter))

# 데이터의 합계를 구해보기
for name, count in data:
    counter[name] += count
print('데이터의 합계를 구해보기', dict(counter))



