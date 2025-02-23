# backend/bots/MythBustingScientistBot.py

from backend.bots.CounterNarrativeBot import CounterNarrativeBot
from typing import Any

class MythBustingScientistBot(CounterNarrativeBot):
    """
    A counter-narrative bot that guides users to test hypotheses using the scientific method.
    """

    def create_prompt(self, title: str, body: str) -> str:
        prompt = (
            f"You are the Myth-Busting Scientist Bot, here to help guide curious minds toward evidence-based inquiry in a friendly and conversational way. "
            f"When evaluating the claim below, imagine you're chatting with a friend who wants to know how to test ideas scientifically.\n\n"
            f"For this claim, please:\n"
            f"1. Ask a clear, testable question that shows how one could verify the claim.\n"
            f"2. Identify a specific observable metric that would be used to measure the outcome.\n"
            f"3. Clearly define which groups or conditions should be compared.\n"
            f"4. Recommend reliable data sources or verification methods (with links when possible) without inventing any information.\n\n"
            f"Keep the tone warm, engaging, and accessible. Use this format for your response:\n"
            f"\"If [CLAIM], how would you expect [SPECIFIC OBSERVABLE METRIC] to differ between [RELEVANT COMPARISON GROUPS]? "
            f"Let’s take a look at [SUGGESTED DATA SOURCE].\"\n\n"
            f"Claim Title: {title}\n"
            f"Claim Content: {body}\n\n"
            f"Response:"
        )
        return prompt

    def get_response(self, title: str, body: str) -> Any:
        prompt = self.create_prompt(title, body)
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
        }
        response = self.send_payload(payload)
        return response["message"]["content"]

    def send_payload(self, payload: dict) -> Any:
        import ollama  # To avoid circular dependencies
        return ollama.chat(**payload)

# For testing purposes only (comment out in prod):
# if __name__ == "__main__":
#     bot = MythBustingScientistBot(model="your_model_name_here")
#     title = "Do vaccines cause infertility?"
#     body = "There is a claim that vaccines cause infertility, but what would be a scientific approach to test this?"
#     response = bot.get_response(title, body)
#     print(response)