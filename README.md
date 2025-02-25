# 📊 CSV Analysis with CrewAI & Streamlit

This project is a dynamic CSV analysis tool that integrates **Streamlit** for real-time visualizations and logging, combined with **CrewAI agents** for sequential data processing tasks like inference, cleaning, visualization, and reporting.

## 🔍 Key Features
- Upload and analyze CSV files through an interactive web interface.
- Automated data inference, cleaning, visualization, and report generation.
- Sequential execution of tasks using CrewAI agents.

## 📁 Project Structure

- **`app.py`**  
  Runs the Streamlit web app. Handles CSV uploads, live logging, data processing, and report downloading.

- **`crew.py`**  
  Configures CrewAI agents and tasks:
  - *Dataset Inference Specialist*: Analyzes dataset structure and potential uses.
  - *Data Cleaning Specialist*: Identifies and applies data cleaning strategies.
  - *Visualization Expert*: Generates data visualizations. (not working properly)
  - *Reporting Analyst*: Compiles findings into a markdown report.

- **`custom_tool.py`**  
  Contains `CSVAnalyzer`, responsible for:
  - Loading and encoding detection for CSV files.
  - Cleaning data (handling missing values, fixing data types).
  - Generating a quick summary of the dataset.

- **`tasks.yaml`**  
  Defines task descriptions and expected outputs for:
  - Dataset inference
  - Data cleaning
  - Report generation
- **`agents.yaml`**  
  Specifies the configuration for each agent in the CrewAI system, including:
  - Agent roles and responsibilities.
  - Model parameters and settings for execution.
  - Verbosity and task-specific behavior settings.
 

## 🚀 Usage
Find the .env file and add your OpenAPI key (you can generate one [here](https://platform.openai.com/) )

Load the poetry environment
```
#run where the .toml file is
poetry install
poetry env activate
```
Rrun the Streamlit app

```
# on the initital project folder run
streamlit run app.py
```
Upload your csv and you are ready to go

## Project Collaborators

Lauris Piziks- AAU BDS24

Tryfonas Karmiris- AAU BDS24
