from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from world import look, move_to, pick_up, put_down

load_dotenv() 

model = init_chat_model("ollama:llama3.1")

agent = create_agent(
    model=model,
    tools = [look, move_to, pick_up, put_down],
    system_prompt = ("You control a robot in a small room. Always call look() first. "
        "Act step by step using the tools. If a tool returns an error, "
        "read it and correct your plan."
    ),
)


result = agent.invoke(
    {"messages": [{"role": "user", "content": "Put the red cup, the book, and the key all in the box."}]}
)

for m in result["messages"]:
    m.pretty_print()