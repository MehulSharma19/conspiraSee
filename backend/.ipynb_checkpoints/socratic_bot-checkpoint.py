from openai import OpenAI
import random

# OpenAI API Key (replace with your own)
API_KEY = "your_openai_api_key"

# Predefined Socratic question templates
SOCRATIC_QUESTIONS = [
    "What evidence would convince you otherwise?",
    "How do you think this information is verified?",
    "Have you considered alternative explanations?",
    "What would happen if this theory were wrong?"
]

client = OpenAI(api_key=API_KEY)

def generate_socratic_question(post_text):
    """Returns a Socratic question based on the conspiracy post."""
    return random.choice(SOCRATIC_QUESTIONS)

if __name__ == "__main__":
    post = "5G is a government mind-control experiment!"
    question = generate_socratic_question(post)
    print("Generated Socratic Question:", question)