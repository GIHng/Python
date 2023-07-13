problem = "GDKKDGCCGDDFDDGCCGCCGDDDGCCGFFF"
# 위 문자열에서 GCCG 의 위치를 전부 출력
# 한 번 포함되면 포함된 문자는 빼고 찾아야 한다
# GCCGCCG는 1번만 찾아야 함.

# help(str.find)
find = []
for i in range(len(problem)):
    print(problem.find('GCCG', i, i+4))

