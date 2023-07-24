import pymysql
import sys

try:
    con = pymysql.connect(host='localhost', port=3306, db='adam', user='root', passwd='wnddkd', charset='utf8')
    print(con)

    # SQL 실행 객체 생성
    cursor = con.cursor()

    # SQL 실행 - 값을 직접 SQL에 작성
    # cursor.execute("INSERT INTO DEPT VALUES(11, '비서','신안')") # statement

    # SQL 실행 - SQL에 서식을 설정하고 파라미터를 대입하는 코드 작성
    # cursor.execute("INSERT INTO DEPT VALUES(%s, %s, %s)", (12, '기획', '제주'))
    # tuple로 값을 전달.  # Prepared Statement 전자정부보안가이드 문서 확인.

    # cursor.execute("UPDATE DEPT SET DNAME = %s, LOC = %s WHERE DEPTNO = %s", ('영업', '서초', 12))

    # con.commit()  # 작업이 끝나면 commit를 해줘야 함.

    cursor.execute("SELECT * FROM DEPT WHERE DEPTNO >= %s", (11))
    # 여러 개의 데이터를 읽을 땐, 데이터가 없는 경우 빈 튜플을 리턴한다. (None이 아님)
    # 데이터를 받는 쪽에서 None을 넘겨주면 Exception이 생길 수 있음.

    record = cursor.fetchall()
    if len(record) is 0: # 데이터가 여러 개 인 경우, 데이터의 개수가 0인지 확인해야 함.
        print("검색된 데이터 없음")
    else:
        print(record) # 튜플 형태로 반환.
except:
    print("예외 발생", sys.exc_info)
finally:
    if con is not None:
        con.close()
