# 2차원 배열 대신에 dict 사용

kia = ["윤영철", "최형우", "이의리"]
lg = ["켈리", "플럿코"]
hanhwa = ["노시환"]

kbo = [{"team":"기아", "data":kia}, {"team":"엘지", "data":lg}, {"team":"한화", "data":hanhwa}]
# 데이터에 대한 설명을 같이 넣어줘야 한다. (위의 경우엔 팀 이름.)

for dic in kbo:
    print(dic.get("team"), end='\t')
    for player in dic.get("data"):
        print(player, end='\t')
    print()



#
# li3 = [li1, li2]  # 배열로 추가하면 이들을 구분할 수 있는 이름을 넣을 수 없음.
# # list는 index를 이용해서 접근하고 dict는 key를 이용해서 접근
#
# for idx, b in enumerate(li3):  # enumerate는 index와 데이터를 튜플로 리턴함.
#     if idx == 0:
#         print("li1", end="\t")
#     else:
#         print("li2", end="\t")
#
#     for player in b:
#         print(player, end='\t')
#     print()