import functools


@functools.lru_cache()
def fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibo(n: int) -> int:
    result = 1
    n_1 = 1
    n_2 = 1
    for i in range(3, n + 1):
        result = n_1 + n_2
        n_2 = n_1
        n_1 = result
    return result


print(fibonacci(500))
print(fibo(500))

fibonacci.__doc__ = "재귀를 이용하여 피보나치 수열의 값을 리턴하는 함수"

help(fibonacci)

