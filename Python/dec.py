import time


def clock(func):  # decorator 가 적용된 함수가 호출되면 수행될 실제 함수
    def clocked(*args):
        start = time.time()  # 현재 시간을 기록
        result = func(*args)
        end = time.time()
        elapsed = end - start

        print('시간', elapsed)
        # 매개변수 확인
        print('매개변수 :', args)
        print('리턴 값:', result)

        return result

    return clocked()

import functools
@functools.lru_cache()
@clock
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
