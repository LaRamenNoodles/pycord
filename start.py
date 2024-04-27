import gateway_scripts.identify
import gateway_scripts.heartbeat
import os
import json
import sys
from websocket import create_connection
from dotenv import load_dotenv

load_dotenv()

GATEWAY = os.getenv('GATEWAY')

ws = create_connection(GATEWAY)

heartbeat_interval_set = False
identified = False

while True:
    try:
        response = json.loads(ws.recv())
        print('Received message:', response)

        if not heartbeat_interval_set:
            heartbeat_interval_set = gateway_scripts.heartbeat.initiate_heartbeat_thread(ws, response)

        if not identified and heartbeat_interval_set == True:
            identified = gateway_scripts.identify.identify(ws, response)
    except Exception:
        print('Something went wrong. Make sure that bot token and gateway are correct')
        sys.exit(1)
