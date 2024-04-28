import sys
import json
import gateway_scripts.heartbeat
import gateway_scripts.identify

def connect(ws):
    heartbeat_interval_set = False
    identified = False

    while True:
        try:
            response = ws.recv()

            if response == '':
                print('Connection to gateway was lost')
            else:
                response = json.loads(response)

                if not heartbeat_interval_set:
                    heartbeat_interval_set = gateway_scripts.heartbeat.initiate_heartbeat_thread(ws, response)

                if not identified and heartbeat_interval_set == True:
                    identified = gateway_scripts.identify.identify(ws, response)

        except Exception as ex:
            print(type(ex).__name__, '–', ex)
            print('Something went wrong. Make sure that bot token and gateway are correct')
            sys.exit(1)
