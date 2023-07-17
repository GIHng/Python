ar = [10, 20, 30]
try:
    su = int(input("나눌 수를 입력하세요"))

    i = 0
    while i < len(ar):
        if su == 1:
            raise ValueError("강제 에러")
        assert su != 2, 'su는 2이면 안 됩니다.'  # su의 값이 2라면 메시지를 출력하고 프로그램은 중단 된다.
        print(ar[i] / su)
        i = i + 1

except ValueError as e:  # 유효성 검사로 우회할 수 있었다.
    print("잘못된 데이터를 입력하셨습니다.")
    print(e)    
except ZeroDivisionError as e:  # 유효성 검사로 우회할 수 있었다.
    print("0으로 나눌 수 없습니다.")
    print(e)
else:
    print("정상적으로 종료되었습니다.")

# 예외 처리 구문이 끝나버림, finally는 구문의 마지막. (순서를 지켜야 함.)
finally:
    print("무조건 수행할 내용")

# else와 finally를 같이 사용하고자 하는 경우에는 else를 먼저 작성해야 한다.