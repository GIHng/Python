key = ['A', 'B', 'C']
value = ['D', 'E', 'F']

print(list(zip(key, value))) # 데이터 모임의 개수가 같아야 함.
print(dict(zip(key, value)))

# [('A', 'D'), ('B', 'E'), ('C', 'F')]
# {'A': 'D', 'B': 'E', 'C': 'F'}