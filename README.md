### cmxreceiver-python
# NodeJS CMX Receiver

### A basic web service to accept CMX data from a Cisco Meraki network
- Accept a GET request from Meraki and respond with a validator
- Meraki will POST to server, if validated.
- POST will contain a secret, which can be verified by the server.
- JSON data will be in the req.body.data. This will be available in the cmxData function's data object.

## cmxreceiver.py
-- The basic app will only place the data received on the console. 

## cmxreceiver-mongodb.py
-- Extends the basic app by placing data into a local MongoDB database.


## Prerequisites
* Flask must be installed
http://flask.pocoo.org/docs/0.12/

* Cisco Meraki Network with CMX/Scanning API enabled and configured to point to this server

## Installation and Run
```
$ git clone <<this repo>>
```
### Direct Run with Python3
* Option 1 - Basic Receiver
```
python3 cmxreceiver.py -v <validator> -s <secret>'
```
* Option 2 - Receiver with MongoDB
```
python3 cmxreceiver.py-mongodb.py -v <validator> -s <secret>'
```

### Via Flask
* Option 1 - Basic Receiver
```
export FLASK_APP=cmxreceiver.py -v yourValidatorKey -s yourSecret
flask run -h 0.0.0.0
 * Running on http://0.0.0.0:5000/
```
* Option 2 - Receiver with MongoDB
```
export FLASK_APP=cmxreceiver-mongodb.py -v yourValidatorKey -s yourSecret
flask run -h 0.0.0.0
 * Running on http://0.0.0.0:5000/
```

## Defaults
* Port: 5000
* CMX Post URL: http://yourserver:5000/

## TIP
* use ngrok to expose port 5000
```
ngrok http 5000
```
Then use the new url it creates as your base URL. `https://2a6eed03.ngrok.io/`



# Cisco Meraki CMX Location API Documentation
https://documentation.meraki.com/MR/Monitoring_and_Reporting/CMX_Analytics#CMX_Location_API




### Written by Cory Guynn
2016

http://www.InternetOfLEGO.com
http://Developers.Meraki.com
