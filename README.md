
# SMS App

SMS App is a Flask-based web application for sending SMS messages using Twilio.

## Features

-   Send SMS messages to any phone number
-   Easy-to-use web interface
-   Error handling for missing recipient number or message body
-   Configurable Twilio phone number

## Installation

1.  Clone the repository:
    
    bash
    
    Copy code
    
    `https://github.com/basiliohadnan/sun-alert.git` 
    
2.  Install dependencies:
    
    bash
    
    Copy code
    
    `pip install -r requirements.txt` 
    
3.  Set up your Twilio account and obtain your account SID, auth token, and phone number.
    
4.  Copy the `.env.example` file to `.env` and update it with your Twilio credentials and phone number:
    
    makefile
    
    Copy code
    
    `TWILIO_ACCOUNT_SID=your_account_sid
    TWILIO_AUTH_TOKEN=your_auth_token
    TWILIO_PHONE_NUMBER=your_phone_number` 
    

## Usage

1.  Run the Flask application:
    
    bash
    
    Copy code
    
    `python main.py` 
    
2.  Access the application in your web browser at `http://localhost:5000`.
    
3.  Enter the recipient's phone number and the message body, then click "Send SMS" to send the message.
    

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.
