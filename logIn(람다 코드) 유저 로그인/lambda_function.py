import json
import boto3
import gzip
import base64
import zlib
import pymysql
import cgi
import io

import pymysql

def createUserStat(name, phoneNumb, socialSec, logInId="null", psw = "null", country="null", city="null", streetAddr="null", detailAddr="null", emailAddr="null"):
    insertStat = "INSERT INTO user(logInId, psw, name, phoneNumb, country, city, streetAddr, detailAddr, socialSec, emailAddr) values({}, {}, {}, {}, {},{},{},{},{},{})"
    inserStat = insertStat.format(changeFormat(logInId), changeFormat(psw), changeFormat(name), changeFormat(phoneNumb), changeFormat(country), 
            changeFormat(city), changeFormat(streetAddr), changeFormat(detailAddr), changeFormat(socialSec), changeFormat(emailAddr))
    return inserStat
    
def createBusinessStat(businessName, phoneNumb,  country, city, streetAddr, emailAddr = "null", bid = "null" , logBusId="null", psw = "null", detailAddr = "null"):
    insertStat = "INSERT INTO business(busiName, phoneNumb, emailAddr, bid, logBusId, psw, country, city, streetAddr, detailAddr) values( {}, {}, {}, {},{},{},{},{},{}, {})"
    insertStat = insertStat.format(changeFormat(businessName), changeFormat(phoneNumb), changeFormat(emailAddr), changeFormat(bid), changeFormat(logBusId), 
        changeFormat(psw), changeFormat(country), changeFormat(city), changeFormat(streetAddr), changeFormat(detailAddr))
    return insertStat

def insertBusinessPict(busSysId, businessPictList = []):
    insertStat = "INSERT INTO businessPict(busSysId, busiPictPath) values"
    for pictPath in businessPictList:
        insertStat = insertStat + "({},'{}'),".format(busSysId, pictPath)
    return insertStat[:-1]

def insertBusinessProd(busSysId, businessProdList = []):
    insertStat = "INSERT INTO busiProd(busSysId, productName, price, productPictPath) values"
    for businessProd in businessProdList:
        insertStat = insertStat + "({},'{}', {}, {}),".format(busSysId, businessProd[0], businessProd[1], changeFormat(businessProd[2])) #(busSysId, prodName, price, pictPath)
    return insertStat[:-1]

def registerPlatform(platformName, bid = "null", phoneNumb = "null",country="null", city="null", streetAddr="null", detailAddr="null", apiKey = "null"):
    insertStat = "INSERT INTO platform(platformName, bid, phoneNumb, country, city, streetAddr, detailAddr, apiKey) values({}, {}, {}, {}, {}, {}, {}, {})"
    insertStat = insertStat.format(changeFormat(platformName), changeFormat(bid), phoneNumb, changeFormat(country), changeFormat(city), changeFormat(streetAddr),
        changeFormat(detailAddr), changeFormat(apiKey))
    return insertStat

def getLikesStat(userId):
    return """SELECT count(*) FROM likes WHERE reviewId in (SELECT reviewId FROM review WHERE userSysId = {})""".format(userId)

def getHatesStat(userId):
    return """SELECT count(*) FROM hates WHERE reviewId in (SELECT reviewId FROM review WHERE userSysId = {})""".format(userId)

def getCommentNum(userId):
    return """SELECT count(*) FROM review WHERE userSysId = {}""".format(userId)
    
def createNewReviewStat(userId, busId, platformName, reviewContent, trust, rating, authPlatformName, authUserSysId, authBusSysId, authVisitedTime, revDate = "CURRENT_TIMESTAMP()"):
    if(revDate != "CURRENT_TIMESTAMP()"):
        revDate = "'" + revDate + "'"
    insertStat = """INSERT INTO review(userSysId, busSysId, srcPlatform, reviewContent, trust, rating, authPlatformName, authUserSysId,
        authBusSysId, authVisitedTime, revDate) values({}, {}, '{}', '{}', {}, {},'{}',{}, {}, '{}' ,{})"""
    insertStat = insertStat.format(userId, busId, platformName, reviewContent, trust, rating, authPlatformName, authUserSysId, authBusSysId, authVisitedTime, revDate)
    return insertStat

def insertReviewPictures(revId, picturePaths):
    insertStat = """INSERT INTO reviewPictures(reviewId, revPictPath) values"""
    for path in picturePaths:
        insertStat = insertStat + "({}, '{}'),".format(revId, path)
    return insertStat[:-1]
    
def insertReviewProds(revId, prods):
    insertStat = """INSERT INTO reviewProductNames(reviewId, productName) values"""
    for prod in prods:
        insertStat = insertStat + "({}, '{}'),".format(revId, prod)
    return insertStat[:-1]
    
