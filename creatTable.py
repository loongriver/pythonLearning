#倒入mysql驱动
import mysql.connector

conn = mysql.connector.connect(user = 'root', password = '123', database = 'test')
cursor = conn.cursor()

# #创建user表
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# #插入一行记录
cursor.execute('insert into user (id,name) values (%s, %s)',['3','aa'])
print(cursor.rowcount)

#提交事务
conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('2',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()