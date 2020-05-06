from slack import WebClient
import os

def post(text, channel='#maejima-dev'):
    client = WebClient(token=os.environ['SLACK_API_TOKEN'])
    client.chat_postMessage(
        channel=channel,
        text=text)
