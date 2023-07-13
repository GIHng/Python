import queue


def power(param):
    return param ** 2

li = list(range(10))  # 0부터 9까지의 숫자를 가지고 list를 생성
#li의 모든 데이터를 제곱한 ㅣist를 생성
result = list(map(power, li))
print(result)

result = []
for i in range(len(li)):
    result.append(li[i] ** 2)
print(result)


# list comprehension
# [ 연산식 순회할 문장 ]
result = [i*i for i in li]
print(result)

li1 = [1, 2, 3]
li2 = [4, 5, 6, 7]
result = [ x * y for x in li1 for y in li2]
print(result)



# for 와 if 사용 가능 - filtering
singers = ['Abc', 'Bdef', 'Cs', 'Daf']

result = list(filter(lambda x : len(x) >= 3, singers))
print(result)
result = [x for x in singers if len(x) >= 3]
print(result)

result = [x for x in singers if len(x) >= 3 and len(x) < 4]
print(result)

result = [x if len(x) >= 3 else x + '_' for x in singers ]
print(result)

help(queue.Queue)