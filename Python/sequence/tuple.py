record = ("A", "B", "C")  # 튜플 생성
print(record)
# record[0] = "D"  # 오류 발생

# list와 tuple은 unpacking이 가능하다.
name, job, albumCnt = record  # 여러 변수에 데이터를 나누어 저장하는 것.
print(albumCnt)

*etc, albumCnt = record  # *을 이용하면 나머지 모두를 list로 생성.
print(etc)

# swap : 2개의 데이터 값을 치환.
a = 10
b = 20
a, b = b, a
print(a,b)

data = [('A', 'B'), ('C', 'D')]

for row in data:
    print(row[0])

# 컬럼에 이름을 사용하는 튜플
from collections import namedtuple
# 자료구조 생성 - 튜플의 각 컬럼 이름 만들기
Person = namedtuple("Person", "name mobile")
persons = [Person('A', '010'), Person('jessica', '010')]

for person in persons:
    print(person.name)