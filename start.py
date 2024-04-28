import gateway_scripts.initiate_connection
import os
from websocket import create_connection
from dotenv import load_dotenv

load_dotenv()

GATEWAY = os.getenv('GATEWAY')

ws = create_connection(GATEWAY)

gateway_scripts.initiate_connection.connect(ws)
