import subprocess
import tempfile
import os

def run_code(code):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
        f.write(code.encode())
        filename = f.name

    try:
        result = subprocess.run(
            ["python", filename],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout, result.stderr
    except Exception as e:
        return "", str(e)
    finally:
        os.remove(filename)
