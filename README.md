# High Counsel

High Counsel is a local app that runs multiple LLMs as a council and produces a final synthesized answer through a chairman model.

It has:
A Python backend that talks to OpenRouter
A Vite frontend that streams responses

## What you need

Python 3.10 or newer
Node.js and npm
uv

On macOS with Homebrew:

brew install python node uv

## Setup

Clone and install:

git clone https://github.com/Joieux/High-Counsel.git
cd High-Counsel
uv sync
cd frontend
npm install
cd ..

## Add your OpenRouter key

Create a .env file in the repo root:

OPENROUTER_API_KEY=sk-or-v1-yourkeyhere

Do not commit this file.

## Configure the council

Edit backend/config.py and set your council members and chairman.

Start simple first:

COUNCIL_MODELS = [
    "anthropic/claude-sonnet-4.5",
]

CHAIRMAN_MODEL = "anthropic/claude-sonnet-4.5"

Then add members one at a time.

Tip: if a model fails, it is usually a model id typo or a model that does not support your input type.

## Run

From the repo root:

./start.sh

Frontend:
http://localhost:5173

Backend:
http://localhost:8001

## Troubleshooting

401 Unauthorized in backend logs
Your OpenRouter key is missing, empty, or not being loaded

400 Bad Request in backend logs
Most often a model id typo, for example gpt 4o uses the letter o

Backend crash but frontend still runs
The frontend can appear healthy even when the backend failed to boot, so always trust the backend terminal output

## Safety and secrets

Never commit:
.env
data/conversations

## License

MIT
