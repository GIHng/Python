class Student:
    def __init__(self, name="no_name"):
        self.__name = name #속성 이름이 __로 시작하기 때문에 인스턴스로 접근이 안 된다.
    @property
    def getName(self):
        print("name의 getter 호출")
        return self.__name
    @getName.setter
    def setName(self, name):
        print("name의 setter 호출")
        self.__name = name

    # 프로퍼티를 생성
    name = property(fget= getName, fset= setName)
stu = Student()
stu.setName('abc')
print('stu', stu.getName())
stu.name = "DEF"  # fget와 fset이 호출된다. 속성을 바로 이용하는 것처럼 보인다.
print(stu.name)