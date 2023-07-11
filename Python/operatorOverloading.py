class Student:
    def __init__(self, name="no_name"):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __eq__(self, other):
        return self.name == other.name  # id를 확인하지 않고 name만 같으면 같은 걸로.


stu1 = Student('A')  # 별도의 메모리 공간, id가 다름
stu2 = Student('A')  #
print(stu1 + stu2)

stu3 = stu1
print(stu1 == stu2)  # __eq__ 메서드를 호출함. name이 똑같은지 확인하는 것임.
print(stu1 is stu2)  # id를 불러냄. 다른 것.
