import streamlit as st
import pandas as pd
from datetime import datetime
from project.crew import CSVAnalysisProject
from project.tools.custom_tool import CSVAnalyzer
import io
import sys
import os

# Redirect standard output to Streamlit
class StreamlitLogger(io.StringIO):
    def write(self, message):
        if message.strip():
            st.write(message)

# Replace default stdout with Streamlit logger
sys.stdout = StreamlitLogger()

# Streamlit App Title
st.title("📊 CSV Analysis Streamlit App with Real-time Logs and Report Download")
st.write("Upload your CSV file to begin the analysis and see live outputs.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        # Read the uploaded file directly into a DataFrame
        df = pd.read_csv(uploaded_file)
        st.success(f"File '{uploaded_file.name}' uploaded and loaded successfully.")
        
        # Initialize CSV Analyzer directly with DataFrame
        analyzer = CSVAnalyzer(df)
        analyzer.load_data()
        analyzer.clean_data()

        # Generate dataset summary
        dataset_summary = analyzer.get_summary()

        # Debug check for NoneType in dataset_summary
        if dataset_summary is None:
            st.error("Dataset summary is None. Check if the CSV file was loaded and cleaned correctly.")
        else:
            # Display dataset summary
            st.subheader("Dataset Summary Done")
  

            # Prepare inputs for the analysis
            inputs = {
                'csv_file': uploaded_file.name,  # Passing filename for reference
                'current_year': str(datetime.now().year),
                'topic': 'CSV Data Analysis',
                'dataset_summary': dataset_summary
            }

            # Run the CSV Analysis Crew with logs
            st.info("Running CSV Analysis... Please wait.")
            result = CSVAnalysisProject().crew().kickoff(inputs=inputs)
            
            if result is None:
                st.error("❌ CSV Analysis returned None.")
            else:
                st.success("✅ CSV Analysis Completed Successfully. Report saved in 'reports/'.")

            # Check if report exists and allow download
            report_path = 'reports/report.md'
            if os.path.exists(report_path):
                with open(report_path, "r") as file:
                    report_content = file.read()
                st.download_button(
                    label="📥 Download Report",
                    data=report_content,
                    file_name="report.md",
                    mime="text/markdown"
                )

    except Exception as e:
        st.error(f"An error occurred during analysis: {e}")
else:
    st.info("Please upload a CSV file to start the analysis.")
