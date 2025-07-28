# 🛠️Blueprint-Driven CI/CD Framework

This repository demonstrates a modular, scalable, and tech-agnostic CI/CD framework using **GitHub Actions** and a **blueprint-driven approach**.

The goal is to standardize build and deployment pipelines across multiple languages and tech stacks using a single source of truth — the `.ci-blueprint.yaml`.

---

## 🚀 How It Works

### 📁 1. Project Setup

Every application repository must include a `.ci-blueprint.yaml` file that defines:
- Tech stack (Python, Java, Node, etc.)
- Build tool (pip, Maven, npm, etc.)
- CI stages to run (lint, test, dockerize, etc.)
- Deployment method (Docker, SAM, CDK, etc.)
- Branching strategy (semver, trunk-based, etc.)

``` Example yaml format
tech_stack: python
build_tool: pip
ci_stages:
  - lint
    - test
      - dockerize
      deploy_method: docker
      branch_strategy: semver
      