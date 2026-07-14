# AI Engineering Skill Library

## Purpose

This skill library is designed to help AI agents operate like experienced software engineers rather than code generators.

Each skill has a single responsibility.

Skills should be composable.

A feature should flow through multiple skills instead of one giant prompt.

---

# Skill Hierarchy

## Foundation Layer

These skills are responsible for understanding the problem before implementation begins.

### 1. Repository Archaeologist

Purpose:

Understand the existing codebase before any modifications.

Responsibilities:

* Analyze architecture
* Discover conventions
* Identify dependencies
* Locate implementation patterns
* Produce codebase analysis reports

Recommended Model:

* Claude
* Gemini

---

### 2. Requirements Analyst

Purpose:

Transform vague requirements into precise specifications.

Responsibilities:

* Clarify requirements
* Identify assumptions
* Discover hidden requirements
* Define acceptance criteria
* Generate requirement documents

Recommended Model:

* Claude

---

### 3. Feature Planner

Purpose:

Convert requirements into implementation plans.

Responsibilities:

* Feature decomposition
* Dependency mapping
* Risk identification
* Task generation
* Milestone creation

Deliverable:

docs/feature_plan.md

Recommended Model:

* Claude

---

# Architecture Layer

These skills determine how systems should be built.

### 4. System Architect

Purpose:

Design scalable system architecture.

Responsibilities:

* Service boundaries
* Data flow
* Component interactions
* Deployment considerations
* Scalability planning

Deliverables:

* Architecture diagrams
* Request flow diagrams
* System documentation

Recommended Model:

* Claude
* Gemini

---

### 5. Database Architect

Purpose:

Design efficient database structures.

Responsibilities:

* Schema design
* Relationship design
* Indexing strategy
* Migration planning
* Query optimization

Recommended Model:

* Claude
* DeepSeek

---

### 6. API Contract Guardian

Purpose:

Define stable contracts between systems.

Responsibilities:

* Endpoint definitions
* Request schemas
* Response schemas
* Error formats
* API consistency

Deliverables:

* OpenAPI specifications
* API documentation

Recommended Model:

* Claude

---

# Implementation Layer

These skills generate production-grade software.

### 7. Senior Backend Engineer

Purpose:

Implement backend systems.

Responsibilities:

* Services
* Repositories
* Controllers
* Authentication
* Authorization
* Transactions

Recommended Model:

* Claude
* Codex

---

### 8. Frontend Systems Engineer

Purpose:

Implement maintainable frontend systems.

Responsibilities:

* UI architecture
* State management
* API integration
* Component design
* Accessibility

Recommended Model:

* Claude
* Gemini

---

### 9. Refactoring Specialist

Purpose:

Improve code quality without changing behavior.

Responsibilities:

* Simplify complexity
* Remove duplication
* Improve readability
* Improve maintainability

Recommended Model:

* Claude

---

# Quality Layer

These skills verify correctness.

### 10. Test Engineer

Purpose:

Ensure functionality is verifiable.

Responsibilities:

* Unit tests
* Integration tests
* End-to-end tests
* Edge case testing

Recommended Model:

* Claude
* Codex

---

### 11. Security Auditor

Purpose:

Identify security weaknesses.

Responsibilities:

* Authentication review
* Authorization review
* Input validation review
* File upload review
* Secret management review

Recommended Model:

* Claude
* Gemini

---

### 12. Performance Engineer

Purpose:

Identify bottlenecks.

Responsibilities:

* Query analysis
* Memory analysis
* Network analysis
* Caching recommendations
* Concurrency review

Recommended Model:

* Claude

---

# Operations Layer

These skills prepare systems for production.

### 13. Observability Engineer

Purpose:

Ensure system visibility.

Responsibilities:

* Logging
* Metrics
* Tracing
* Alerting
* Monitoring

Recommended Model:

* Claude

---

### 14. Production Readiness Auditor

Purpose:

Determine whether software is ready for deployment.

Responsibilities:

* Deployment review
* CI/CD review
* Backup review
* Recovery review
* Infrastructure review

Recommended Model:

* Claude

---

# Governance Layer

These skills act as final gatekeepers.

### 15. Principal Engineer Reviewer

Purpose:

Perform final technical review.

Responsibilities:

* Architecture review
* Scalability review
* Security review
* Maintainability review
* Technical debt review

Output:

APPROVE

or

REJECT

Recommended Model:

* Claude
* Gemini

---

### 16. Documentation Architect

Purpose:

Ensure long-term maintainability.

Responsibilities:

* README generation
* Architecture documentation
* ADR generation
* Runbook generation
* API documentation

Recommended Model:

* Claude

---

# Feature Development Workflow

Every feature should flow through the skills in this order:

Requirements Analyst
↓
Repository Archaeologist
↓
Feature Planner
↓
System Architect
↓
Database Architect
↓
API Contract Guardian
↓
Senior Backend Engineer
↓
Frontend Systems Engineer
↓
Test Engineer
↓
Security Auditor
↓
Performance Engineer
↓
Observability Engineer
↓
Production Readiness Auditor
↓
Principal Engineer Reviewer
↓
Documentation Architect

---

# Long-Term Goal

The objective is not to generate more code.

The objective is to create a repeatable engineering process that consistently produces:

* Correct software
* Secure software
* Scalable software
* Maintainable software
* Observable software
* Production-ready software
