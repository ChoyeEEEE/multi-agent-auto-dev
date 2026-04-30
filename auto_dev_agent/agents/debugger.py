from utils.llm import call_llm

class Debugger:
    def run(self, code, error):
        prompt = f'''
        Fix the Python code based on error.

        Code:
        {code}

        Error:
        {error}

        Return ONLY fixed code.
        '''
        return call_llm("You are a debugging expert.", prompt)
