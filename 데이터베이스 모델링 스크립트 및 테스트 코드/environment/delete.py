import pymysql

host = 'reviewdb.ccres59nk3ay.us-east-2.rds.amazonaws.com'
user = 'admin'
password = 'Insukkim!6810'
database = 'reviewDB'

connection = pymysql.connect(host = host, port = 3306, user=user, passwd=password, db=database, charset = 'utf8')
cursor = connection.cursor()

#cursor.execute("SELECT * FROM review")
cursor.execute("START TRANSACTION")
cursor.execute("DELETE FROM review")
cursor.execute("COMMIT")
#cursor.execute("SELECT * FROM likes")
re = cursor.fetchall()
for a in re:
    print(a)

connection.close()