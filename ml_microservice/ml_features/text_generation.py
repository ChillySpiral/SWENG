from transformers import pipeline, set_seed


class TextGenerator:
    def __init__(self, seed=42, task="text-generation", model="gpt2"):
        self.generator = pipeline(task=task, model=model)
        set_seed(seed)

    def generate_text(self, text, max_length=30, num_return_sequences=5):
        print(self.generator(text, max_length=max_length, num_return_sequences=num_return_sequences))
