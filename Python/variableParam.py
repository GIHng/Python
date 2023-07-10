# def merge(name, *li):
def merge(*li, name):
    for element in li:
        print(element)


# merge("A", 10, 20, 30) # name에 A가 대입되고 나머지는 li에 대입
merge(10, 20, 30, name="A")  # 가변 매개변수 뒤의 name 데이터는 변수명을 지정해줘야 한다.


def merge(name, **param):  # dict 형태로 받을 수 있다.
    for k in param:
        print(k, param[k])


merge(name="A", b="B", c="C")
