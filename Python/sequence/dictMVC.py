# dict를 이용한 MVC

# DTO 역할을 수행하는 클래스 생성

class DTO:
    def __init__(self, name='noname', tel='전화없음'):
        self.name = name
        self.tel = tel


# 데이터 목록 출력
# datas = [DTO("A", "010"), DTO("B", "011")]

# for data in datas:
#     print(data.name, data.tel)  # BE에서 보내는 데이터의 형식이 바뀌어도 동일한 결과를 보여줘야 함.

datas = [{"name": "adam", "tel": "010"}, {"name": "jessica", "tel": "011"}]  # 데이터를 생성하는 부분.
for data in datas:
    for key in data:  # key 이름이 바뀌어도 받아오기 때문에 상관 없음.
        print(key, data[key])
