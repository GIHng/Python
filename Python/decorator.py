def deco(func):
    print('공통관심사항')
    func()
@deco  # 이제부터 businesslogic 이라는 함수를 호출하면 deco 함수를 호출한다
# 개발자가 작성한 코드 대신에 다른 코드를 불러낸내는 방식을 프록시 패턴이라고 한다.ㅕ
# 유지보수가 필요하거나 업무 로직과 관련이 없는 코드를 추가하거나 삭제하는 경우 업무로직을 수정하는 것은 위험함.
# 가능하도면 업무로직 안만드는게 나음.

def decorator(func):
    func()


def transaction(): # 이 함수는 한 번에 실행되어야 함
    print("공통 관심 사항_1")
    print("비즈니스 로직")
    print("공통 관심 사항_2")

transaction()