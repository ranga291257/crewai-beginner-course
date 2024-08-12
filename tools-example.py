import os
from dotenv import load_dotenv
from langchain_community.tools import tool
from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew

# Load environment variables from a .env file
load_dotenv()

# Set up OpenAI API key (make sure it's properly configured in your .env file)
os.environ["OPENAI_API_KEY"] = "sk-proj-1111"

# Define the calculation tool using the @tool decorator
@tool("Calculate")
def calculate(equation):
    """ Useful for solving math equations """
    try:
        return eval(equation)
    except Exception as e:
        return f"Error: {str(e)}"

# Initialize the language model
llm = ChatOpenAI(
    model="stablelm-zephyr",
    base_url="http://localhost:11434/v1"
)

# Get user input for the math equation
print("## Welcome to the Math Whiz")
math_input = input("What is your math equation: ")

# Define the Math Agent
math_agent = Agent(
    max_iter=600,  # Optional
    max_rpm=None, # Optional
    max_execution_time=None, # Optional
    role="Math Magician",
    goal="You are able to evaluate any math expression.",
    backstory="YOU ARE A MATH WHIZ.",
    verbose=True,
    tools=[calculate],
)

# Define a simple task for the agent
task1 = Task(
    description=math_input,
    expected_output="Provide the result of the calculation.",
    agent=math_agent
)

# Create a crew with the Math Agent
crew = Crew(
    agents=[math_agent],
    tasks=[task1],
    verbose=True  # Ensure verbose is set to True for detailed output
)

# Kick off the crew to execute the task
result = crew.kickoff()

# Print the result of the calculation
print("############")
print(result)









