import os
from crewai import Agent
from langchain_openai import ChatOpenAI
os.environ["OPENAI_API_KEY"] = "sk-proj-1111"
llm = ChatOpenAI(
    model="stablelm-zephyr",
    base_url="http://localhost:11434/v1")
# Example: Creating an agent with essential attributes
agent = Agent(
    role='Data Analyst',
    goal='Extract actionable insights',
    backstory="""You're a data analyst at a large company.
    You're responsible for analyzing data and providing insights
    to the business. Currently, you're working on a project to
    analyze the performance of our marketing campaigns.""",
    function_calling_llm=llm,  # Optional for function calling
    max_iter=15,  # Maximum iterations
    verbose=True,  # Enable detailed logging
    allow_delegation=True,  # Allow agent to delegate tasks
    cache=True  # Enable caching
    # Remove undefined parameters
)


# Another example: Minimal agent configuration
minimal_agent = Agent(
    role="{topic} specialist",
    goal="Figure {goal} out",
    backstory="I am the master of {role}",
    system_template="""system\n\n{{ .System }}""",
    prompt_template="""user\n\n{{ .Prompt }}""",
    response_template="""assistant\n\n{{ .Response }}"""
)

# Simulating calling the agent with print statements
def call_agent(agent, description):
    print(f"Calling agent with role: {agent.role}")
    print(f"Goal: {agent.goal}")
    print(f"Backstory: {agent.backstory}")
    print(f"Description: {description}")
    # Simulate agent processing
    print(f"Agent {agent.role} is processing the task...")
    # Normally, you'd call the agent's method to execute the task here
    # For example: result = agent.execute_task(description)
    # We'll simulate the result for now
    result = "Simulated result"
    print(f"Result: {result}\n")

# Example usage of the agents
print("### Using the Full Data Analyst Agent ###")
call_agent(agent, "Analyze the effectiveness of the latest marketing campaign.")

print("### Using the Minimal Specialist Agent ###")
call_agent(minimal_agent, "Investigate the {topic} for better understanding.")
