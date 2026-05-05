# ==========================================
# CELL 1: SETUP & CREDENTIALS
# ==========================================
!pip install openai -q

import os
import json
from openai import OpenAI

# 🛑 Paste your OpenRouter API Key here
OPENROUTER_API_KEY = "sk-or-v1-YOUR-API_KEY"
MODEL_NAME = "YOUR_MODEL" 

# Initialize the client pointing to OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
    default_headers={
        "HTTP-Referer": "https://colab.research.google.com/",
        "X-Title": "Ctx2Skill-From-Scratch",
    }
)

# Helper function to call the LLM and parse JSON safely
def call_llm(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        response_format={"type": "json_object"} # Forces JSON output (supported by most models)
    )
    
    raw_content = response.choices[0].message.content
    try:
        return json.loads(raw_content)
    except json.JSONDecodeError:
        # Fallback cleanup if the model wraps it in markdown blocks
        clean_content = raw_content.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_content)

print("✅ Environment Set up and LLM Client Ready!")