def updateReviewStat(reviewId, reviewContent, rating, srcPlatform, revDate = "CURRENT_TIMESTAMP()"):
    if(revDate != "CURRENT_TIMESTAMP()"):
        revDate = "'" + revDate + "'"
    updateStat = """UPDATE review SET reviewContent = '{}', rating = {}, srcPlatform = '{}', revDate = {} WHERE reviewId = {}"""
    return updateStat.format(reviewContent, rating, srcPlatform, revDate, reviewId)

def deleteReviewPictures(revId):
    return """DELETE FROM reviewPictures WHERE reviewId = {}""".format(revId)

def deleteReviewProds(revId):
    return """DELETE FROM reviewProductNames WHERE reviewId = {}""".format(revId)

def deleteReviewStat(revId):
    return "UPDATE review SET isDeleted = 1 WHERE reviewId = {}".format(revId)
    
def getReviewsForABusiStat(busSysId, userSysId):
    return """SELECT reviewId, revDate, reviewContent, trust, rating, likeNum, hateNum, paths, prods, srcPlatform, 
        CASE WHEN reviewId in (SELECT reviewId FROM likes WHERE userSysId = {}) THEN 1 ELSE 0 END AS liked,
        CASE WHEN reviewId in (SELECT reviewId FROM hates WHERE userSysId - {}) THEN 1 ELSE 0 END AS hated FROM review 
        natural left outer join (SELECT reviewId, count(*) AS likeNum FROM likes GROUP BY reviewId) AS likeG 
        natural left outer join (SELECT reviewId, count(*) AS hateNum FROM hates GROUP BY reviewId) AS hateG 
        natural left outer join (SELECT reviewId, GROUP_CONCAT(revPictPath SEPARATOR ';') AS paths FROM reviewPictures GROUP BY reviewId) AS picPaths 
        natural left outer join (SELECT reviewId, GROUP_CONCAT(productName SEPARATOR ';') AS prods FROM reviewProductNames GROUP BY reviewId) AS prods
        WHERE isDeleted = 0 AND busSysId = {}""".format(userSysId, userSysId, busSysId)

def getRatingStat(busSysId):
    return """SELECT sum(trustFor) FROM (SELECT trust * rating / sum(trust) AS trustFor FROM review WHERE busSysId = {}) AS T""".format(busSysId)

def getRatingStat2(busSysId):
    return """SELECT sum(T) FROM (SELECT rating / count(*) AS T FROM review WHERE busSysId = {}) AS tem""".format(busSysId)

def insertIntoAuthenticateStat(platformName, userSysId, busSysId, visitedTime = "CURRENT_TIMESTAMP()"):
    if(visitedTime != "CURRENT_TIMESTAMP()"):
        visitedTime = "'" + visitedTime + "'"
    insertStat = """INSERT INTO authenticate(platformName, userSysId, busSysId, visitedTime) values('{}', {}, {}, {})""".format(platformName, userSysId, busSysId, visitedTime)
    return insertStat

def getLastVisitedTimeStat(userSysId, busSysId):
    return """SELECT max(visitedTime) FROM (SELECT visitedTime FROM authenticate WHERE busSysId = {} AND userSysId = {}) AS T""".format(busSysId, userSysId)
    
def getBusiListStat(busiName):
    queryStat = """SELECT busSysId, busiName, city, streetAddr, detailAddr, pictPathGroup, FROM business natural left outer join 
        (SELECT busSysId, GROUP_CONCAT(busiPictPath SEPARATOR ';') AS pictPathGroup FROM businessPict GROUP BY busSysId) AS busPicts
         WHERE busiName LIKE '%{}%'""".format(busiName)
    return queryStat
    
def insertLikeStat(reviewId, userSysId):
    insertStat = """INSERT INTO likes(reviewId, userSysId) VALUES({}, {})""".format(reviewId, userSysId)
    return insertStat
    
def insertHateStat(reviewId, userSysId):
    insertStat = """INSERT INTO hates(reviewId, userSysId) VALUES( {}, {})""".format(reviewId, userSysId)
    return insertStat

def deleteLikeStat(reviewId, userSysId):
    deleteStat = """DELETE FROM likes WHERE reviewId = {} AND userSysId = {}""".format(reviewId, userSysId)
    return deleteStat

def deleteHateStat(reviewId, userSysId):
    deleteStat = """DELETE FROM hates WHERE reviewId = {} AND userSysId = {}""".format(reviewId, userSysId)
    return deleteStat

