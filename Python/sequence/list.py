# list의 메서드 활용
import random

li1 = ["A", "B", "C", "D"]
li2 = list(range(10))

# 데이터 추가
li1.append('E')
print('마지막 항목 :',li1[-1])

# slicing
print('slicing :', li1[0:2])

# 리스트 항목 삭제
del li1[-1]
print('삭제 후 마지막 항목 :', li1[-1])

# 리스트 데이터 순회
# for data in li1:
#     print(data)

# 리스트 sort
li1.sort(reverse=True)
print('정렬 후 :', li1)

li1.sort(key = str.lower)
print('정렬 후 :', li1)