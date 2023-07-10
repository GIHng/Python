# 이름과 점수를 갖는 객체를 여러 개 필요

class Student:
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score


student = Student()
student.setName('ABC')
student.setScore(50)

student1 = Student()
student1.setName('DEF')
student1.setScore(70)

print(f'student의 이름 {student.getName()} 점수 {student.getScore()}, student1의 이름 {student1.getName()} 점수 {student1.getScore()}')