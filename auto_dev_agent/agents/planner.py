from utils.llm import call_llm

class Planner:
    def run(self, task):
        prompt = f'''
        Break the task into steps and return JSON:
        {{
            "task": "...",
            "steps": ["step1", "step2"]
        }}
        Task: {task}
        '''
        return call_llm("You are a planning agent.", prompt)
