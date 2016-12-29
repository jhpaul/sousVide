#import control
import tempRead
from flask import Flask
from flask import request, flash, redirect, url_for, render_template, jsonify
import time
import sys

app = Flask(__name__)

setTemp = 70
	
@app.context_processor
def util():
	def currentTemp():
		return str(round(tempRead.read_temp(),2))	
	return dict(temp=currentTemp(), setTemp=setTemp)
	
@app.route('/')
def index():
#	return "hello"
	return render_template('index.html')
	
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80)
