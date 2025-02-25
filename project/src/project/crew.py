from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import yaml
import matplotlib.pyplot as plt

# Function to load YAML config files
def load_yaml(file_path):
    try:
        with open(file_path, "r") as file:
            config = yaml.safe_load(file)
            if config is None:
                print(f"❌ Failed to load YAML from {file_path}. The file is empty or invalid.")
            else:
                print(f"✅ Successfully loaded YAML from {file_path}.")
            return config
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return None

@CrewBase
class CSVAnalysisProject:
    """CSV Analysis Crew"""

    def __init__(self):
        self.agents_config = load_yaml("src/project/config/agents.yaml")
        self.tasks_config = load_yaml("src/project/config/tasks.yaml")

    # --- Define Agents ---
    @agent
    def dataset_inference_specialist(self) -> Agent:
        return Agent(
            name="Dataset Inference Specialist",
            config=self.agents_config.get('dataset_inference_specialist', {}),
            verbose=True
        )

    @agent
    def data_cleaning_specialist(self) -> Agent:
        return Agent(
            name="Data Cleaning Specialist",
            config=self.agents_config.get('data_cleaning_specialist', {}),
            verbose=True
        )

    @agent
    def visualization_expert(self) -> Agent:
        return Agent(
            name="Visualization Expert",
            config=self.agents_config.get('visualization_expert', {}),
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            name="Reporting Analyst",
            config=self.agents_config.get('reporting_analyst', {}),
            verbose=True
        )

    # --- Define Tasks ---
    @task
    def dataset_inference_task(self) -> Task:
        task_config = self.tasks_config.get('dataset_inference_task', None)
        if task_config is None:
            print("❌ Task 'dataset_inference_task' not found in tasks.yaml.")
            return None
        result = task_config.get('expected_output', None)
        if result is None:
            print("❌ Expected output not found for dataset inference task.")
        else:
            print("✅ Dataset inference task output:\n", result)
        return Task(name="Dataset Inference Task", config=task_config)

    @task
    def data_cleaning_task(self) -> Task:
        task_config = self.tasks_config.get('data_cleaning_task', None)
        if task_config is None:
            print("❌ Task 'data_cleaning_task' not found in tasks.yaml.")
            return None
        result = task_config.get('expected_output', None)
        if result is None:
            print("❌ Expected output not found for data cleaning task.")
        else:
            print("✅ Data cleaning task output:\n", result)
        return Task(name="Data Cleaning Task", config=task_config)

    @task
    def visualization_task(self) -> Task:
        task_config = self.tasks_config.get('visualization_task', None)
        if task_config is None:
            print("❌ Task 'visualization_task' not found in tasks.yaml.")
            return None
        visualization_code = task_config.get('expected_output', None)
        if visualization_code is None:
            print("❌ Visualization code was not generated.")
        else:
            try:
                print("🔍 Executing visualization code...\n", visualization_code)
                exec(visualization_code)
                print("✅ Visualization code executed successfully.")
            except Exception as e:
                print(f"❌ Error executing visualization code: {e}")
        return Task(name="Visualization Task", config=task_config)

    @task
    def report_generation_task(self) -> Task:
        task_config = self.tasks_config.get('report_generation_task', None)
        if task_config is None:
            print("❌ Task 'report_generation_task' not found in tasks.yaml.")
            return None
        result = task_config.get('expected_output', None)
        if result is None:
            print("❌ Expected output not found for report generation task.")
        else:
            print("✅ Report generation output:\n", result)
        return Task(name="Report Generation Task", config=task_config)

    # --- Define Crew ---
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
