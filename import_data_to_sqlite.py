# -*- coding: utf-8 -*-
# coding = utf-8
#将生成的 sql 放入 batchinsert.sql 文件中，然后逐行读入写入 sqlite
#不得不说，本机执行sqlite还是挺快的


import codecs
import sqlite3

#db_file = 'D:\wwwroot\flask\app\fxh.db'

conn = sqlite3.connect('fxh.db')

c = conn.cursor()
 
 # 建表脚本 
c.execute('''CREATE TABLE articles              
     (id int, dataID int, forumID int, webName text, forumName text,
     topicID text, topicTitle text,	topicLink text, author text,
     pubTime text, authorLink text, replyNum int, viewNum int,
     lastReplier text, lastReplyTime text, lastReplierLink text, 
     topicContent text, spiderDate text, spiderTime text, 
     SYSspiderTime text, mediaType text, Dlevel int, isManu int,
     DTopicKind int, effectIndex int, DlevelKey text,	alexa int,
     remark text,	xid int)''') 

#写入单条数据
#c.execute("insert into articles values ('1903214','0','0','大江网','  -*-  ','http://news.jxnews.com.cn/system/2016/09/19/015207804.shtml','市场聚焦美日央行议息港股上涨逾200点','http://news.jxnews.com.cn/system/2016/09/19/015207804.shtml','大江网','2016-09-19 19:35:00','','0','0','','2016-09-19 19:35:00','http://www.alexa.com','　　市场聚焦美日央行议息港股上涨逾200点  　　http://www.jxnews.com.cn2016-09-1919:42:35来源：中国新闻网编辑：jxnews作者：佚名  　　中新社香港9月19日电在美联储和日本央行即将宣布利率决议的背景下，香港恒生指数19日高开约151点至23486点，随后持续走高，最高升至23625点，全日收报23550点，上升约215点，升幅为0.92%，主板成交额为725.04亿港元。  　　当日，8成蓝筹股股价上涨。中国人寿升4.36%，领涨蓝筹股；华润置地、百丽国际、恒隆地产、信和置业的升幅均超过3%；中资银行股中，工商银行升2.07%，交通银行升1.85%，中国银行升1.69%，建设银行升1.37%，中银香港跌0.52%；金沙中国跌4.59%，跌幅最大；蒙牛乳业跌2.98%；其他股价下跌的蓝筹股跌幅均不到1%。国企指数升1.58%，红筹指数升1.25%。  　　永丰金融集团表示，即将迎来的美日利率决议，虽然按兵不动的预期高，但仍存在不确定性，料各类资产波幅加大，不得不格外小心。  　　富汇证券负责人何志铭表示，港股经过一轮调整后于低位有企稳迹象，市场观望本周美联储议息和港股通重开后额度使用情况，预料恒指短线继续于23300点至23800点水平上落。  　　国泰君安证券(香港)有限公司表示，美联储9月加息机会预期较低，但最新较佳的通胀数字为年底加息提供更充分的理据。在美国加息时机不确定的背景下，港股近期明显回吐，预计香港市场在近期区间震荡。(完)  　　1、凡本网注明“中国江西网讯”或“中国江西网”、“大江网”的所有作品，版权均属于中国江西网，未经本网授权不得转载、摘编或利用其它方式使用上述作品。已经本网授权使用作品的，应在授权范围内使用，并注明“来源：中国江西网”。违反上述声明者，本网将追究其相关法律责任。  　　2、凡本网注明“中国江西网讯[xxx报]”或“中国江西网-xxx报”的所有作品，版权均属于江西日报社，未经本网授权不得转载、摘编或利用其它方式使用上述作品。已经本网授权使用作品的，应在授权范围内使用，并注明“来源：中国江西网・xxx报”。违反上述声明者，本网将追究其相关法律责任。  　　3、凡本网注明“来源：xxx（非中国江西网）”的作品，均转载自其它媒体，转载目的在于传递更多信息，并不代表本网赞同其观点和对其真实性负责。本网转载其他媒体之稿件，意在为公众提供免费服务，不授权任何机构、媒体、网站或个人从本网转载、截取、复制和使用。如稿件版权单位或个人不想在本网发布，可与本网联系，本网视情况可立即将其撤除。  　　4、如因作品内容、版权和其它问题需要同本网联系的，请在30日内进行。  　　※联系方式：中国江西网电话：0791-86849032  　　日本史学家用古地图再证钓鱼岛属于中国...时速350公里复兴号售票：京沪每天7对车...台风登陆现场直击船“上”马路车“游”...黑龙江女子不堪虐待杀死男友隐姓埋名外...台风“天鸽”侵袭澳门已致8人死亡153人...问题突出政府网站整改：有的仍无法访问...章莹颖案开审或推后：量刑悬未决，公道...北京“裸婚”人：没房没车相恋11年不结...黑龙江一饭店员工持刀劫持主管被警方击...加拿大一黑熊尾随2岁幼童进屋猛男一拳...  　　更多大江专题  　　','2016-09-19','2016-09-19 19:35:00','2017-08-25 11:26:36','新闻','0','0','0','0','','0','NEW第一次抓取','0')")


#测试读出写入的数据
c.execute('SELECT * FROM articles order by ID desc')
print(c.fetchone())

#批量写入数据
fo = codecs.open(r'D:\wwwroot\flask\app\BatchInsert.sql', 'r', 'utf-8')
lines = fo.readlines()
fo.close()
rn = 0
for line in lines:
    #print(line)
    #break;
    c.execute(line)
    rn = rn +1
    print(rn)

conn.commit()


conn.close()
 