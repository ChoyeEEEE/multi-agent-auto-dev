from utils.llm import call_llm

class Coder:
    def run(self, task):
        prompt = f"Write Python code for: {task}"
        return call_llm("You are a senior Python developer.", prompt)
