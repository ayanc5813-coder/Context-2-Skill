# 🧠 Ctx2Skill

A lightweight, from-scratch implementation of the **Ctx2Skill** framework, optimized for Google Colab and powered by OpenRouter. 

This project allows Large Language Models (LLMs) to autonomously learn, evolve, and apply context-specific "skills" without any parameter fine-tuning or human intervention. By utilizing a multi-agent self-play loop, the model teaches itself how to better reason over complex information.

---

## ✨ Key Features
* **Zero Heavy Boilerplate:** A clean-room implementation of the core Ctx2Skill architecture without the bulky benchmarking code of the original repo.
* **OpenRouter Native:** Fully configured to route requests through OpenRouter, allowing you to use dozens of state-of-the-art models (like `owl-alpha`, `claude-3`, or `gemini-2.0`) for free or at a fraction of the cost.
* **Bulletproof JSON Parsing:** Includes fallback regex extraction to handle models that wrap JSON in markdown blocks or conversational fluff.
* **Reasoning Model Support:** Automatically strips `<think>...</think>` chain-of-thought tags so models like `nemotron-reasoning` or `deepseek-r1` don't crash the JSON parser.
* **Built-in Rate Limit Handling:** Gracefully catches `429 Rate Limit` errors (common with free OpenRouter tiers) and implements an automatic pause-and-retry mechanism.

---

## 🏗️ Architecture: The Multi-Agent Loop

The framework relies on three distinct AI agents communicating in a closed loop:

1. ⚔️ **Challenger Agent:** Reads the provided context and the current "skills" memory. It generates a complex task and a grading rubric to test the system's understanding.
2. 🧩 **Reasoner Agent:** Attempts to solve the Challenger's task using the context and the currently available skills.
3. ⚖️ **Judge Agent:** Evaluates the Reasoner's solution against the rubric. It then **rewrites and evolves** the skill set, providing new rules, heuristics, and procedures to ensure the Reasoner performs better on the next iteration.

---

## 🚀 Getting Started (Google Colab)

### 1. Prerequisites
You only need a Google account (for Colab) and an [OpenRouter API Key](https://openrouter.ai/).

### 2. Installation
Open a new Google Colab notebook and install the official OpenAI SDK (which we will reroute to OpenRouter).

```bash
!pip install openai -q
