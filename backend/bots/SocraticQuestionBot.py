# backend/bots/SocraticQuestionBot.py

from backend.bots.CounterNarrativeBot import CounterNarrativeBot
from typing import Any

class SocraticQuestionBot(CounterNarrativeBot):
    """
    A counter-narrative bot that responds to statements in the style of Socrates, using reflection and thoughtful questioning.
    """
    def create_prompt(self, title: str, body: str) -> str:
        prompt = (
            f"Respond as Socrates to my statement.\n"
            f"Your response should include:\n"
            f"1. A Socratic reflection on the claim.\n"
            f"2. No more than two questions that challenge the idea in a non-confrontational but thought-provoking way.\n"
            f"3. At the end of the response, include a clearly labeled 'Transparency Note' indicating that the response is AI-generated, along with a brief explanation of the bot’s purpose.\n\n"
            f"Guidelines:\n"
            f"- Do NOT use anthropomorphic language (e.g., ‘friend’).\n"
            f"- Keep the tone philosophical, guiding the user toward deeper reasoning.\n\n"
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
        import ollama  # To avoid circular dependencies if needed
        return ollama.chat(**payload)

# For testing purposes only (comment out in prod):
# if __name__ == "__main__":
#     bot = SocraticQuestionBot(model="your_model_name_here")
#     title = "AI will soon surpass all human intelligence"
#     body = "Machines are evolving so rapidly that humans will become obsolete."
#     response = bot.get_response(title, body)
#     print("Generated Response:", response)