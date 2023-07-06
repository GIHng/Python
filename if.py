# cnt = 0
# loop = 0
#
# for idx in range(1, 101):
#     loop += 1
#     if idx % 3 == 0:
#         loop += 1
#         if idx % 4 == 0:
#             cnt +=1
# print("12의 배수의 개수 :", cnt)
# print("조건 확인 개수 :", loop)

cnt = 0
loop = 0

for idx in range(1, 101):
    loop += 1
    if idx % 4 == 0:
        loop += 1
        if idx % 3 == 0:
            cnt +=1
print("12의 배수의 개수 :", cnt)
print("조건 확인 개수 :", loop)
