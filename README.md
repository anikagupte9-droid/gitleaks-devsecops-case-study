# Secure Vehicle Telemetry Application Using Gitleaks

## 1. Overview

This project demonstrates the use of **Gitleaks** as a DevSecOps security tool for detecting and preventing hardcoded credentials in a vehicle telemetry application.

A simulated Formula Student vehicle telemetry system is used as the application scenario. The telemetry client communicates with an authenticated mock telemetry service to retrieve vehicle parameters such as speed, battery voltage, battery current, motor torque, and motor temperature.

Gitleaks is integrated into the Git workflow using a **pre-commit hook** so that exposed credentials are detected before they can be committed to the repository.

---

## 2. Problem Statement

Modern applications frequently require API keys, access tokens, and other credentials to communicate with external services.

If developers accidentally hardcode these credentials into source code, they may be exposed through version control repositories and create a security risk.

This project demonstrates a realistic DevSecOps scenario in which a developer accidentally hardcodes a telemetry service credential and Gitleaks automatically detects and prevents the insecure commit.

---

## 3. Case Study Scenario

The application simulates a telemetry system for a Formula Student vehicle named **Athena**.

The system consists of:

```text
Vehicle Telemetry Client
          |
          | Authenticated API Request
          v
    Mock Telemetry API
          |
          v
    Telemetry JSON Data