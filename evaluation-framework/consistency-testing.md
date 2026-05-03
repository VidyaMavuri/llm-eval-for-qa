# Consistency Testing for LLMs

## Objective
Ensure stable outputs across multiple executions.

---

## Method

1. Run same prompt 5–10 times
2. Compare outputs
3. Compute similarity score

---

## Example

Prompt: "Explain OAuth2 flow"

Outputs:
- Run 1 → technical explanation
- Run 2 → simplified explanation
- Run 3 → inconsistent token flow ❌

---

## QA Failure Indicator
> High variance = unstable model behavior
