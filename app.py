from flask import Flask
from flask import render_template
from flask import request, redirect

# Twilio API
from twilio.rest import TwilioRestClient
ACCOUNT_SID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
AUTH_TOKEN =  'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Flask app
app = Flask(__name__)
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

# Twilio number
twilio_number = "+1XXXXXXXXXXXXX" 

# App exectution 
@app.route("/") 
def main():
    return render_template('form.html')

# Receiver's number and app outgoing message 
@app.route("/submit-form/", methods = ['POST'])
def submit_number():
    number = request.form['number']
    formatted_number = "+1" + number 
    client.sms.messages.create(to=formatted_number, from_ = twilio_number, body = "This is a test message from Surya's Twilio app. Feel free to reply!") 
    return redirect('/messages/')

# Incoming messages 
@app.route("/messages/")
def list_messages():
    messages = client.sms.messages.list(to=twilio_number)
    return render_template('messages.html', messages = messages)

# Command line exexution 
if __name__ == '__main__': 
    app.run("0.0.0.0", port = 3000, debug = True)
