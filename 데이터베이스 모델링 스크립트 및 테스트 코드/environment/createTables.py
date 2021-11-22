import pymysql

host = 'reviewdb.ccres59nk3ay.us-east-2.rds.amazonaws.com'
user = 'admin'
password = 'Insukkim!6810'
database = 'reviewDB'

connection = pymysql.connect(host = host, port = 3306, user=user, passwd=password, db=database, charset = 'utf8')
cursor = connection.cursor()

#create user table
#cursor.execute("CREATE TABLE user(userSysId BIGINT NOT NULL auto_increment, logInId varchar(60), psw varchar(40), name varchar(50)"
#",phoneNUmb Decimal(11,0),country varchar(50), city varchar(50), streetAddr varchar(70), detailAddr varchar(70),"
#"socialSec Decimal(13,0), emailAddr varchar(50), CONSTRAINT prima PRIMARY KEY(userSysId), CONSTRAINT logIn_un UNIQUE(logInId),"
#"CONSTRAINT socialSec_un UNIQUE(socialSec), CONSTRAINT emailAddr_ch CHECK(emailAddr LIKE '%@%.___'))")

#create platform table
#cursor.execute("CREATE TABLE platform("
#	"platformName varchar(60) NOT NULL, bid Decimal(10, 0), phoneNumb Decimal(11,0),"
#	"country varchar(50), city varchar(50), streetAddr varchar(70), detailAddr varchar(70),"
#	"apiKey varchar(60), CONSTRAINT prima PRIMARY KEY(platformName), CONSTRAINT bid_un UNIQUE(bid), CONSTRAINT apiKey_un UNIQUE(apiKey))")

#create business table
#cursor.execute("CREATE TABLE business( busSysId BIGINT NOT NULL auto_increment,"
#	"bid Decimal(10,0), logBusId varchar(60), psw varchar(40),"
#	"country varchar(50), city varchar(50), streetAddr varchar(70),"
#	"detailAddr varchar(70), CONSTRAINT prima PRIMARY KEY(busSysId), CONSTRAINT bid_un UNIQUE(bid), CONSTRAINT log_un UNIQUE(logBusId))")

#create businessPict
#cursor.execute("CREATE TABLE businessPict(busSysId BIGINT NOT NULL, busiPictPath varchar(300),"
#	"CONSTRAINT businessPict_busSysId_fk FOREIGN KEY(busSysId) REFERENCES business(busSysId), CONSTRAINT prima PRIMARY KEY(busSysId, busiPictPath))")

#create busiProd
#cursor.execute("CREATE TABLE busiProd(busSysId BIGINT NOT NULL, productName varchar(60),"
#	"price Decimal(13,0), productPictPath varchar(300), CONSTRAINT busiProd_busSysId_fk FOREIGN KEY(busSysId) REFERENCES business(busSysId), CONSTRAINT prima PRIMARY KEY (busSysId, productName))")

#rename constraint
#cursor.execute("ALTER TABLE businessPict DROP CONSTRAINT busSysId_fk")
#cursor.execute("ALTER TABLE businessPict ADD CONSTRAINT businessPict_busSysId_fk FOREIGN KEY (busSysId) REFERENCES business(busSysId)")

#create otherPlatformUser
#cursor.execute("CREATE TABLE otherPlatformUser( userSysId BIGINT NOT NULL, platformName varchar(60) NOT NULL,"
#	"platformId varchar(60),CONSTRAINT otherPlatformUser_userSysId_fk FOREIGN KEY(userSysId) REFERENCES user(userSysId),"
#	"CONSTRAINT otherPlatformUser_platformName_fk FOREIGN KEY(platformName) REFERENCES platform(platformName),"
#	"CONSTRAINT prima PRIMARY KEY (userSysId, platformName))")

#cursor.execute("CREATE TABLE authenticate(platformName varchar(60), userSysId BIGINT NOT NULL,"
#	"busSysId BIGINT NOT NULL, visitedTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP, productName varchar(60),"
#	"CONSTRAINT authenticate_platformName_fk FOREIGN KEY (platformName) REFERENCES platform(platformName),"
#	"CONSTRAINT authenticate_userSysId_fk FOREIGN KEY (userSysId) REFERENCES user(userSysId),"
#	"CONSTRAINT authenticate_busSysId_fk FOREIGN KEY (busSysId) REFERENCES business(busSysId),"
#	"CONSTRAINT prima PRIMARY KEY (platformName, userSysId, busSysId, visitedTime, productName))")

