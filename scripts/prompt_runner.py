"""
Simulated LLM Prompt Runner
"""

import json

def run_prompt(prompt):
    # Simulated response
    return f"Generated response for: {prompt}"

def main():
    with open("../datasets/qa-eval-prompts.json") as f:
        data = json.load(f)

    for item in data:
        output = run_prompt(item["prompt"])
        print(item["id"], "=>", output)

if __name__ == "__main__":
    main()
