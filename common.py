# common.py
import os
import sys
import random
import re
import time
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), "backend"))

from backend.bots.MythBustingScientistBot import MythBustingScientistBot
from backend.bots.SourceDissectorBot import SourceDissectorBot
from backend.bots.HistoricalEchoBot import HistoricalEchoBot
from backend.bots.ParodyAnalogyBot import ParodyAnalogyBot
from backend.bots.SocraticQuestionBot import SocraticQuestionBot

def classify_prompt_with_ollama(prompt, model_name="llama3.1:8b"):
    """
    Calls Ollama to classify prompt text into a category.
    Fallback to ParodyAnalogyBot on error.
    """
    try:
        import ollama  # import here to avoid potential circular dependencies
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
    Decides which bot to use based on classification or keywords.
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
        # Fallback bot
        return ParodyAnalogyBot(model=model_name)