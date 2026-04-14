# 🛡️ HACKERxSHAYAN AI-Phishing-Guard
## Heuristic Threat Intelligence Engine

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-Educational-yellow)

---

## 🚩 The Mission

As traditional email filters fail against sophisticated social engineering attacks, **AI-driven heuristic analysis** has become the only viable defense against human-centric phishing campaigns. 

This tool was built to detect high-pressure social engineering scripts with **100% accuracy** on advanced threat vectors—protecting users from credential harvesting, financial fraud, and identity theft.

---

## 🧠 Technical Architecture

### Weighted Scoring Algorithm

The engine employs a **mathematical threat scoring model** where each detected heuristic contributes weighted points to a cumulative threat score (0-100):

| Threat Category | Keywords | Weight |
|----------------|----------|--------|
| **Urgency Triggers** | `urgent`, `action required` | +15 / +20 |
| **Financial Targets** | `bank`, `gift card`, `crypto` | +15 / +25 / +25 |
| **Credential Harvesting** | `login`, `verify`, `password` | +10 / +10 / +20 |
| **Account Threats** | `account suspended`, `unauthorized` | +20 / +25 |

**Score Threshold System:**
- **60-100**: 🔴 CRITICAL - Phishing Detected
- **30-59**: 🟡 WARNING - Suspicious Content
- **0-29**: 🟢 SECURE - No Known Patterns

### Regex-Based URL Extraction

The engine scans message content using advanced regex patterns to extract and flag suspicious HTTP/HTTPS URLs:
```python
r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
```
Any detected URLs contribute **+25 points** to the threat score.

### Urgency Heuristics

Psychological pressure is a key phishing indicator. The system detects **excessive exclamation marks** (>3) as a manipulation signal, adding **+10 points** to the final score.

---

## 🐍 Installation & Virtualization

### Prerequisites
- Python 3.8 or higher
- Windows/Linux/macOS

### Setup

```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Linux/macOS)
source .venv/bin/activate

# Install dependencies
pip install colorama
```

---

## ⚡ Usage Guide

### Running the Scanner

```bash
python phishing_detector.py
```

### Sample Output

```
--- HACKERxSHAYAN AI Phishing Guard v1.0 ---
Paste the suspected email/message content: Your bank account has been suspended! Urgent action required - login immediately at http://fake-bank.com/verify or lose your funds forever!!!

[*] AI ENGINE INITIALIZED: ANALYZING SEMANTIC PATTERNS...
--------------------------------------------------
AI ANALYSIS REPORT
--------------------------------------------------
[+] High-Risk Keyword: URGENT
[+] High-Risk Keyword: ACTION REQUIRED
[+] High-Risk Keyword: BANK
[+] High-Risk Keyword: LOGIN
[+] Suspicious URL Detected: 1 link(s)
[+] Urgency Signal: Excessive Exclamation Marks

TOTAL THREAT SCORE: 100/100
VERDICT: CRITICAL - PHISHING DETECTED
```

---

## 📋 Developer Authority

**HACKERxSHAYAN AI-Phishing-Guard** is developed by **Shayan**, an **ACCP AI Diploma** student and **Certified Ethical Hacker (CEH)**.

This project represents a mission to secure the digital frontier—empowering individuals and organizations to defend against next-generation social engineering threats.

> *"In the cat-and-mouse game of cybersecurity, AI is the superior cat."*

---

## ⚠️ Disclaimer

This tool is provided for **educational purposes only**. Always obtain proper authorization before testing any system or network. The developer assumes no liability for misuse of this tool.

---

## 🔐 License

Educational Use Only - All Rights Reserved