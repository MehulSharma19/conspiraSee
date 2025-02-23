# backend/bots/ParodyAnalogyBot.py

from backend.bots.CounterNarrativeBot import CounterNarrativeBot
from typing import Any

class ParodyAnalogyBot(CounterNarrativeBot):
    """
    A counter-narrative bot that responds to conspiracy theories with absurd yet thought-provoking analogies.
    """
    def create_prompt(self, title: str, body: str) -> str:
        prompt = (
            f"Respond with one absurd analogy to highlight logical flaws in my conspiracy theory in a conversational way.\n"
            f"Use humor to disarm defensiveness while keeping the response non-confrontational but thought-provoking.\n\n"
            f"Guidelines:\n"
            f"- Do NOT use anthropomorphic language (e.g., ‘friend’).\n"
            f"- Ensure the analogy is creative but relevant to the logic of the claim.\n\n"
            f"- Make your response funny and draw a parallel absurd so the user finds it relevant.\n\n"
            f"Statement Title: {title}\n"
            f"Statement Content: {body}\n\n"
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
        import ollama  # Import here to avoid circular dependencies if needed
        return ollama.chat(**payload)

# For testing purposes only (comment out in prod):
# if __name__ == "__main__":
#     bot = ParodyAnalogyBot(model="your_model_name_here")
#     title = "The moon landing was fake"
#     body = "The government staged the moon landing in a Hollywood studio."
#     response = bot.get_response(title, body)
#     print("Generated Response:", response)