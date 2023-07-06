year = 2023
#윤년의 조건 - 둘 중 하나만 True이면 True
# 1. 4의 배수이고 100의 배수가 아닌 경우
# 2. 400의 배수인 경우

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 윤년이 아닙니다.")
