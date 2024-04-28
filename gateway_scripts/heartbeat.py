import json
from threading import Timer

def get_payload(response): 
    return {
        'op': 1,
        'd': response['s'],
    }

def initiate_heartbeat_thread(connection, response):
    try:
        if response['op'] == 10:
            send_heartbeat(connection, response)

            return True
    except Exception:
        print('Something went wrong while initiating heartbeat thread')

def send_heartbeat(connection, response):
    print('Sending heartbeat...')
    try:
        hbInterval = response['d']['heartbeat_interval']
        jsonMessage = json.dumps(get_payload(response))

        connection.send(jsonMessage)

        hbProcess = Timer(hbInterval / 1000.0, send_heartbeat, [connection, response])
        hbProcess.start()
    except Exception:
        print('Something went wrong while sending heartbeat')
