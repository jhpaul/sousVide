#import control
import tempRead
from flask import Flask
from flask import Markup, request, flash, redirect, url_for, render_template, jsonify
import os
import time
import sys
import logging
import helpers
import json
import csv
import HTMLParser
html_parser = HTMLParser.HTMLParser()

from datetime import datetime
fileDir = os.path.dirname(os.path.realpath(__file__)) 
print fileDir
logging.basicConfig(filename=fileDir+'/tempLog2.csv',level=logging.DEBUG)
configFile = fileDir+'/config.json'
statusFile = fileDir+'/status.json'
historyFile = fileDir+'/history.json'

app = Flask(__name__)









@app.context_processor
def util():
	with open(statusFile, 'r') as f:
	    status = json.load(f)
	with open (historyFile, 'r') as f:
	    historyList = (f.read())
	with open(configFile, 'r') as c:
            config = json.load(c) 
	#historyList = ""
	#historyList = str(list(reader)).replace("'", '"')
	#print historyList
        mode = config['mode']
	power = status['power']
	setTemp = status['setTemp']
	currentTemp = status['temp']
	datetime = status['datetime']
	return dict(history=historyList, mode=mode, power=power, temp=currentTemp, setTemp=setTemp, datetime = str(datetime))
#	return dict(power=power, temp=currentTemp, setTemp=setTemp, datetime = str(datetime))
	
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/temp', methods=['GET','PUT','POST'])
def temp():
	if request.method in ('PUT',"POST"):
		with open(statusFile, 'r') as f:
		    status = json.load(f)
		currentTemp = status['temp']
		setTemp = request.args.get('setTemp')
		package = jsonify(method=request.method, temp=currentTemp, setTemp=setTemp)
		logging.info(str(request.method)+","+str(currentTemp)+","+str(setTemp))
		print setTemp
                configPackage = {'setTemp': int(setTemp), 'mode':'heat'}
		
                data = {}
                config = {}
                with open(configFile) as c:
                    try:
                        data = json.load(c)
                        data["setTemp"] = int(setTemp)
                        
                    except ValueError:
                        data = {}
                        data.update(configPackage)
                with open(configFile, 'w') as h:
                    json.dump(data,h)
                    
                
                return package
	else:
                config = {}
		with open(statusFile, 'r') as f:
		    status = json.load(f)
                with open(configFile, 'r') as c:
                    config = json.load(c) 
		power = status['power']
		setTemp = status['setTemp']
		currentTemp = status['temp']
		datetime = status['datetime']
                mode = str(config['mode'])
		package = jsonify(method=request.method, mode=mode, temp=currentTemp, setTemp=setTemp, datetime=datetime, power=power)
		logging.info(str(request.method)+","+str(currentTemp)+","+str(setTemp))
		return package



@app.route('/log', methods=['GET','PUT','POST'])
def log():
	if request.method in ('GET'):
		with open(historyFile, 'r') as f:
		    status = (f.read())
		return status
#		currentTemp = status['temp']
#		setTemp = request.args.get('setTemp')
#		package = jsonify(method=request.method, temp=currentTemp, setTemp=setTemp)
#		logging.info(str(request.method)+","+str(currentTemp)+","+str(setTemp))
#		print setTemp
#		configPackage = {'setTemp': int(setTemp)}
#		with open(configFile, 'w') as f:
#			json.dump(configPackage, f)
#		return package

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80)



