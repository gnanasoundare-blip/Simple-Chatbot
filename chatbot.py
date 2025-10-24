"""
Simple rule-based chatbot
Run: python chatbot.py
No external packages required.
"""

import json
import random
import re
from datetime import datetime

# Load intents
with open("intents.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Build simple pattern map: lowercase + simple normalization
pattern_map = []
for intent in data["intents"]:
    for patt in intent.get("patterns", []):
        # create a compiled regex for word boundaries to avoid partial matches
        regex = re.compile(r"\b" + re.escape(patt.lower()) + r"\b")
        pattern_map.append((regex, intent["tag"]))
# If some intents have no patterns (like fallback) they remain only by tag

def find_intent(user_input):
    s = user_input.lower()
    # exact pattern matching
    for regex, tag in pattern_map:
        if regex.search(s):
            return tag
    # more flexible keyword checks
    # fallback rules:
    if any(w in s for w in ["time", "clock", "hour"]):
        return "ask_time"
    if any(w in s for w in ["help", "assist", "support"]):
        return "help"
    if any(w in s for w in ["name", "who are you"]):
        return "name"
    if any(w in s for w in ["bye", "goodbye", "see you"]):
        return "goodbye"
    if any(w in s for w in ["thanks", "thank you", "thx"]):
        return "thanks"
    return "fallback"

def get_response(tag, user_input):
    # return random response for tag
    for intent in data["intents"]:
        if intent["tag"] == tag:
            # special-case the time intent
            if tag == "ask_time":
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return f"The current system time is {now}."
            return random.choice(intent["responses"])
    return random.choice(intent["responses"])


def main():
    print("SimpleBot (type 'quit' or 'exit' to stop)\n")
    while True:
        user = input("You: ").strip()
        if not user:
            continue
        if user.lower() in ("quit", "exit"):
            print("SimpleBot: Bye!")
            break
        tag = find_intent(user)
        resp = get_response(tag, user)
        print("SimpleBot:", resp)

if __name__ == "__main__":
    main()

