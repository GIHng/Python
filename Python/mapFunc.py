ar = ['123456', '456789', '789012']


def f(x):
    if len(x) > 3:
        return x[0:3] + "..."
    return x


temp = list(map(f, ar))  # ar의 모든 요소에 f 함수를 적용해서 변환한 결과를 temp에 대입 lambda로 구현할 수 없음.
print(temp)
