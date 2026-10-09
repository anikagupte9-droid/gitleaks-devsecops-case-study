# Automated Secret Detection in DevSecOps Using Gitleaks

## 1. Overview

This case study demonstrates the use of **Gitleaks** as a DevSecOps security tool for detecting hardcoded secrets in source code.

The project demonstrates how secret detection can be integrated directly into the software development workflow using a **Git pre-commit hook**, preventing developers from accidentally committing sensitive credentials.

---

## 2. Problem Statement

Hardcoded API keys, passwords, tokens, and other credentials in source code can expose sensitive information and create security risks.

This project demonstrates an automated approach to detecting and preventing such secrets before they are committed to a Git repository.

---

## 3. Tool Selected

**Gitleaks**

Gitleaks is a secret-detection tool that scans source code and Git repositories for accidentally exposed credentials and other sensitive information.

### DevOps Lifecycle Stage

**Security / DevSecOps**

---

## 4. Technologies Used

- Gitleaks 8.30.0
- Git
- GitHub
- Python
- pre-commit
- PowerShell
- Visual Studio Code

---

## 5. Project Workflow

```text
Developer writes code
        |
        v
Secret accidentally introduced
        |
        v
Git commit attempted
        |
        v
Pre-commit hook
        |
        v
Gitleaks scan
        |
    +---+---+
    |       |
 Secret    Clean
    |       |
    v       v
 Block    Allow
 Commit   Commit