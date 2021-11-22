import pymysql

host = 'reviewdb.ccres59nk3ay.us-east-2.rds.amazonaws.com'
user = 'admin'
password = 'Insukkim!6810'
database = 'reviewDB'

connection = pymysql.connect(host = host, port = 3306, user=user, passwd=password, db=database, charset = 'utf8')
cursor = connection.cursor()

#cursor.execute("ALTER TABLE review DROP userSysId")
#cursor.execute("ALTER TABLE review ADD userSysId BIGINT NOT NULL")
#cursor.execute("ALTER TABLE review ADD CONSTRAINT review_userSysId_fk FOREIGN KEY (userSysId) REFERENCES user(userSysId)")
#cursor.execute("ALTER TABLE review DROP CONSTRAINT busSysId")
#cursor.execute("ALTER TABLE review ADD CONSTRAINT review_busSysId_fk FOREIGN KEY (busSysId) REFERENCES business(busSysId)")
#cursor.execute("ALTER TABLE review MODIFY isDeleted BOOLEAN NOT NULL DEFAULT 0")
#cursor.execute("ALTER TABLE user ADD CONSTRAINT phoneNumb_un UNIQUE(phoneNumb)")
#cursor.execute("ALTER TABLE user MODIFY COLUMN phoneNumb varchar(11), MODIFY COLUMN socialSec varchar(13)")
#cursor.execute("ALTER TABLE business MODIFY COLUMN phoneNumb varchar(11), MODIFY COLUMN bid varchar(10)")
#cursor.execute("ALTER TABLE platform MODIFY COLUMN phoneNumb varchar(11), MODIFY COLUMN bid varchar(10)")
#cursor.execute("ALTER TABLE otherPlatformUser DROP CONSTRAINT otherPlatformUser_platformName_fk")
#cursor.execute("ALTER TABLE otherPlatformUser ADD CONSTRAINT otherPlatformUser_platformName_fk FOREIGN KEY (platformName) REFERENCES platform(platformName) ON DELETE CASCADE")
#cursor.execute("ALTER TABLE review ADD rating INT")
#cursor.execute("ALTER TABLE review ADD CONSTRAINT rating_ck CHECK(rating <=5 AND rating >= 0)")
#cursor.execute("ALTER TABLE cookieTable MODIFY cookieTime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP")
#cursor.execute("select substring(MD5(RAND()),1,32)")
#cursor.execute("DROP FUNCTION checkCookie")
#cursor.execute("ALTER TABLE authenticate DROP COLUMN productName")
#cursor.execute("""ALTER TABLE authenticate ADD COLUMN reviewId BIGINT, ADD CONSTRAINT authenticate_reviewId_fk FOREIGN KEY(reviewId) 
#    REFERENCES review(reviewId)""")
#cursor.execute("ALTER TABLE authenticate DROP CONSTRAINT authenticate_reviewId_fk")
#cursor.execute("ALTER TABLE authenticate DROP COLUMN reviewId")
#cursor.execute("ALTER TABLE review ADD COLUMN authPlatformName varchar(60)")
#cursor.execute("ALTER TABLE review ADD COLUMN authUserSysId BIGINT")
#cursor.execute("ALTER TABLE review ADD COLUMN authBusSysId BIGINT")
#cursor.execute("ALTER TABLE review ADD COLUMN authVisitedTime TIMESTAMP")
#cursor.execute("""ALTER TABLE review ADD CONSTRAINT review_authenticate_fk FOREIGN KEY (authPlatformName, authUserSysId, authBusSysId, authVisitedTime) 
#        REFERENCES authenticate(platformName, userSysId, busSysId, visitedTime) ON UPDATE CASCADE """)
#cursor.execute("""ALTER TABLE review ADD CONSTRAINT review_authenticate_un UNIQUE(authPlatformName, authUserSysId, authBusSysId, authVisitedTime)""")
cursor.execute("DROP FUNCTION checkCookie")
res = cursor.fetchall()
print(res)
connection.close()