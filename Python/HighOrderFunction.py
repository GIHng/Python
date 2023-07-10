#함수가 함수를 내부에 만들어서 리턴하면 고위 함수라고 한다.
def outer():
    print('외부 함수')
    outer_data = '외부 함수의 데이터'
    def inner():
        inner_data = '내부 함수의 데이터'
        print("내부 함수")
    return inner
    # print(inner_data)를 사용할 수 없음.
# 함수를 호출해서 그 결과를 변수에 대입하고 그 변수를 통해서 함수를 호출한다.
func = outer()
# inner()를 호출할 순 없음.
func()