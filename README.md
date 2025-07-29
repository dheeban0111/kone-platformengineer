# 🚀 Kone Ci/Cd Blueprint Framework – Platform Engineering POC

This repo demonstrates a **dynamic, GitHub Actions-based CI/CD framework** that generates pipelines automatically from a centralized configuration (`.ci-blueprint.yaml`). It supports multiple tech stacks and deployment methods via a shared, modular template strategy.

---

## 📌 Objective

Build a **standardized and extensible CI/CD system** that:

- ✅ Supports **multiple tech stacks** (Python, Node, Java, etc.)
- ✅ Handles different **build tools** (pip, npm, Maven, etc.)
- ✅ Dynamically creates stages based on a config file
- ✅ Applies consistent **branching/tagging rules**
- ✅ Is easy to **extend**, maintain, and scale across teams

---

## 🧠 How It Works

```mermaid
flowchart TD
  A[Trigger a manual run on CI dispatcher workflow] --> B[Dispatcher Workflow]
  B --> C[Read .ci-blueprint.yaml]
  C --> D[Identify tech_stack & ci stages]
  D --> E[Python CI Workflow gets triggerd automatically]
  E --> F[Run selected stages: Lint → Test → Dockerize]
