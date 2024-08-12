import os
from crewai import Agent
from croq import SimpleProcessor

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "sk-proj-1111"

# Initialize a croq processor (this could be a wrapper around an LLM)
processor = SimpleProcessor()

# Define a simple callback function
def simple_callback(step_info):
    print(f"Callback: {step_info}")

# Create an agent using crewAI with croq processor
agent = Agent(
    role='Data Analyst',
    goal='Extract actionable insights from data',
    backstory="You are a data analyst who needs to analyze marketing data.",
    processor=processor,  # Using croq processor for text processing
    max_iter=10,
    verbose=True,
    allow_delegation=True,
    step_callback=simple_callback,  # Simple callback for demonstration
)

# Define a function to simulate calling the agent
def call_agent(agent, description):
    print(f"Calling agent with role: {agent.role}")
    print(f"Goal: {agent.goal}")
    print(f"Backstory: {agent.backstory}")
    print(f"Description: {description}")
    
    # Simulate agent processing with croq processor
    result = agent.processor.process(description)
    
    print(f"Result: {result}\n")

# Example usage of the agent
call_agent(agent, "Analyze the effectiveness of the recent email marketing campaign.")
