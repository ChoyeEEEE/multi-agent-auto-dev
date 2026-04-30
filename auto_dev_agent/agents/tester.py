from utils.executor import run_code

class Tester:
    def run(self, code):
        stdout, stderr = run_code(code)
        success = stderr == ""
        return {
            "success": success,
            "output": stdout,
            "error": stderr
        }
