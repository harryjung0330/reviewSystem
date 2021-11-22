import pymysql

host = 'reviewdb.ccres59nk3ay.us-east-2.rds.amazonaws.com'
user = 'admin'
password = 'Insukkim!6810'
database = 'reviewDB'

connection = pymysql.connect(host = host, port = 3306, user=user, passwd=password, db=database, charset = 'utf8')
cursor = connection.cursor()
cursor.execute("START TRANSACTION")
#cursor.execute("INSERT INTO business(busiName, country, city, streetAddr, detailAddr) values('세종대학식', '한국', '서울시', )")
#userId = cursor.execute("INSERT INTO businessPict(busSysId, busiPictPath) values(10, 'https://reviewsysbusibucket.s3.us-east-2.amazonaws.com/busiPict/10/%EC%84%B8%EC%A2%85%EB%8C%80+%EA%B5%B0%EC%9E%90%EA%B4%80.jpg')")
cursor.execute("UPDATE review SET trust = 3 WHERE reviewId = 50")
cursor.execute("UPDATE review SET trust = 1.8 WHERE reviewId = 49")
re = cursor.fetchall()
cursor.execute("COMMIT")
print(re)

connection.close()