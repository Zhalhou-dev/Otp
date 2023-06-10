# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define route and Verify_otp() function below

def verify_otp():
	username-request.form['username']
	password=request.form['password']
	mobile_number=request.form['number']
	if username=="Zhalhou" and password=="12345":
		Twilio_SID="AC2a4e0722722d55ace198db1858312dd9"
		Twilio_auth_token="a40c3debc16b9ae03e730e02a87b0065"
		client=Client(Twilio_SID,Twilio_auth_token)
		        verification = client.verify \
            .services(Twilio_SID) \
            .verifications \
            .create(to=mobile_number, channel='sms')


		return render_template('home.html')
	else:
		"Entered password or username is wrong"


















if __name__ == "__main__":
    app.run()

