import requests
import json

webhook = "https://hooks.slack.com/services/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"

def send_message(message_text):

    r = requests.post(webhook, json={"text": message_text})
    return ()
