# -*- coding: utf-8 -*-
import sqlite3

import json
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import Response
from flask import send_file


import dao

#app = Flask(__name__)

app = Flask(__name__,static_url_path='',root_path=r'D:\wwwroot\flask\fxh')  

def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/' , methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        a = request.get_data()
        return 'bonjuno ' + a
		#dict1 = json.loads(a)
        #return json.dumps(dict1["data"])
    else:
        return '<h1>只接受GET请求！</h1>'

@app.route('/user/<name>')
def user(name):
    return'<h1>hello, %s</h1>' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    return 'ciao ciao ' + request.args.get('username', '')
    #if request.method == 'GET':
    #    return 'ciao ciao:' + request.form['username']
	
#获得不同mediaType的统计
@app.route('/getCountByMediaType', methods=['POST', 'GET'])
def getCountByMediaType():
    content = dao.CountByMediaType()
    resp = Response_headers(content)
    return resp
    #if request.method == 'GET':
    #    return 'ciao ciao:' + request.form['username']
    
#获得不同webName的统计
@app.route('/getCountByWebName', methods=['POST', 'GET'])
def getCountBywebName():    
    content = dao.CountByWebName()
    resp = Response_headers(content)
    return resp

#获得不同时间的统计
@app.route('/getArticleByDate', methods=['POST', 'GET'])
def getCountByDate():    
    content = dao.CountByDate()
    resp = Response_headers(content)
    return resp


#获得不同mediaType的统计
@app.route('/getArticles', methods=['POST', 'GET'])
def getArticles():
    currPage = int(request.args.get('pageNumber', '0'))
    pageSize = int(request.args.get('pageSize', '10'))
    content = dao.getArticles(currPage,pageSize)
    resp = Response_headers(content)
    return resp

#测试request
@app.route('/testRequest')
def test_request():
    return 'currPage=' + request.args.get('pageNumber', '') + ',pageSize=' + request.args.get('pageSize', '')

    
#静态文件
@app.route('/test')
def test_html():
    return send_file("bst_test.html")
    
#静态文件
@app.route('/report')
def test_report():
    return send_file("report.html")


    
    
if __name__ =='__main__':
    app.run(debug=True)