def logInStat(userLogInId, psw):
    logInStat = """SELECT userSysId FROM user WHERE logInId = '{}' AND psw = '{}' """.format(userLogInId, psw)
    return logInStat

def turnBusiListResultToDicts(fetchedTuples):
    retList = []
    
    for tup in fetchedTuples:
        tempDict = {}
        tempDict["busSysId"] = tup[0]
        tempDict["busiName"] = tup[1]
        tempDict["city"] = tup[2]
        tempDict["streetAddr"] = tup[3]
        tempDict["detailAddr"] = tup[4]
        tempDict["pictPathGroup"] = tup[5]
        retList.append(tempDict)
    return retList

def changeFormat(data):
    if(data != "null"):
        return "'" + data + "'"
    else:
        return data
        

    
#business logic function -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def logIn(cursor, userLogInId, psw):
    cursor.execute(logInStat(userLogInId, psw))
    id = cursor.fetchone()
    if(id != None):
        id = id[0]
    return id

def insertLike(cursor, reviewId, userSysId):
    cursor.execute("START TRANSACTION")
    cursor.execute(insertLikeStat(reviewId = reviewId, userSysId = userSysId))
    cursor.execute("COMMIT")

def insertHate(cursor, reviewId, userSysId):
    cursor.execute("START TRANSACTION")
    cursor.execute(insertHateStat(reviewId = reviewId, userSysId = userSysId))
    cursor.execute("COMMIT")

def deleteLike(cursor, reviewId, userSysId):
    cursor.execute("START TRANSACTION")
    cursor.execute(deleteLikeStat(reviewId = reviewId, userSysId = userSysId))
    cursor.execute("COMMIT")
    
def deleteHate(cursor, reviewId, userSysId):
    cursor.execute("START TRANSACTION")
    cursor.execute(deleteHateStat(reviewId = reviewId, userSysId = userSysId))
    cursor.execute("COMMIT")
    
def insertNewBusiness(cursor ,businessName, phoneNumb,  country, city, streetAddr, emailAddr = "null", bid = "null" , logBusId="null", psw = "null", detailAddr = "null" ,
    businessPictList = [] ,businessProdList = []):
    cursor = connection.cursor()
    cursor.execute("START TRANSACTION")
    cursor.execute(createBusinessStat(businessName, phoneNumb, country, city, streetAddr, emailAddr, bid, logBusId, psw, detailAddr))
    cursor.execute("SELECT LAST_INSERT_ID()")
    lastInsertedId = cursor.fetchone()[0]
    if(len(businessPictList) > 0):
        cursor.execute(insertBusinessPict(lastInsertedId, businessPictList))
    if(len(businessProdList) > 0):
        cursor.execute(insertBusinessProd(lastInsertedId, businessProdList))
    cursor.execute("COMMIT")

def insertNewPlatform(cursor ,platformName, bid = "null", phoneNumb = "null",country="null", city="null", streetAddr="null", detailAddr="null", apiKey = "null"):
    cursor.execute("START TRANSACTION")
    cursor.execute(registerPlatform(platformName, bid, phoneNumb, country, city, streetAddr, detailAddr, apiKey))
    cursor.execute("COMMIT")

def getTrust(cursor, userId):
    cursor.execute(getCommentNum(userId))
    reviewNumb = cursor.fetchone()[0]
    if(reviewNumb == 0):
        return 0
    cursor.execute(getLikesStat(userId))
    likes = cursor.fetchone()[0]
    cursor.execute(getHatesStat(userId))
    hates = cursor.fetchone()[0]
    return ((likes - hates * 10) / (reviewNumb + 1) + 1)  

def createNewReview(cursor, userId, busSysId, reviewContent, rating, prodList = [], srcPlatform = "main", revDate = "CURRENT_TIMESTAMP()" ):
    cursor.execute("""SELECT platformName, userSysId, busSysId, visitedTime FROM authenticate 
                WHERE busSysId = {} AND userSysId = {} AND TIMESTAMPDIFF(DAY, visitedTime , CURRENT_TIMESTAMP()) < 15 AND
                (platformName, userSysId, busSysId, visitedTime) NOT IN (SELECT authPlatformName, authUserSysId, authBusSysId, authVisitedTime
                FROM review where authUserSysId = {} AND authBusSysId = {})""".format(busSysId, userId, userId, busSysId))
    temp = cursor.fetchone()
    if(temp == None):
        return -1
    
    print("retrieved tuple = " + str(temp))
    authPlatformName = temp[0]
    authUserSysId = temp[1]
    authBusSysId = temp[2]
    authVisitedTime = temp[3]
    
    trust = getTrust(cursor ,userId)
    cursor.execute(createNewReviewStat(userId, busSysId, srcPlatform, reviewContent, trust, rating, authPlatformName, authUserSysId, authBusSysId, str(authVisitedTime), revDate))
    cursor.execute("SELECT LAST_INSERT_ID()")
    revId = cursor.fetchone()[0]
    if(len(prodList) > 0):
        cursor.execute(insertReviewProds(revId, prodList))
    return revId

