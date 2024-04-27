from dotenv import load_dotenv
import os
import json

load_dotenv()

TOKEN = os.getenv('TOKEN')

PAYLOAD = {
    'op': 2,
    'd': {
        'token': TOKEN,
        'intents': 513,
        'properties': {
            'os': 'macos',
            'browser': 'disco',
            'device': 'disco',
        }
    }    
}

def identify(connection, response):
    print('Identifying...')
    try:
        if 'op' in response and response['op'] == 11:
            jsonMessage = json.dumps(PAYLOAD)
            connection.send(jsonMessage)
            
            response = json.loads(connection.recv())

            if 't' in response and response['t'] == 'READY':
                print('Identified')
                return True

            print('Not identified')
            return False
    except RuntimeError:
        print('Could not identify. Make sure bot token is correct.')
