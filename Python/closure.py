def outer():
    data = 0

    def inner():
        nonlocal data
        data = data+1
        # 함수 내부의 데이터를 수정하는 함수를 리턴하는 함수를 closure라고 한다.
        print(data)
    return inner

closure = outer() # 함수를 호출해서 리턴하는 함수를 변수에 저장.
closure()
closure()
# data = data+1 # data는 함수 내에서 생성되었기 때문에 함수 밖에서 사용할 수 없다.