def updateReview(cursor, reviewId, reviewContent, rating, srcPlatform = "main", revDate = "CURRENT_TIMESTAMP()", prodList = [], pictList = []):
    cursor.execute("START TRANSACTION")
    cursor.execute(deleteReviewPictures(reviewId))
    cursor.execute(deleteReviewProds(reviewId))
    cursor.execute(updateReviewStat(reviewId, reviewContent, rating, srcPlatform, revDate))
    if(len(pictList) > 0):
        cursor.execute(insertReviewPictures(reviewId, pictList))
    if(len(prodList) > 0):
        cursor.execute(insertReviewProds(reviewId, prodList))
    cursor.execute("COMMIT")

def deleteReview(cursor ,revId):
    cursor.execute("START TRANSACTION")
    cursor.execute(deleteReviewStat(revId))
    cursor.execute("COMMIT")

def getReviews(cursor, busSysId, userSysId): 
    cursor.execute(getReviewsForABusiStat(busSysId, userSysId))
    return cursor.fetchall()
    
def getRating(cursor, busSysId):
    cursor.execute(getRatingStat(busSysId))
    return cursor.fetchone()[0]

def getRating2(cursor, busSysId):
    cursor.execute(getRatingStat2(busSysId))
    return cursor.fetchone()[0]
    
def insertIntoAuthenticate(cursor, userSysId, busSysId, platformName = "main", visitedTime = "CURRENT_TIMESTAMP()"):
    cursor.execute("START TRANSACTION")
    cursor.execute(insertIntoAuthenticateStat(platformName, userSysId, busSysId, visitedTime))
    cursor.execute("COMMIT")

def getLastVisitedTime(cursor,userId, busId):
    cursor.execute(getLastVisitedTimeStat(userId, busId))
    return cursor.fetchone()[0]

def getBusiList(cursor, busiName):
    cursor.execute(getBusiListStat(busiName))
    return cursor.fetchall()

def lambda_handler(event, context):
    resPondMsg = 'wrong id or pswd'
    resFlag = 1
    
    print(event)
    body = event["body"]
    host = 'reviewdb.ccres59nk3ay.us-east-2.rds.amazonaws.com'
    user = 'admin'
    password = 'Insukkim!6810'
    database = 'reviewDB'
    
    #fp = io.BytesIO(event['body'].encode('utf-8'))
    #pdict = cgi.parse_header(event['headers']['Content-Type'])[1]
    #if 'boundary' in pdict:
    #    pdict['boundary'] = pdict['boundary'].encode('utf-8')
    #pdict['CONTENT-LENGTH'] = len(event['body'])
    #form_data = cgi.parse_multipart(fp, pdict)
    #print('form_data=', form_data)
    
    cookie = event["headers"].get("cookie")
    if(cookie == None):
        cookie = event["headers"].get("Cookie")
    
    if(cookie == None):
        cookie = -1
    
    print("cookie is " + str(cookie))
    
    li = body.split('&')
    form_data = {}
    for comp in li:
        dat = comp.split('=')
        form_data[dat[0]] = dat[1]
        
    logInId = form_data["userLogInId"]
    psw = form_data["psw"]
    
    
    try:
        connection = pymysql.connect(host = host, port = 3306, user=user, passwd=password, db=database, charset = 'utf8')
        cursor = connection.cursor()
        revId = logIn(cursor, logInId, psw)
        if(revId == None):
            return  {
            'statusCode': 200,
            'headers' : {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({
                    "respondMsg": resPondMsg,
                    "resFlag": resFlag
            })
                
            }
            
        resFlag = 0
        resPondMsg = "logIn succeed!"
        cursor.execute("START TRANSACTION")
        cursor.execute("SELECT createNewCookie({},  '{}')".format(revId, cookie))
        cookie = cursor.fetchone()[0]
        cursor.execute("COMMIT")
        resPondMsg = "Success!"
        
    except Exception as e:
        connection.rollback()
        resPondMsg = str(e)
        resFlag = 1
        
    finally:
        connection.close()
    
    return {
        'statusCode': 200,
        "headers": {
            "Set-Cookie":cookie + "; Path/ ", 
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            "respondMsg": resPondMsg,
            "resFlag": resFlag
        })
    }
