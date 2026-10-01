# LLM Agent in a Simulated Room

A LangChain agent that controls a robot in a small text-based world
(physical AI + LLM trial for our research paper).

## Setup
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

## Run
python agent.py

## Files
- world.py: the simulated world and its tools (look, move_to, pick_up, put_down)
- agent.py: the LangChain agent and task runner
- tasks.txt: test tasks

## Model
llama3.1 via Ollama (local)
