# Smishing Detection Tool

A Python-based SMS phishing (smishing) detection system that analyzes text messages using rule-based heuristic techniques to identify malicious patterns such as urgency language, threat signals, and social engineering tactics.

The system evaluates multiple features within a message and assigns a weighted risk score (0–100) indicating the likelihood that the message is a smishing attempt.

---

## Project Overview

Smishing attacks rely heavily on **social engineering**, urgency, impersonation, and malicious links to deceive users. This project simulates a lightweight detection engine that models these behaviors using rule-based analysis.

Each message is evaluated across multiple dimensions, including:

- urgency and pressure language
- threat and enforcement signals
- sender context (unknown contact, group messaging, etc.)
- (planned) malicious link detection and domain analysis
- (planned) impersonation of trusted entities (e.g., IRS, DMV, banks)

Each detected signal contributes to a cumulative **risk score**, allowing the system to classify messages based on severity.

---

## How It Works

1. Messages are loaded from a JSON dataset  
2. Each message is passed into the `MessageAnalyzer`  
3. Detection modules evaluate the message for suspicious patterns  
4. Flags are generated for each detected signal  
5. A weighted risk score is calculated  
6. Results are displayed via a command-line interface  

---

### `data/examples.json`
Stores sample SMS messages and metadata used for testing the detection system.

### `engine/analyzer.py`
Core detection engine implementing rule-based analysis, flag generation, and risk scoring.

### `cli.py`
Command-line interface for running the analyzer on datasets and displaying results.

---

## Current Features

- Rule-based SMS analysis using object-oriented Python design  
- Multi-factor heuristic detection (urgency, pressure, and threat signals)  
- Weighted risk scoring system for evaluating message severity  
- JSON-driven dataset input for scalable message testing  
- CLI-based output displaying message analysis results and flagged indicators  

---

## Future Features

Planned improvements to the system include:

- Advanced URL detection and domain validation to identify malicious links and suspicious TLDs (e.g., `.vip`, `.click`, `.cc`)  
- Entity impersonation detection (e.g., IRS, DMV, banks, toll services) to identify spoofed organizations  
- Modular detection architecture for extensible rule-based analysis  
- Enhanced flag explanations including trigger phrases for improved interpretability  
- Structured output formats (e.g., JSON reports) for integration with other tools  
- Performance evaluation metrics such as detection accuracy and false positive rate  
- Expanded dataset of both malicious and legitimate messages for improved testing and validation  

---

## Cybersecurity Relevance

This project demonstrates how **rule-based detection systems** can be used to model real-world smishing attacks and identify common social engineering techniques.

By simulating how attackers craft messages, the system highlights:

- how urgency and fear are used to manipulate users  
- how malicious links are disguised  
- how impersonation increases credibility of attacks  

Understanding these patterns is critical for building more advanced detection systems and improving user awareness of phishing threats.

---

## Author

Avery Dyer