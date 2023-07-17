# import re
# from collections import Counter
# data = []
# count = 0
# ipCounter = dict()
# traffic = dict()
# result = 0
# counter = Counter()
# with open('./log.txt', 'r', encoding='UTF-8') as file:
#     for line in file:
#         ar = line.split()
#         data.append(ar)
#         if ar[8] == '200':
#             # print('횟수 : ', count + 1, '\t', ar)
#             count += 1
#         try:
#             ipCounter[ar[0]] = ipCounter.get(ar[0],0)
#             result += int(ar[9])
#         except Exception as e:
#             pass
#         counter[ar[0]] += 1
#
# print('성공 코드 개수는 : ', count)
# print(result)
#         # 읽어 낸 함수를 공백을 기준으로 분할해서 list로 생성
# print(dict(counter))

import re
from collections import Counter

data = []
count = 0
ipCounter = dict()
traffic = dict()
result = 0
counter = Counter()
with open('./log.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        ar = line.split()
        data.append(ar)
        if ar[8] == '200':
            # print('횟수 : ', count + 1, '\t', ar)
            count += 1
        try:
            ipCounter[ar[0]] = ipCounter.get(ar[0], 0)
            result += int(ar[9])
        except Exception as e:
            pass
        counter[ar[0]] += 1
print('성공 코드 개수는 : ', count)
print(result)
# 읽어 낸 함수를 공백을 기준으로 분할해서 list로 생성
print(dict(counter))
