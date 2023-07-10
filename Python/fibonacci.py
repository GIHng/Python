from functools import lru_cache
#
# N = int(input())
# fibo = [1] * N
#
#
# for i in range(2, N):
#     fibo[i] = fibo[i-1] + fibo[i-2]
#     print(fibo[i] / fibo[i-1])
# print(*fibo)



@lru_cache(maxsize=None)
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(1, 10):
    print(i, fib(i))

# print(dir(__builtins__))