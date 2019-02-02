#!/usr/bin/python

#import module
from bs4 import BeautifulSoup
import re
import requests
import time
import urllib
from flask import Flask,request,render_template
#------------------------------------end-------------------------------------------------------
app = Flask(__name__)


@app.route("/",methods=['GET', 'POST'])

def index():
	if request.method=='GET':
		
		return render_template("index.html")
	elif request.method=='POST':
		my_headers = {'user-agent' : 'Mozilla/11.0'}
		get1 = requests.get("https://www.google.com/search?q="+request.form['dork']+"&start=10",headers = my_headers).text
		get2 = requests.get("https://www.google.com/search?q="+request.form['dork']+"&start=20",headers = my_headers).text
		get3 = requests.get("https://www.google.com/search?q="+request.form['dork']+"&start=30",headers = my_headers).text

		scrap1 = BeautifulSoup(get1,'html.parser')
		scrap2 = BeautifulSoup(get2,'html.parser')
		scrap3 = BeautifulSoup(get3,'html.parser')

		hasil = []
		for x1 in scrap1.find_all('h3' ,class_='r'):
			hasil1 = re.findall("url\?q=(.+?)\&sa", x1.a['href'])
			for h1 in hasil1:
				hasil.append(h1)
				time.sleep(0.5)

		for x2 in scrap2.find_all('h3' ,class_='r'):
			hasil1 = re.findall("url\?q=(.+?)\&sa", x2.a['href'])
			for h2 in hasil1:
				hasil.append(h2)
				time.sleep(0.5)
		for x3 in scrap2.find_all('h3' ,class_='r'):
			hasil1 = re.findall("url\?q=(.+?)\&sa", x3.a['href'])
			for h3 in hasil1:
				hasil.append(h3)
				time.sleep(0.5) 
		dk = ['inurl','intext','site']
		for ilegal in dk :
			if ilegal in request.form['dork']:
				return "Captcha is active !!, don't use "+ilegal+" to bypass it\n"+get1
			elif (len(hasil) == 0 ):
				return "google captcha blocked this action <a href=''>back</a>\n"+get1
			else:
				return render_template("hasil.html", hasil = hasil) 
if __name__ == "__main__":
	app.run(port = "31337",debug=True)