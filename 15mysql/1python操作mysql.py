import pymysql

# 连接数据库
db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='test')
# print(db)
# 设置字符编码
db.set_charset('utf8')
#创建游标对象  用于下面的操作
cursor = db.cursor()
# sql语句执行
# 查询
# sql = 'select * from user'
# 执行SQL语句
# cursor.execute(sql)
# 获取所有
# print(cursor.fetchall())
# 获取一条
# print(cursor.fetchone())

try:
    # 插入数据
    # sql = 'insert into user values(4, "lucky", 18, 1)'
    sql = 'insert into user values(null, "lucky", 18, 1)'
    cursor.execute(sql)
    print(cursor.rowcount)  # 受影响的行数
    db.commit()  # 提交事务
except:
    db.rollback()   # 回滚事务