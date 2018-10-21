import pymysql

# 打开数据库链接
getsql = pymysql.connect(host="localhost",port=3316,user="root",password="",db="test")

cur = getsql.cursor()

sql = "insert into user(id,name,age) values(8,'ee','70')"

try:
	cur.execute(sql)
	#提交
	getsql.commit()
except Exception as e:
	#错误回滚
	getsql.rollback()
finally:
    getsql.close()
