#!/usr/bin/env python3
from flask import Flask, render_template
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('db.json')
number = Query()
if not db.search(number.id == 1):
	db.insert({'id':1,'number':0})
@app.route('/')
def count():
	return render_template('count.html',count=db.search(number.id ==1)[0]['number'])

@app.route('/WHY', methods=['POST'])
def why():
	num = db.search(number.id ==1)[0]['number']+1
	print(num)
	db.update({'number':num}, number.id==1)
	return('Thank you for reporting this error!')

app.run(host='0.0.0.0', port=80)
