from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from crewai.memory.long_term.long_term_memory import LongTermMemory
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage


# embeddings = {
# 	"provider": "openai",
# 	"model": "text-embedding-ada-002",
# 	"dimension": 1536,
# }



# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Chalk():
	"""Chalk crew"""
	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools


	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task


	@agent
	def conversation_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['conversation_agent'],
			verbose=True,
			memory=True,
		)
	
	@task
	def conversation(self) -> Task:
		return Task(
			config=self.tasks_config['conversation'],
			agent=self.conversation_agent(),
			memory=True,
		)
	

	


	@crew
	def crew(self) -> Crew:
		"""Creates the Chalk crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			memory=True,
			verbose=True,
			long_term_memory = LongTermMemory(
       storage =LTMSQLiteStorage(db_path="/Users\DELL\Desktop\VS CODE\langflow\Agentic_Journal\storage.db")
    ),
			
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)




@CrewBase
class Chalk1():
	"""Chalk crew"""
	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents1.yaml'
	tasks_config = 'config/tasks1.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools


	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task

	@agent
	def journal_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['journal_agent'],
			verbose=True,
			memory=True,
		)

	
	@task
	def journaling(self) -> Task:
		return Task(
			config=self.tasks_config['journaling'],
			agent = self.journal_agent(),
			memory=True,
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Chalk crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			memory=True,
			verbose=True,
			long_term_memory = LongTermMemory(
       storage =LTMSQLiteStorage(db_path="/Users\DELL\Desktop\VS CODE\langflow\Agentic_Journal\storage.db")
    ),
			

			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)