import pandas as pd
import os
import chardet

class CSVAnalyzer:
    """Handles CSV file processing: loading, cleaning, and saving"""

    def __init__(self, data):
        """Initialize with either a CSV file path or a DataFrame"""
        if isinstance(data, str):  # If file path
            self.file_path = data
            self.df = None
        elif isinstance(data, pd.DataFrame):  # If DataFrame
            self.file_path = None
            self.df = data
        else:
            raise ValueError("Invalid input type. Must be a file path or a Pandas DataFrame.")

    def detect_encoding(self):
        """Detect file encoding dynamically"""
        if self.file_path:
            with open(self.file_path, 'rb') as f:
                raw_data = f.read()
                result = chardet.detect(raw_data)
                return result['encoding']
        return None

    def load_data(self):
        """Load CSV data with encoding detection or return existing DataFrame"""
        if self.df is not None:
            return self.df
        elif self.file_path:
            encoding = self.detect_encoding()
            try:
                self.df = pd.read_csv(self.file_path, encoding=encoding)
                print(f"✅ CSV loaded successfully with encoding: {encoding}")
            except Exception as e:
                print(f"⚠️ Error loading CSV with detected encoding, trying default: {e}")
                self.df = pd.read_csv(self.file_path)  # Fallback encoding
            return self.df
        else:
            raise ValueError("No data source available for loading.")

    def clean_data(self):
        """Fill missing values appropriately based on data type."""
        if self.df is not None:
            # Fill numeric columns with 0
            numeric_columns = self.df.select_dtypes(include=['number']).columns
            self.df[numeric_columns] = self.df[numeric_columns].fillna(0)

            # Fill categorical columns with 'Unknown'
            categorical_columns = self.df.select_dtypes(include=['object', 'category']).columns
            self.df[categorical_columns] = self.df[categorical_columns].fillna("Unknown")

            print("🧹 Missing values handled: Numeric columns filled with 0, categorical columns filled with 'Unknown'.")
            return self.df
        print("⚠️ No data to clean.")
        return None

    def get_summary(self):
        """Generate a quick summary of the dataset"""
        if self.df is not None:
            summary = {
                "Rows": int(self.df.shape[0]),
                "Columns": int(self.df.shape[1]),
                "Missing Values": int(self.df.isnull().sum().sum()),
                "Sample Data": self.df.head().astype(str).to_dict()
            }
            print("✅ Dataset summary generated:", summary)
            return summary
        print("⚠️ No data loaded for summary.")
        return None
