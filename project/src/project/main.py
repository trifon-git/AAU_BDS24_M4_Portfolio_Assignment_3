#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime
from project.crew import CSVAnalysisProject
from project.tools.custom_tool import CSVAnalyzer
from langchain_openai import ChatOpenAI
print(f"Current Working Directory: {os.getcwd()}")

warnings.filterwarnings("ignore", category=SyntaxWarning)

from dotenv import load_dotenv
import openai

load_dotenv()

# Initialize the lm
OpenAIGPT4 = ChatOpenAI(
    model="gpt-4o-mini"
)

def run():
    """
    Run the CSV Analysis Crew with a given CSV file.
    """
    if len(sys.argv) < 2:
        print("⚠️  Usage: python main.py run <path_to_csv_file>")
        sys.exit(1)
    
    csv_file = './src/data/train.csv'


    
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"❌ Error: File '{csv_file}' not found.")

    print(f"📂 Loading CSV: {csv_file}")
    analyzer = CSVAnalyzer(csv_file)
    analyzer.load_data()
    analyzer.clean_data()
    
    # Directly use the in-memory cleaned data without saving to a new CSV file
    analyzer.clean_data()

    # Generate dataset summary
    dataset_summary = analyzer.get_summary()

    # Pass the dataset summary in inputs
    inputs = {
        'csv_file': csv_file,
        'current_year': str(datetime.now().year),
        'topic': 'CSV Data Analysis',
        'dataset_summary': dataset_summary  # Add the dataset summary
    }

    
    try:
        print(f"🚀 Starting CSV Analysis on: {csv_file}")
        CSVAnalysisProject().crew().kickoff(inputs=inputs)
        print("✅ CSV Analysis Completed Successfully. Report saved in 'reports/'.")
    except Exception as e:
        raise Exception(f"❌ An error occurred while running the CSV analysis: {e}")

def train():
    if len(sys.argv) < 4:
        print("⚠️  Usage: python main.py train <iterations> <output_file>")
        sys.exit(1)
    inputs = {
        "csv_file": "./src/data/train.csv"
    }
    try:
        CSVAnalysisProject().crew().train(n_iterations=int(sys.argv[2]), filename=sys.argv[3], inputs=inputs)
    except Exception as e:
        raise Exception(f"❌ An error occurred while training the Crew: {e}")

def replay():
    if len(sys.argv) < 3:
        print("⚠️  Usage: python main.py replay <task_id>")
        sys.exit(1)
    try:
        CSVAnalysisProject().crew().replay(task_id=sys.argv[2])
    except Exception as e:
        raise Exception(f"❌ An error occurred while replaying the CSV Analysis: {e}")

def test():
    if len(sys.argv) < 4:
        print("⚠️  Usage: python main.py test <iterations> <model>")
        sys.exit(1)
    inputs = {
        "csv_file": "./src/data/train.csv"
    }
    try:
        CSVAnalysisProject().crew().test(n_iterations=int(sys.argv[2]), openai_model_name=sys.argv[3], inputs=inputs)
    except Exception as e:
        raise Exception(f"❌ An error occurred while testing the CSV Analysis: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️  Usage: python main.py <run|train|replay|test> [additional_arguments]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print("⚠️  Unknown command. Use 'run', 'train', 'replay', or 'test'.")
