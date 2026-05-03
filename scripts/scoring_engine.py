"""
QA Scoring Engine for LLM Outputs
"""

def calculate_score(metrics):
    score = (
        metrics["accuracy"] * 0.3 +
        metrics["relevance"] * 0.3 +
        metrics["consistency"] * 0.2 +
        (1 - metrics["hallucination_rate"]) * 0.2
    )
    return round(score, 2)


if __name__ == "__main__":
    sample = {
        "accuracy": 0.85,
        "relevance": 0.9,
        "consistency": 0.8,
        "hallucination_rate": 0.1
    }

    print("Final QA Score:", calculate_score(sample))
