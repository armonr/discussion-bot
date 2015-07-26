import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

DISCUSSION_API_SCHEME = 'http://'
DISCUSSION_API_HOST = 'localhost'
DISCUSSION_API_PORT = 8080
DISCUSSION_API_PATH = ''  # Path to the API. Leave empty if root

SLACK_TOKEN = None  # Add slack token here
SLACK_CHANNEL = 'discussion-bot'
SLACK_BOT_USERNAME = 'wikia discussions bot'
