# Hallucination Detection Framework

## Problem
LLMs may generate:
- Fake APIs
- Incorrect business logic
- Unsupported technical claims

---

## Detection Strategy

### 1. Rule-Based Validation
Check against:
- Known API schema
- Business rules
- Domain constraints

---

### 2. Cross Verification
Compare output with:
- Source documentation
- Golden dataset answers

---

### 3. Semantic Validation
Use embedding similarity to detect:
- Off-topic expansions
- Fabricated context

---

## Example

### Prompt:
"List AWS services for serverless orchestration"

### Hallucinated Output:
- "AWS CloudFlowX" ❌ (does not exist)

---

## QA Rule
If not verifiable → mark as hallucination risk
