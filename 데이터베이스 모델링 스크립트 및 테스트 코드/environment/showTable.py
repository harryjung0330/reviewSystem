import pymysql

host = 'reviewdb.ccres59nk3ay.us-east-2.rds.amazonaws.com'
user = 'admin'
password = 'Insukkim!6810'
database = 'reviewDB'

connection = pymysql.connect(host = host, port = 3306, user=user, passwd=password, db=database, charset = 'utf8')
cursor = connection.cursor()

#cursor.execute("SELECT reviewId, busSysId, isDeleted, productName FROM review natural join reviewProductNames")

#cursor.execute("SHOW CREATE TABLE user")
cursor.execute("START TRANSACTION")
cursor.execute("SELECT * FROM business")
re = cursor.fetchall()
cursor.execute("COMMIT")

for r in re:
    print(r)

connection.close()
