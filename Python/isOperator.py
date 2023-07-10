class Student:
    class_data = '클래스의 속성'


# 인스턴스 생성해서 대입
stu1 = Student()

# 인스턴스 생성해서 대입
stu2 = Student()

# stu1의 데이터를 대입 : stu1이 참조하고 있는 데이터의 참조를 stu3가 참조한다.
stu3 = stu1

# 2개의 인스턴스가 동일한지 여부를 확인
print(stu1 == stu3)  # 내부의 데이터가 같은지 확인
print(stu1 is stu3)  # id가 같은지 확인.

# stu1과 stu2는 다른 메모리 영역을 할당받음