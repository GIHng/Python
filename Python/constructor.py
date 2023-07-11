# 클래스 생성
class Student:

    # 이 메서드에서 속성을 생성해서 속성을 처음부터 소유하도록 만들어주는 것이 좋다.
    # 매개변수를 이용해서 초기화하면 만들어질 때 다양한 값으로 초기화가 가능
    # 매개변수를 이용해서 초기화 할 때, 매개변수에 기본값을 설정하지 않으면
    # 인스턴스를 생성할 때 반드시 매개변수에 값을 대입해야 한다.

    def __init__(self, name="no_name"):
        print("인스턴스 생성")
        self.name = name
        # 클래스에 만들어졌지만 인스턴스 없이는 호출할 수 없다.
        # 특정한 실수로 생성하고자 하는 경우는 생성자 내부에서 직접 설정


    def disp(self):
        print('인스턴스 생성')
    def setName(self, name):
        self.name = name  # name이란 속성이 없으면 만들고, 존재하면 수정.

    def getName(self):
        return self.name

stu1 = Student()  # 생성자를 통해 인스턴스의 속성을 지정할 수 있음.
Student.disp(stu1)  # 클래스가 인스턴스 메서드를 호출함. (unbound 호출)
stu1.disp()  # self에 인스턴스가 대입되서 메서드를 호출한다. (bound 호출)
print()
stu1.setName('ABC')  # set, get이 순서가 바뀌면 안 됨. 인스턴스를 만들 때 name을 만들 수 있음.
print(f'stu1.Name : {stu1.getName()}')
