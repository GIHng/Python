outer_data = '전역 데이터'
def outer():
    outer_data = '함수 외부에 만든 데이터'

    def inner():
        global outer_data # 전역 데이터를 부름.
        # 함수 내부에서 데이터를 생성하지 않고 외부의 데이터를 사용하기 위해서 이름을 다시 등록.
        outer_data = '함수 내부에서 수정한 데이터'
        print(outer_data)

    inner()
    print(outer_data)


outer()
