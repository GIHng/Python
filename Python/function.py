def display():
    for i in range(3):
        print('Hello Python')


def add(a: int, b: int) -> int:
    return a + b


display()  # 함수 이름은 함수를 저장한 곳의 참조
print(add(3, 4))

def callByValue(a : int) -> None:
    a = 20
    print(a)

x = 30
callByValue(x) # 함수 내에서 외부에 있는 x의 데이터를 바꾸지 못함.
print(x)

def callByReference(li : list) -> None:
    li[0] = 20 # 함수 내부에서 바꿀 수 있다.
    print(li)

l = [100, 200, 300]
callByReference(l) # list는 vector 데이터이기 때문에 l에 대한 참조를 넘겨줌. 데이터를 바꿀 수 있음. [20, 200, 300]
print(l)