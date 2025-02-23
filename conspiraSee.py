from flask import Flask, request, render_template, send_from_directory
import sys
import os
import re
import random
import time

# Import all bots (and any you need):
from backend.bots.MythBustingScientistBot import MythBustingScientistBot
from backend.bots.SourceDissectorBot import SourceDissectorBot
from backend.bots.HistoricalEchoBot import HistoricalEchoBot
from backend.bots.ParodyAnalogyBot import ParodyAnalogyBot
from backend.bots.SocraticQuestionBot import SocraticQuestionBot

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static/images', 'dinosaur.svg', mimetype='image/svg+xml')

def classify_prompt_with_ollama(prompt, model_name="llama3.1:8b"):
    try:
        import ollama
        payload = {
            "model": model_name,
            "messages": [{"role": "user", "content": prompt}],
        }
        response = ollama.chat(**payload)
        classification = response["message"]["content"].strip()
        return classification
    except Exception as e:
        print(f"Error calling Ollama model: {e}")
        return "ParodyAnalogyBot"

def expert_selection(title, body, model_name="mistral"):
    """
    A simplified classification approach,
    returning a bot instance based on detected keywords.
    """
    prompt = (
        f"Title: {title}\n"
        f"Body: {body}\n\n"
        "Classify the above text into one of the following categories, based on these keywords:\n"
        "- MythBustingScientist: debunk, science, experiment, fact-check, myth\n"
        "- SourceDissector: source, evidence, verify, analyze, research\n"
        "- HistoricalEcho: history, past, legacy, echo, tradition\n"
        "- ParodyAnalogy: parody, humor, analogy, satire, creative twist\n"
        "- SocraticQuestion: question, inquiry, dialectic, provoke, explore\n\n"
        "Provide only the category name."
    )
    
    classification = classify_prompt_with_ollama(prompt)
    print(f"[expert_selection] Classification: {classification}")
    
    if classification == "MythBustingScientist":
        return MythBustingScientistBot(model=model_name)
    elif classification == "SourceDissector":
        return SourceDissectorBot(model=model_name)
    elif classification == "HistoricalEcho":
        return HistoricalEchoBot(model=model_name)
    elif classification == "ParodyAnalogy":
        return ParodyAnalogyBot(model=model_name)
    elif classification == "SocraticQuestion":
        return SocraticQuestionBot(model=model_name)
    else:
        return ParodyAnalogyBot(model=model_name)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    user_text = request.form.get("text_input", "").strip()
    selected_bot = request.form.get("bot_choice", "mixture")
    model_name = "mistral"

    if selected_bot == "MythBustingScientist":
        bot = MythBustingScientistBot(model=model_name)
    elif selected_bot == "SourceDissector":
        bot = SourceDissectorBot(model=model_name)
    elif selected_bot == "HistoricalEcho":
        bot = HistoricalEchoBot(model=model_name)
    elif selected_bot == "ParodyAnalogy":
        bot = ParodyAnalogyBot(model=model_name)
    elif selected_bot == "SocraticQuestion":
        bot = SocraticQuestionBot(model=model_name)
    else:
        bot = expert_selection("", user_text, model_name=model_name)

    response = bot.get_response("", user_text)
    return render_template("result.html", result=response)

@app.route("/health", methods=["GET"])
def health_check():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)