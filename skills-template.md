# STANDARD_SKILL_TEMPLATE.md

## Metadata

### Name

[Skill Name]

### Version

1.0.0

### Recommended Models

* Claude
* Gemini
* Codex
* DeepSeek

### Category

* Architecture
* Planning
* Implementation
* Quality
* Operations
* Governance

### Trigger Conditions

Describe when this skill should be invoked.

Example:

* Before implementing new features
* Before modifying existing modules
* Before architectural decisions

---

# Purpose

Explain the mission of this skill.

The purpose should be a single responsibility.

Bad:

"This skill handles architecture, testing, documentation and deployment."

Good:

"This skill analyzes an existing repository and produces an implementation-focused understanding of the codebase."

---

# Core Responsibilities

The skill MUST perform the following tasks:

* Task A
* Task B
* Task C

The skill MUST NOT perform:

* Task X
* Task Y
* Task Z

---

# Inputs

Expected inputs.

Example:

* Source code
* Project structure
* Feature request
* Documentation

---

# Outputs

Expected outputs.

Example:

* Analysis report
* Architecture document
* Feature plan

---

# Process

Step-by-step reasoning process.

Step 1

...

Step 2

...

Step 3

...

---

# Deliverables

Specific artifacts that must be produced.

Examples:

docs/architecture.md

docs/feature_plan.md

docs/security_review.md

---

# Quality Standards

The output must:

* Be complete
* Be technically accurate
* Be actionable
* Be implementation-ready

---

# Constraints

Rules the skill must follow.

Examples:

* Do not write code
* Do not modify files
* Do not make assumptions without evidence
* Always cite file locations

---

# Verification Checklist

Before finishing verify:

□ All requirements addressed

□ No assumptions remain

□ Deliverables generated

□ Recommendations justified

---

# Example Invocation

[prompt example]

---

# Example Output

[expected output example]
