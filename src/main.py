import os
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv 
# import json to load JSON data to a python dictionary 
import json 
  
# urllib.request to make a request to api 
import urllib.request 
  

load_dotenv()

  
app = Flask(__name__) 
app.config['SECRET_KEY'] = os.urandom(32)


def celcius(temp):
	return int(temp) - 273
  
@app.route('/', methods =['POST', 'GET']) 
def weather(): 
	global source


	if request.method == 'POST': 
		city = request.form['city'] 
	else: 
		# for default name Andijan
		city = 'Andijan'
	# your API key will come here 

	api = '0e4b23dd401f1441ff166699de6b225b'
	# source contain json data from api 
	try:
		source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api).read() 
	except urllib.error.HTTPError:
		flash("Incorrect city name! Try again.")
	# converting JSON data to a dictionary 
	list_of_data = json.loads(source)

	# data for variable list_of_data 
	data = { 
		"country_code": str(list_of_data['sys']['country']),
		"cityname": str(city), 
		"coordinate": str(list_of_data['coord']['lon']) + ' ' 
					+ str(list_of_data['coord']['lat']), 
		"temp": str(list_of_data['main']['temp']) + 'K°',
		"temp_cel": str(int(list_of_data['main']['temp']) - 273) + 'C°',
		"pressure": str(list_of_data['main']['pressure']), 
		"humidity": str(list_of_data['main']['humidity']), 
    }

	return render_template('index.html', data = data) 