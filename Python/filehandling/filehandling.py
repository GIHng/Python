# import os
#
# # print(os.getcwd())
#
# try:
#     # file = open('./data.txt', 'w')
#     file = open('./data.txt', 'r')
#     for line in file:
#         print(line)
#
#     # content = file.read()  # 전체 읽기.
#     # print(content)
#     # file.write('문자열\n') # 문자열 기록
#     # lines = ["A", "B", "C"]
#     # file.writelines(lines)
#
# except Exception as e:
#     print("파일 처리 중 예외 발생")
# finally:
#     file.close()

# ------------------------------------------------------------------------

# 텍스트로 읽어서 split 같은 메서드를 이용

# import re
# data = []
#
# with open('./test.csv', 'r') as file:  # 현재 경로의 data.txt 파일을 읽음.
#     for line in file:
#         # ar = line.split(",")  # 각 행의 마지막 데이터에는 \n이 들어감.
#         ar = re.sub('\n', '', line).split(",")
#         data.append(ar)
# print(data)

# ------------------------------------------------------------------------

# 파이썬이 제공하는 csv 모듈을 이용하는 방법

import csv

data = []
with open('./test.csv', 'a') as file:  # 모드를 생략하면 읽기 모드가 default. 'w'는 삭제하고 다시 쓰기, 'a'는 추가.
    wr = csv.writer(file)
    wr.writerow(['AA', 'BB', 'CC'])  # io.UnsupportedOperation: not writable -> 쓰기 권한이 없음.
    wr.writerow(['DD', 'EE', 'FF'])


#     rdr = csv.reader(file)
#     for line in rdr:
#         data.append(line)
# print(data)
# help(csv.reader)