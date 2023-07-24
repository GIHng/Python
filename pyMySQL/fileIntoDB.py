import pymysql
import sys

con = pymysql.connect(host='localhost', port=3306, db='adam', user='root', passwd='wnddkd', charset='utf8')

# SQL 실행 객체 생성
cursor = con.cursor()

f = open('image.jpg', 'rb')
image = f.read()
f.close()

cursor.execute("INSERT INTO FILETABLE VALUES(%s, %s)", ("image.jpg", image))

# 작업이 끝나면 commit를 해줘야 함.
con.commit()
