import sys
import json
import gateway_scripts.heartbeat
import gateway_scripts.identify
from cache.resume_cache import cache
import json
from dotenv import load_dotenv
from websocket import create_connection
import os

def connect(ws):
    heartbeat_interval_set = False
    identified = False

    while True:
        try:
            response = ws.recv()
            print('RECEIVED: ', response)
            if response == '':
                resume_connection(ws)
            else:
                response = json.loads(response)
                opCode = response['op']

                match opCode:
                    case 0:
                        cache['last_event_id'] = response['s']
                    case 7, 4000, 4007, 4009: 
                        resume_connection(ws)                    
                    case 9 if response['d'] == True:
                        resume_connection(ws)
                    
                if not heartbeat_interval_set:
                    heartbeat_interval_set = gateway_scripts.heartbeat.initiate_heartbeat_thread(ws, response)

                if not identified and heartbeat_interval_set == True:
                    identified = gateway_scripts.identify.identify(ws, response)

        except Exception as ex:
            print(type(ex).__name__, '–', ex)
            print('Something went wrong. Make sure that bot token and gateway are correct')
            sys.exit(1)

def resume_connection(ws):
    ws = create_connection(cache['resume_gateway_url'])
    
    payload = {
        'op': 6,
        'd': {
            'token': os.getenv('TOKEN'),
            'session_id': cache['session_id'],
            'seq': cache['last_event_id'],
        }
    }

    ws.send(json.dumps(payload))

    response = json.loads(ws.recv())

    if response['op'] == 9 and response['d'] == False:
        ws.close()

        ws = create_connection(os.getenv('GATEWAY'))
        identified = False

        connect(ws)
    else:
        connect(ws)
