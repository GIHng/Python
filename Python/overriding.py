class Sup:
    def method(self):
        print("상위 클래스의 메서드")

# Sup 클래스를 상속받는 Sub 클래스
class Sub(Sup):
    # 상위 클래스에 존재하는 메서드를 하위 클래스에서 다시 정의 - Overriding
    def method(self):
        print("하위 클래스의 메서드")

s = Sub()
s.method()