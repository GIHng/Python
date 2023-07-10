score = int(input())

if score >= 60:
    data = 30 # else 갈 경우 이 문장이 실행되지 않음.
    print('합격')
else: # 블록이 다르기 때문에 data 사용할 수 없음
    print('불합격')

print('프로그램 종료')
