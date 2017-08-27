# -*- coding: utf-8 -*-
import sqlite3

import json
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

import dao

app = Flask(__name__)

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
        
    return dao.CountByMediaType()
    #if request.method == 'GET':
    #    return 'ciao ciao:' + request.form['username']
    
    
    
    
    
if __name__ =='__main__':
    app.run(debug=True)