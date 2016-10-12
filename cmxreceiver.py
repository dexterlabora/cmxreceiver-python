#!flask/bin/python

"""
Cisco Meraki CMX Receiver

A simple example demonstrating how to interact with the CMX API.

How it works:
- Meraki access points will listen for WiFi clients that are searching for a network to join and log the events.
- The "observations" are then collected temporarily in the cloud where additional information can be added to
the event, such as GPS, X Y coordinates and additional client details.
- Meraki will first send a GET request to this CMX receiver, which expects to receieve a "validator" key that matches
the Meraki network's validator.
- Meraki will then send a JSON message to this application's POST URL (i.e. http://yourserver/ method=[POST])
- The JSON is checked to ensure it matches the expected secret, version and observation device type.
- The resulting data is sent to the "save_data(data)" function where it can be sent to a databse or other service
    - This example will simply print the CMX data to the console.

Default port: 5000

Cisco Meraki CMX Documentation
https://documentation.meraki.com/MR/Monitoring_and_Reporting/CMX_Analytics#CMX_Location_API

Written by Cory Guynn
2016

www.InternetOfLEGO.com
Developers.Meraki.com
"""

# Libraries
from pprint import pprint
from flask import Flask
from flask import json
from flask import request

# MERAKI SETTINGS
validator = "8e0846499d9a3f6c23f7868c4c25b9d6325035f5"
secret = "supersecret"
version = "2.0" # This code was written to support the JSON version specified

# Save CMX Data
def save_data(data):
    print("---- SAVING CMX DATA ----")
    # CHANGE ME - send 'data' to a database or storage system
    pprint(data, indent=1)

app = Flask(__name__)


###################################

# Respond to Meraki with validator
@app.route('/', methods=['GET'])
def get_validator():
    print("validator sent to: ",request.environ['REMOTE_ADDR'])
    return validator

# Accept CMX JSON POST
@app.route('/', methods=['POST'])
def get_cmxJSON():
    if not request.json or not 'data' in request.json:
        return("invalid data",400)
    cmxdata = request.json
    #pprint(cmxdata, indent=1)
    print("Received POST from ",request.environ['REMOTE_ADDR'])

    # Verify secret
    if cmxdata['secret'] != secret:
        print("secret invalid:", cmxdata['secret'])
        return("invalid secret",403)
    else:
        print("secret verified: ", cmxdata['secret'])

    # Verify version
    if cmxdata['version'] != version:
        print("invalid version")
        return("invalid version",400)
    else:
        print("version verified: ", cmxdata['version'])

    # Determine device type
    if cmxdata['type'] == "DevicesSeen":
        print("WiFi Devices Seen")
    elif cmxdata['type'] == "BluetoothDevicesSeen":
        print("Bluetooth Devices Seen")
    else:
        print("Unknown Device 'type'")
        return("invalid device type",403)

    # Do something with data (commit to database)
    save_data(cmxdata)

    # Return success message
    return "CMX POST Received"

if __name__ == '__main__':
    app.run(debug=True)
