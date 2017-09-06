# -*- coding: utf-8 -*-
import sqlite3

import json
from flask import Flask
from flask import request, session, escape, url_for
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
    if request.method == 'POST':
	    return 'usr=' + request.form.get('username', 'error') + 'pass=' + request.form.get('password', 'error')
    else:
	    return 'currPage=' + request.args.get('pageNumber', '') + ',pageSize=' + request.args.get('pageSize', '')

#测试 Session
@app.route('/testSession')
def testSession():
    #return session['username']
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

		
#静态文件
@app.route('/test')
def test_html():
    return send_file("bst_test.html")
    
#静态文件
@app.route('/report')
def report():
    if 'username' in session:
        return send_file("report.html")
    else:
        return redirect(url_for('signin'))

#登录
@app.route('/signin')
def signin():
    return send_file("signin.html")


#验证用户名和密码
@app.route('/signinAction', methods=['POST', 'GET'])
def signinAction():	    
    if request.method == 'POST':
        if (request.form.get('username', 'error') == 'admin') and request.form.get('password', 'error') == 'test':
            session['username'] = 'admin'
            return redirect(url_for('report'))
        else:
            return '用户名密码不匹配'
    else:
        '错误的请求'
	
	
	
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RTEFDE'    
    
if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
    #app.run(debug=True)