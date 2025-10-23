"""
Simple rule-based chatbot
Run: python chatbot.py
No external packages required.
"""

import json
import random
import datetime
import time
from tqdm import tqdm
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama

# Load intents
with open('intents.json', 'r') as file:
    data = json.load(file)

def typing_effect(text, delay=0.02):
    """Creates a typing animation for bot responses."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # New line after text

def match_intent(user_input):
    """Tries to find the best intent match for a given user input."""
    user_input = user_input.lower()
    for intent in data['intents']:
        for pattern in intent['patterns']:
            if pattern in user_input:
                return intent
    return next(i for i in data['intents'] if i['tag'] == 'default')

print(Fore.CYAN + "SimpleBot (type 'quit' or 'exit' to stop)\n")

while True:
    user_input = input(Fore.PURPLE + "You: " + Style.RESET_ALL).strip().lower()
    if user_input in ['quit', 'exit']:
        typing_effect(Fore.CYAN + "SimpleBot: Goodbye! Have a great day! 👋")
        break

    intent = match_intent(user_input)
    response = random.choice(intent['responses'])

    # Insert dynamic time if applicable
    if '{time}' in response:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = response.replace("{time}", current_time)

    # Animated colored bot response
    typing_effect(Fore.BLUE + "SimpleBot: " + response)

