class Sup:
    def __init__(self):
        self.name = 'no_name'  # super에 name이라는 속성이 생김.
    def superMethod(self):
        print("상위 클래스의 메서드")


# Sup 클래스를 상속받는 클래스

class Sub(Sup):  # 상위 클래스 Sup로부터 상속받은 하위 클래스 Sub
    def __init__(self):
        super().__init__()  # 필수!
        self.score = 80   # 생성하면 상위 클래스의 __init__를 호출하지 않는다.
        # 하위 클래스에 __init__를 만들 때는 상위 클래스의 __init__를 호출해줘야 한다.

    def subMethod(self):
        print("하위 클래스의 메서드")

#
# Sub의 인스턴스를 생성 및 메서드 호출

sub = Sub()
sub.subMethod()
sub.superMethod()  # 하위 클래스의 인스턴스는 상위 클래스의 메서드를 부를 수 있다.
print(sub.name)  # 상위 클래스의 속성에 접근할 수 있다. 
print(sub.score)
sup = Sup()
sup.superMethod()
# sup.subMethod() 상위 클래스의 인스턴스가 하위 클래스의 메서드를 부를 순 없다.
