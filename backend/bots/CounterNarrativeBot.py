import ollama

class CounterNarrativeBot:
    def __init__(self, model):
        """
        Initialize the bot with a specific model.
        """
        self.model = model

    def create_prompt(self, title, body):
        """
        Subclasses should override this method to construct a prompt 
        tailored to the specific counter-narrative approach.
        """
        raise NotImplementedError("Subclasses must implement create_prompt method.")

    def get_response(self, title, body):
        """
        Constructs the prompt using the subclass method, sends the payload to Ollama,
        and returns the response.
        """
        prompt = self.create_prompt(title, body)
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
        }
        response = ollama.chat(**payload)
        return response["message"]["content"]