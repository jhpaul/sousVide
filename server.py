#import control
import tempRead
from flask import Flask
from flask import request, flash, redirect, url_for, render_template, jsonify
import time
import sys
import logging
import helpers
import json
from datetime import datetime
logging.basicConfig(filename='tempLog2.csv',level=logging.DEBUG)

configFile = 'config.json'
statusFile = 'status.json'


app = Flask(__name__)








@app.context_processor
def util():
	with open(configFile, 'r') as f:
	    config = json.load(f)
	with open(statusFile, 'r') as f:
	    status = json.load(f)
	setTemp = status['setTemp']
	currentTemp = status['temp']
	datetime = status['datetime']
	return dict(temp=currentTemp, setTemp=setTemp, datetime = str(datetime))
	
@app.route('/')
def index():
#	return "hello"
	return render_template('index.html')

@app.route('/temp', methods=['GET','PUT','POST'])
def temp():
	if request.method in ('PUT',"POST"):
		with open(statusFile, 'r') as f:
		    status = json.load(f)
		currentTemp = status['temp']
		setTemp = request.args.get('setTemp')
		package = jsonify(method=request.method, temp=currentTemp, setTemp=setTemp)
		# logging.info(str(request.method)+","+str(currentTemp)+","+str(setTemp))
		# print setTemp
		configPackage = {'setTemp': int(setTemp)}
		with open(configFile, 'w') as f:
			json.dump(configPackage, f)
		return package
	else:
		with open(statusFile, 'r') as f:
		    status = json.load(f)
		setTemp = status['setTemp']
		currentTemp = status['temp']
		datetime = status['datetime']
		package = jsonify(method=request.method,temp=currentTemp, setTemp=setTemp, datetime=datetime)
		# logging.info(str(request.method)+","+str(currentTemp)+","+str(setTemp))
		return package


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80)



