# LLM Evaluation Metrics Framework

## Overview
This defines QA-grade metrics for evaluating LLM outputs.

---

## 1. Accuracy
Measures factual correctness.

Formula:
- Correct statements / Total statements

---

## 2. Relevance
Measures how well output answers the prompt intent.

Scoring:
- 0 → irrelevant
- 1 → partially relevant
- 2 → fully relevant

---

## 3. Hallucination Rate
Detects unsupported or fabricated claims.

Hallucination examples:
- Non-existent APIs
- Incorrect facts
- Invented constraints

---

## 4. Consistency Score
Same prompt → multiple runs → similarity score.

---

## 5. Robustness Score
Performance across:
- Reworded prompts
- Adversarial inputs
- Edge cases

---

## Insight from a Senior QA 
In LLM QA, correctness is probabilistic, not absolute.
