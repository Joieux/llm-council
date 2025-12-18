"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Council members - list of OpenRouter model identifiers
COUNCIL_MODELS = [
    "anthropic/claude-sonnet-4.5",
    "openai/gpt-4o-mini",
    "openai/gpt-5.1",
    "deepseek/deepseek-r1",
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "anthropic/claude-sonnet-4.5"

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
