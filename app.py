import meraki
import requests
import time
import os
from flask import Flask, request
from dotenv import load_dotenv

# load all environment variables, make sure to create a .env file!
load_dotenv()

# Can use this Meraki SDK for other meraki related calls!
dashboard = meraki.DashboardAPI(os.environ['MERAKI_API_TOKEN'], output_log=False, print_console=False)
app = Flask(__name__)

# Helpers
def triggerAlexaOffRoutine():
    url = "https://api-v2.voicemonkey.io/trigger"
    params = {'token':os.environ['ROUTINE_API_TOKEN'],'device':'mt30'}

    requests.get(url, params=params)
    return

def triggerAlexaWhiteRoutine():
    url = "https://api-v2.voicemonkey.io/trigger"
    params = {'token':os.environ['ROUTINE_API_TOKEN'],'device':'mt30-long'}

    requests.get(url, params=params)
    return


@app.route("/meraki_webhook", methods=["POST"])
def handle_meraki_event():
    if request.method == 'POST':
        #debug print
        print(request.json)
        print("Received POST event")

        button_name = request.json['deviceName']
        # button_serial = request.json['deviceSerial']
        # device_url = request.json['deviceUrl']
        button_press_type = ''
        try:
            # message = request.json['alertData']['message']
            button_press_type = request.json['alertData']['trigger']['button']['pressType']

        except KeyError:
            message = ''
        
        if button_press_type == 'short':
            print("Button Name: " + button_name + "\n")
            print('SHORT BUTTON PRESS')

            triggerAlexaOffRoutine()

            return 'Meraki Button - Short Webhook Test'
        elif button_press_type == 'long':
            print("Button Name: " + button_name + "\n")
            print('LONG BUTTON PRESS')

            triggerAlexaWhiteRoutine()

            return 'Meraki Button - Long Webhook Test'
        else:
            print('TESTS MERAKI DASHBOARD WEBHOOK')
            return 'Meraki Button - Webhook Test'
    return


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)