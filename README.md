# Simple-Chatbot
Simple rule-based chatbot demo.


A tiny **rule-based chatbot** built entirely in **Python**, designed as a quick project to demonstrate basic programming, logical structuring, and GitHub usage. 

(This repo demonstrates foundational skills: Python scripting, JSON-driven intent structure, and GitHub project setup. It's small by design — ready to extend with ML or a web UI.)

---

## What It Does
- Recognizes a few basic *intents* such as greeting, asking for help, or saying goodbye.  
- Responds with simple pre-defined answers stored in a JSON file.  
- Demonstrates how chatbots work at a fundamental level — through *pattern matching* instead of machine learning.  
- Built to be small, clear, and easy to extend later with NLP or ML features.

---

## Project Files
| File | Description |
|------|--------------|
| `chatbot.py` | Main Python script that runs the chatbot |
| `intents.json` | Contains the chatbot’s intents, patterns, and responses |
| `requirements.txt` | Lists any required packages (none for now) |
| `.gitignore` | Tells GitHub to ignore unnecessary files like `__pycache__` |
| `LICENSE` | MIT license allowing open-source use |

---

## How to Run
1. Make sure you have **Python 3.8+** installed.  
2. Download or clone this repository.  
3. Open the project folder in your terminal or command prompt.  
4. Run:
   ```bash
   python chatbot.py

## Some prompts you can try:
"hi", "hello", "hey", "good morning", "good evening", "yo", "hola", 

"how are you", "how are you doing", "how do you feel", 

"what is your name", "who are you", "your name",

"who created you", "who made you", "your creator", "who built you",

"what's the weather", "weather today", "is it hot", "is it raining",

"i'm happy", "feeling good", "i feel great", "i'm fine", 

"i'm sad", "i feel bad", "i'm depressed", "i feel lonely",

"tell me a joke", "make me laugh", "say something funny",

"thanks", "thank you", "appreciate it",

"bye", "goodbye", "see you", "later", "exit", "quit"



