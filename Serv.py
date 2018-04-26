# -*- coding: utf-8 -*-
from flask import Flask, request
from datetime import datetime

dump = []

app = Flask(__name__)

stroki = [['.'] * 10 for i in range(10)]

messages = "<p>"

@app.route("/")
def index():
	return "<h1>Hello world</h1>"



@app.route('/max')
def max_page():
	a =  request.args.get('a', u'0')
	b =  request.args.get('b', u'0')
	c =  request.args.get('c', u'0')
	if a.isnumeric() and b.isnumeric() and c.isnumeric():
		a = int(a)
		b = int(b)
		c = int(c)
		if(a>=b)and(a>=c):
			return str(a)
		elif(b>=a)and(b>=c):
			return str(b)
		elif(c>=a)and(c>=b):
			return	str(c)

@app.route('/datal')
def datal_page():
        s =  request.args.get('data', u'0')
       	ind = 0
	while (s[ind] != '0'):
		ind += 1
	ind = ind / 2 + 1
	return str(ind)

@app.route('/chat', methods=['GET'])
def chat_page():
	global messages
	site = "<form method='GET'><input placeholder='Your name' name='login' style='width:40%'><input placeholder='Your text' name='text' style='width:40%'><input type='submit'></form>"
	if request.method == "GET":
		result = request.form
		messages += datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S :   ") + request.args.get('login', u'0') + ": " + request.args.get('text', u'0') + "<br>"
	site += messages
	dump.append(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S:") + request.args.get('login', u'0') + "/" + request.environ.get("HTTP_X_REAL_IP", request.remote_addr) + ":" + request.args.get('text', u'0'))
	
	return site + "</p>"

@app.route('/data')
def data_page():
        global dump
	sitik = ''
        for i in dump:
		sitik += i + '<br>'
        return "<pre>" + sitik + "</pre>"


app.run(host="Your IP adress", port=50123, debug=True)

//Special for Linux
//By F1reFox
