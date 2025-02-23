import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

class ConspiracyDetector:
    def __init__(self, model_path, device='cpu'):
        self.device = torch.device(device)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path+"conspiracy_detector_tokenizer/")
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path+"conspiracy_detector_model/").to(self.device)
        self.model.eval()

    def classify(self, text):
        # Tokenize the text
        inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True)
        inputs = {key: value.to(self.device) for key, value in inputs.items()}

        with torch.no_grad():
            output = self.model(**inputs)
            predicted_class = torch.argmax(output.logits, dim=1).item()
        return predicted_class
    

