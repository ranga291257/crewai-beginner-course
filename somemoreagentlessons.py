import os

from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
os.environ["OPENAI_API_KEY"] = "NA"
os.environ["SERPER_API_KEY"] = "1cbad1e84ebfa9745bdc3a3505a5c5bad7885e61" # serper.dev API key

llm = ChatOpenAI(
    model="stablelm-zephyr",
    base_url="http://localhost:11434/v1"
)


research_agent = Agent(
  role='Researcher',
  goal='Find and summarize the latest AI news',
  backstory="""You're a researcher at a large company.
  You're responsible for analyzing data and providing insights
  to the business.""",
  verbose=True,
  max_iter= 600,  # Maximum iterations
)

search_tool = SerperDevTool()

task = Task(
  description='Find and summarize the latest AI news',
  expected_output='A bullet list summary of the top 5 most important AI news',
  agent=research_agent,
  tools=[search_tool]
)

crew = Crew(
    agents=[research_agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()
print(result)