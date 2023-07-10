#함수가 함수를 내부에 만들어서 리턴하면 고위 함수라고 한다.
def outer():
    def inner():
        print("내부 함수")
    return inner

# 함수를 호출해서 그 결과를 변수에 대입하고 그 변수를 통해서 함수를 호출한다.
func = outer()
func()