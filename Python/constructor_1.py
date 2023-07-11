class Student:
    auto_increment = 0

    def __init__(self):
        Student.auto_increment += 1
        self.no = Student.auto_increment

    def __del__(self):
        print('인스턴스 소멸')

    @staticmethod
    def method():
        print('매개변수가 없는 static method')



Student.method()  # 인스턴스를 만들 필요가 없음.
stu1 = Student()
print(stu1.no)
stu2 = Student()
stu3 = stu2  # 다른 변수에 참조를 대입하므로 참조 카운트는 1 증가 -> 2
stu2 = None  # 참조 카운트가 1 줄어들어도 -> 1, 인스턴스가 소멸되지 않는다.
print(stu3.no)

stu1 = None  # None이 들어가면 Reference Count가 1 감소한다. -> Reference Count가 0이 되면 인스턴스 소멸

print('프로그램 종료') # 프로그램 종료 이후 인스턴스가 소멸된다.