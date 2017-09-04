import json
import sqlite3
import flask


db_file = r'fxh.db'

"""
表结构
 (id int, dataID int, forumID int, webName text, forumName text,
     topicID text, topicTitle text,	topicLink text, author text,
     pubTime text, authorLink text, replyNum int, viewNum int,
     lastReplier text, lastReplyTime text, lastReplierLink text, 
     topicContent text, spiderDate text, spiderTime text, 
     SYSspiderTime text, mediaType text, Dlevel int, isManu int,
     DTopicKind int, effectIndex int, DlevelKey text,	alexa int,
     remark text,	xid int)''') 

"""
#媒体类型
def CountByMediaType():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('SELECT mediaType, count(ID) as num FROM articles group by mediaType')
    rs = c.fetchall()
    conn.close()
    return(json.dumps(rs))

CountByMediaType()

#媒体名称
def CountByWebName():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('SELECT webName, count(ID) as num FROM articles group by webName order by count(ID) desc limit 30')
    rs = c.fetchall()
    conn.close()
    return(json.dumps(rs))

#时间序列
def CountByDate():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('SELECT date(pubTime), count(ID) as num FROM articles group by date(pubTime) order by date(pubTime) ')
    rs = c.fetchall()
    conn.close()
    return(json.dumps(rs))

CountByDate()



def getArticles(currPage=0, pageSize=10):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    
    #获得所有记录总数
    
    c.execute('SELECT count(*) FROM articles')
    rs = c.fetchone()
    
    rowsCount = rs[0]        
    #print(rowsCount)    
    
    c.execute('SELECT ID,mediaType,webName,topicTitle,author,topicLink,pubTime,DtopicKind,viewNum,replyNum FROM articles limit ' +  str(pageSize) + ' offset ' + str((currPage -1)*pageSize))
    rs = c.fetchall()
    
    
    data = []
    for r in rs:  
        d = {}
        d['id'] = r[0]
        d['mediaType'] = r[1]
        d['webName'] = r[2]
        d['topicTitle'] = r[3]
        d['author'] = r[4]        
        d['topicLink'] = r[5]
        d['pubTime'] = r[6]
        d['DtopicKind'] = r[7]
        d['viewNum'] = r[8]
        d['replyNum'] = r[9]
        
        
        data.append(d)
    conn.close()

    #去掉前后的 []
    jsonStr = json.dumps(data)
    
    jsonStr = '{"total":' + str(rowsCount) + ',"rows":' + jsonStr + '}';  
    
    return jsonStr
    #return jsonStr[1:-1]
        
    #return rs
    #return(json.dumps(rs))


getArticles(1,2)

