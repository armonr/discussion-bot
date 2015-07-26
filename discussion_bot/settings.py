import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

TRAINING_DATA = os.path.join(APP_ROOT, 'bot_data/train/glee/rachel-berry.txt')

DISCUSSION_API_SCHEME = 'http://'
DISCUSSION_API_HOST = 'localhost'
DISCUSSION_API_PORT = 8080
DISCUSSION_API_PATH = ''  # Path to the API. Leave empty if root

