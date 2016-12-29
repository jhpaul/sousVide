import control
import tempRead
from flask import Flask
from flask import request,flash,redirect,url_for,render_template,jsonify
import time
import sys

try:
	app = Flask(_name_)
	
	@app.context_processor
	def util():
		def tempRead():
			return str(tempRead.read_temp())	
