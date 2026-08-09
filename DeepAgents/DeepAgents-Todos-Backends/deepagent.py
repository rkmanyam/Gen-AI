from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend, StateBackend, CompositeBackend
from langchain.agents.middleware import TodoListMiddleware
from utils import get_model

model = get_model()

backend = FilesystemBackend(
    root_dir = "./agent_workplace",
    virtual_mode=True
)

agent = create_deep_agent(
    model = model,
    system_prompt="You are a helpful agent",
    middleware=[TodoListMiddleware()],
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/workplace/": backend
        }
    )
    
)

if __name__ == "__main__":
    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": "What's the capial of France?"
        }]
    })