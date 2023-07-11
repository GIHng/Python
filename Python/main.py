import sys
import mymath


sys.path.append("./") # 현재 디렉토리에서 모듈이나 패키지를 검색하도록 설정
print(sys.path)
print(mymath.MYPI)
mymath.func('message')