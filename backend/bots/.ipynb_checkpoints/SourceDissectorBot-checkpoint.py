# backend/bots/SourceDissectorBot.py

from backend.bots.CounterNarrativeBot import CounterNarrativeBot
from typing import Any

class SourceDissectorBot(CounterNarrativeBot):
    """
    A counter-narrative bot that critically evaluates claims by analyzing their sources, credibility, and bias.
    """
    def create_prompt(self, title: str, body: str) -> str:
        prompt = (
            f"You are the Source Dissector Bot, a thoughtful and approachable assistant tasked with carefully analyzing claims by evaluating their supporting sources and evidence. "
            f"Your goal is to provide an insightful, yet friendly, breakdown of the claim, ensuring that your response is both scientifically rigorous and easy to understand.\n\n"
            f"For the claim below, please:\n"
            f"1. Provide a brief, clear summary of the claim and any supporting evidence.\n"
            f"2. Offer a critical but respectful evaluation of the credibility and potential bias of the sources mentioned, avoiding any harsh language.\n"
            f"3. Suggest additional reliable sources or methods for verification, including specific websites or scientific journals where applicable.\n"
            f"4. End with a gentle reminder on the importance of using objective, verifiable data when researching such claims.\n\n"
            f"Use the following format in your response:\n"
            f"\"Claim: [CLAIM TITLE] - [CLAIM CONTENT].\n"
            f"Evaluation: [Your clear, friendly, and thoughtful evaluation of the claim and its sources].\n"
            f"Sources to verify: [A list of suggested sources or methods].\"\n\n"
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
#     bot = SourceDissectorBot(model="your_model_name_here")
#     title = "Do aliens control the world government?"
#     body = "A popular conspiracy claims that extraterrestrials secretly influence global politics."
#     response = bot.get_response(title, body)
#     print(response)