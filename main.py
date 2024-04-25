# main.py

from flask import Flask, request
from app_config import app, twilio_client

@app.route('/')
def index():
    return 'Welcome to SMS App!'

@app.route('/send_sms', methods=['POST'])
def send_sms():
    recipient_number = request.form['recipient_number']
    message_body = request.form['message_body']

    # Send SMS
    message = twilio_client.messages.create(
        body=message_body,
        from_=app.config['TWILIO_PHONE_NUMBER'],
        to=recipient_number
    )

    return f'SMS sent to {recipient_number}'

if __name__ == '__main__':
    app.run(debug=True)
