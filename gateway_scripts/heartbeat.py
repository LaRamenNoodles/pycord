import json
from threading import Timer

def get_payload(response): 
    return {
        'op': 1,
        'd': response['s'],
    }

def send_heartbeat(connection, response):
    print('Sending heartbeat...')
    try:
        jsonMessage = json.dumps(get_payload(response))
        connection.send(jsonMessage)
    except Exception:
        print('Something went wrong while sending heartbeat')

def initiate_heartbeat_thread(connection, response):
    try:
        if 'd' in response and response['d'] is not None and 'heartbeat_interval' in response['d']:
            hbInterval = response['d']['heartbeat_interval']

            send_heartbeat(connection, response)

            hbProcess = Timer(hbInterval / 1000.0, send_heartbeat, [connection, response])
            hbProcess.start()

            return True
    except Exception:
        print('Something went wrong while initiating heartbeat thread')
