class Student:
    # name과 age 속성만 사용하도록 제한
    __slots__ = ["name", "age", "no"]

    def __init__(self):
        self.name = 'ABC'
        self.no = 1  # 속성을 만들 때 __로 시작하면 인스턴스를 속성에 직접 접근 불가
                        # 메서드를 이용해서 접근하여야 함

stu1 = Student()
stu1.name = 'A'
stu1.age = 35
# stu1.job = "Singer" 에러 발생.

print(stu1.name, stu1.age, stu1.no) # stu1.job 에러 발생