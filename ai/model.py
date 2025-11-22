import json
from ollama import Ollama

class AIModel:
    def __init__(self, model_name="qwen-2.5", personas_file="ai/personas.json"):
        self.model = Ollama(model=model_name)
        with open(personas_file, "r") as f:
            self.personas = json.load(f)
        self.current_persona = "normal"

    def set_persona(self, persona_name):
        if persona_name in self.personas:
            self.current_persona = persona_name

    def ask(self, message):
        prompt = self.personas[self.current_persona]["prompt"] + "\n" + message
        response = self.model.chat(prompt)
        return response

