import subprocess
import json

class Adversary:
    def __init__(self, model_path):
        self.model_path = model_path

    def attack(self, code, existing_tests):
        prompt = f"Find a breaking test case for this code. Existing tests: {existing_tests}. Return only valid JSON format: {{'input': ..., 'expected': ...}}. Code:\n{code}"
        cmd = ["ollama", "run", self.model_path, prompt]
        try:    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return json.loads(result.stdout.strip())
        except subprocess.TimeoutExpired:
            print("Adversary: LLM timeout after 30s")
            return None
        except json.JSONDecodeError:
            print(f"Adversary: Invalid JSON from LLM: {result.stdout}")
            return None
        except Exception as e:
            print(f"Adversary: Unexpected error: {e}")
            return None