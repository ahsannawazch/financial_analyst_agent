from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task
from langchain_cohere import ChatCohere

@CrewBase
class FinancialAnalystCrew():
    """FinancialAnalystCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/task.yaml'

    def __init__(self) -> None:
        self.cohere_llm = ChatCohere(model='command-r', temperature=0)

    @agent
    def company_researcher(self) -> Agent:
        return Agent(config = self.agents_config["company_researcher"],
                     llm = self.cohere_llm
                     )
    
    @agent
    def company_analyst(self) -> Agent:
        return Agent(config = self.agents_config["company_analyst"],
                     llm = self.cohere_llm
                     )
    
    @task
    def research_company_task(self)-> Task:
        return Task(config = self.tasks_config["research_company_task"],
                    agent = self.company_researcher()
                    )
         
    @task
    def analyze_company_task(self)-> Task:
        return Task(config = self.tasks_config["analyze_company_task"],
                    agent = self.company_analyst()
                    )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process= Process.sequential,
            verbose = 2
        )
    