#create review table
#cursor.execute("CREATE TABLE review( reviewId BIGINT auto_increment NOT NULL,"
#	"revDate DATETIME DEFAULT CURRENT_TIMESTAMP, reviewContent varchar(10000),trust Decimal(14,3),"
#	"isDeleted Boolean, srcPlatform varchar(60),busSysId BIGINT NOT NULL, userSysId BIGINT NOT NULL,"
#	"CONSTRAINT review_srcPlatform_fk FOREIGN KEY (srcPlatform) REFERENCES platform(platformName),"
#	"CONSTRAINT review_busSysId_fk FOREIGN KEY (busSysId) REFERENCES business(busSysId),"
#	"CONSTRAINT review_userSysId_fk FOREIGN KEY(userSysId) REFERENCES user(userSysId),"
#	"CONSTRAINT prima PRIMARY KEY (reviewId))")

#create reviewPictures
#cursor.execute("CREATE TABLE reviewPictures(reviewId BIGINT NOT NULL,"
#	"revPictPath varchar(300),CONSTRAINT reviewPictures_reviewId_fk FOREIGN KEY( reviewId) REFERENCES review(reviewId),"
#	"CONSTRAINT prima PRIMARY KEY (reviewId, revPictPath))")

#create likes
#cursor.execute("CREATE TABLE likes("
#	"reviewId BIGINT NOT NULL,"
#	"userSysId BIGINT NOT NULL,"
#	"CONSTRAINT likes_reviewId_fk FOREIGN KEY(reviewId) references review(reviewId),"
#	"CONSTRAINT likes_userSysId_fk FOREIGN KEY(userSysId) references user(userSysId),"
#	"CONSTRAINT prima PRIMARY KEY (reviewId, userSysId))")

#create hates
#cursor.execute("CREATE TABLE hates("
#	"reviewId BIGINT NOT NULL,"
#	"userSysId BIGINT NOT NULL,"
#	"CONSTRAINT hates_reviewId_fk FOREIGN KEY(reviewId) references review(reviewId),"
#	"CONSTRAINT hates_userSysId_fk FOREIGN KEY(userSysId) references user(userSysId),"
#	"CONSTRAINT prima PRIMARY KEY (reviewId, userSysId))")

#create reviewProductName
#cursor.execute("CREATE TABLE reviewProductNames("
#	"reviewId BIGINT NOT NULL,"
#	"productName varchar(60),"
#	"CONSTRAINT prima PRIMARY KEY(reviewId, productName))")

#create cookieTable
#cursor.execute("""CREATE TABLE cookieTable (cookie varchar(40) NOT NULL, userSysId BIGINT NOT NULL, cookieTime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
#	CONSTRAINT prima PRIMARY KEY(cookie), CONSTRAINT cookieTable_userSysId_fk FOREIGN KEY(userSysId) references user(userSysId))""")

#create insertCookieFunction
#cursor.execute("SET GLOBAL log_bin_trust_function_creators = 1;")
#cursor.execute("""CREATE FUNCTION createNewCookie(userId BIGINT, old_cookie varchar(40))
#    RETURNS varchar(40)
    
#    BEGIN
#        DECLARE new_cookie varchar(40);
#        DECLARE num12 int;
#        
#        SET new_cookie = (SELECT substring(MD5(RAND()),1,32));
#        SET num12 = (SELECT count(*) FROM cookieTable WHERE cookie = new_cookie);
#               WHILE num12 > 0 DO
#            SET new_cookie = (SELECT substring(MD5(RAND()),1,32));
#            SET num12 = (SELECT count(*) FROM cookieTable WHERE cookie = new_cookie);
#        END WHILE;
        
      
#        INSERT INTO cookieTable values(new_cookie, userId, CURRENT_TIMESTAMP);
#        DELETE FROM cookieTable WHERE cookie = old_cookie;
        
#        return new_cookie;
#    END""")

#create checkCookie function
#cursor.execute("""CREATE FUNCTION checkCookie(cook varchar(40))
#    RETURNS BIGINT
#    BEGIN
#        DECLARE userId BIGINT;
        
#        SET userId = (SELECT IFNULL((SELECT userSysId FROM cookieTable WHERE cookie = cook), -1));
        
 #       IF userId != -1
 #       THEN
 #           IF ( (SELECT TIMESTAMPDIFF(SECOND, cookieTime, CURRENT_TIMESTAMP) FROM cookieTable WHERE cookie = cook) > 10800)
 #           THEN
 #               SET userId = -1;
 #               DELETE FROM cookieTable WHERE cookie = cook;
 #           ELSE
 #               UPDATE cookieTable SET cookieTime = CURRENT_TIMESTAMP() WHERE cookie = cook;
 #           END IF;
 #       END IF;
 #       
 #       return userId;
 #       
 #   END
#""")

connection.close()