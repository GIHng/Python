class DTO:
    def __init__(self, num=0, name='이름 없음'):
        self.__num = num  # 클래스 내에선 사용 가능, 인스턴스에서 접근 불가
        self.__name = name

    @property
    def num(self):
        return self.__num

    def name(self):
        return self.__name

    def setternum(self, num):
        self.__num = num

    def settername(self, name):
        self.__name = name

    # 인스턴스를 print 함수에 대입했을 때 호출되는 메서드 - 오버라이딩

    # 출력을 편하게 하기 위해서 재정의 - 디버깅 목적
    def __str__(self):
        return str(self.__num) + ":" + self.__name


dto1 = DTO(1, 'A')
dto2 = DTO(2, 'B')

data = [dto1, dto2]

import pickle
try:
    with open("./data.dat", "rb") as f:
        # f의 데이터를 serializable
        # pickle.dump(data, f)  # 읽어낼 수 없음. 모드는 'wb'
        result = pickle.load(f)  # encoding 방식 지정하지 않음, 모드는 'rb'
        for dto in result:
            print(dto)
except Exception as e:
    print(e)
