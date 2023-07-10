class Student:
    # 인스턴스가 있어야만 호출되는 메서드

    def disp(self):
        print("인스턴스 생성")

    def setName(self, name):
        self.name = name  # self.name은 인스턴스의 속성으로 만들어진다. 그냥 name만 쓰면 지역변수가 된다.


# 인스턴스 생성
student = Student()  # Student()가 인스턴스임. student는 이름을 사용하기 위함.
student.setName('ABC')
print('student.name =', student.name)  # self가 있기 때문에 출력할 수 있음.

student.score = 100  # 파이썬은 객체의 속성을 동적으로 만들 수 있음.
print('student.score =', student.score)

# 메서드 호출 - bound 호출
student.disp()  # 인스턴스 생성
Student().disp()  # 인스턴스 생성

# 메서드 호출 - Unbound 호출
Student.disp(student)  # Student()가 들어가도 상관 없음. # 인스턴스 생성
