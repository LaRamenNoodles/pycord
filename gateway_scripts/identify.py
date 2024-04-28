from dotenv import load_dotenv
import os
import json
from cache.resume_cache import cache

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
    try:
        if response['op'] == 11:
            print('Identifying...')
            jsonMessage = json.dumps(PAYLOAD)
            
            connection.send(jsonMessage)
            
            response = json.loads(connection.recv())

            cache['session_id'] = response['d']['session_id']
            cache['resume_gateway_url'] = response['d']['resume_gateway_url'] + '?v=10&encoding=json'
            cache['last_event_id'] = response['s']

            if response['op'] == 0:
                print('Identified')
                cache['last_event_id'] = response['s']
                return True

            print('Not identified')
            return False
    except Exception:
        print('Could not identify. Make sure bot token is correct.')
