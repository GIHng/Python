import pymysql
import sys

con = pymysql.connect(host='localhost', port=3306, db='adam', user='root', passwd='wnddkd', charset='utf8')

cursor = con.cursor()

cursor.execute("SELECT * FROM FILETABLE")
data = cursor.fetchone()

# 두 번째 데이터가 BLOB. 파일로 변경
print(data[0]) # 파일명
f = open(data[0], 'wb')

# 읽은 데이터를 파일에 기록.
f.write(data[1])
f.close()
