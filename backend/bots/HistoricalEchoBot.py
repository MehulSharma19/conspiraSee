# backend/bots/HistoricalEchoBot.py

from backend.bots.CounterNarrativeBot import CounterNarrativeBot
from typing import Any

class HistoricalEchoBot(CounterNarrativeBot):
    """
    A counter-narrative bot that draws parallels between modern theories and past debunked conspiracies.
    """
    def create_prompt(self, title: str, body: str) -> str:
        prompt = (
            f"Respond with parallels between my theory and debunked past conspiracies in a conversational way.\n"
            f"Your response should include:\n"
            f"- A parallel between my theory and debunked historical conspiracies.\n"
            f"- The strongest example that challenges the idea in a non-confrontational but thought-provoking way (limit to one example).\n\n"
            f"Guidelines:\n"
            f"- Do NOT use anthropomorphic language (e.g., ‘friend’).\n"
            f"- Do NOT reuse any part of this prompt in your response.\n\n"
            f"Statement Title: {title}\n"
            f"Statement: {body}\n\n"
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
        import ollama  # To avoid circular dependencies if needed
        return ollama.chat(**payload)

# For testing purposes only (comment out in prod):
# if __name__ == "__main__":
#     bot = HistoricalEchoBot(model="your_model_name_here")
#     body = "The AI singularity is coming soon, and once machines surpass human intelligence, they will take over the world!"
#     response = bot.get_response(body)
#     print("Generated Response:", response)