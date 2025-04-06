import slack
import os
from pathlib import Path
from dotenv import load_dotenv
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
client.chat_postMessage(channel='C08LC55ASKS', text="Working...")

# Keyword set for question detection
# detection_keywords = {"who", "what", "when", "why", "will", "how", "have"}

# Message storage dictionary
messages = {}

def detect_question(text):
    text = text.lower()
    # Rule 1: If it contains a question mark, it's definitely a question
    if "?" in text:
        return True
    return False

def send_message(channel, text):
    client.chat_postMessage(channel=channel, text=text)

