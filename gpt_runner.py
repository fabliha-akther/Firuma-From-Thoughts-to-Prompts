from gpt4all import GPT4All

_model = None

def load_model():
    global _model
    if _model is None:
        model_path = r"/path/to/your/model/file/*.gguf"
        _model = GPT4All(model_path)
    return _model

def run_gpt_model(prompt, tone):
    model = load_model()
    response = model.generate(prompt)
    return response
