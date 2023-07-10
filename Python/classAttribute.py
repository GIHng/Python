def disp():
    print('인스턴스 생성')


class Student:
    class_data = '클래스의 속성'

    # 인스턴스가 있어야만 호출되는 메서드


student = Student()
print(Student.class_data)  # 클래스 이름을 이용해서 클래스 속성에 접근
print(student.class_data)  # 인스턴스 이름을 이용해서 클래스 속성에 접근

Student.class_data = '클래스 데이터 수정'
print(Student.class_data)  # 클래스 이름을 이용해서 클래스 속성에 접근
print(student.class_data)  # 인스턴스 이름을 이용해서 클래스 속성에 접근

student.class_data = '인스턴스를 이용해서 클래스 데이터 수정'  # 인스턴스가 있으면 수정, 없으면 만들어버림.
# 인스턴스 안에 만드려면 self를 썼어야 함.
print(Student.class_data)  # 클래스 이름을 이용해서 클래스 속성에 접근 # 클래스 안에서 찾기 때문에 클래스 안에 있는 class_data를 불러 옴.
print(student.class_data)  # 인스턴스 이름을 이용해서 클래스 속성에 접근

# 클래스의 속성은 인스턴스 간 동일한 속성만 저장하고, 인스턴스 속성은 각 인스턴스마다 다른 데이터를 적어줘야 함.