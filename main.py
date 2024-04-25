from flask import Flask, request, render_template
from app_config import app, twilio_client

@app.route('/')
def index():
    return 'Welcome to SMS App!'

@app.route('/send_sms', methods=['GET', 'POST'])
def send_sms():
    if request.method == 'POST':
        recipient_number = request.form.get('recipient_number')
        message_body = request.form.get('message_body')

        if recipient_number is None or message_body is None:
            return 'Invalid request: recipient_number or message_body missing', 400

        # Send SMS
        message = twilio_client.messages.create(
            body=message_body,
            from_=app.config['TWILIO_PHONE_NUMBER'],
            to=recipient_number
        )

        return f'SMS sent to {recipient_number}'
    
    # If it's a GET request, render the send_sms.html template
    return render_template('send_sms.html')

if __name__ == '__main__':
    app.run(debug=True)
