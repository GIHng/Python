import pymysql
import sys
try:
    con = pymysql.connect(host='localhost', port=3306, db='adam', user='root', passwd='wnddkd', charset='utf8')
    print(con)
except:
    print("예외 발생", sys.exc_info)
finally:
    if con != None:
        con.close()