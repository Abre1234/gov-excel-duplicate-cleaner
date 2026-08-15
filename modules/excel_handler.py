"""
Excel Handler Module
Handles reading and processing of Excel files
"""

import pandas as pd
from io import BytesIO
import openpyxl

class ExcelHandler:
    """Handles Excel file operations"""
    
    def __init__(self, uploaded_file):
        """
        Initialize Excel handler with uploaded file
        
        Args:
            uploaded_file: Streamlit UploadedFile object
        """
        self.uploaded_file = uploaded_file
        self.file_bytes = BytesIO(uploaded_file.getvalue())
    
    def get_sheet_names(self):
        """
        Get list of sheet names in the workbook
        
        Returns:
            list: List of sheet names
        """
        try:
            # Reset file pointer
            self.file_bytes.seek(0)
            excel_file = pd.ExcelFile(self.file_bytes)
            return excel_file.sheet_names
        except Exception as e:
            raise ValueError(f"Unable to read Excel file: {str(e)}")
    
    def read_sheet(self, sheet_name=None):
        """
        Read a specific sheet from the Excel file
        
        Args:
            sheet_name (str): Name of the sheet to read. If None, reads first sheet.
        
        Returns:
            pandas.DataFrame: DataFrame containing the sheet data
        """
        try:
            # Reset file pointer
            self.file_bytes.seek(0)
            
            # Read the Excel sheet
            if sheet_name:
                df = pd.read_excel(self.file_bytes, sheet_name=sheet_name)
            else:
                df = pd.read_excel(self.file_bytes)
            
            # Check if DataFrame is empty
            if df.empty:
                return None
            
            # Add original row numbers (1-indexed, accounting for header)
            df.insert(0, 'Original_Row_Number', range(2, len(df) + 2))
            
            return df
            
        except Exception as e:
            raise ValueError(f"Unable to read sheet '{sheet_name}': {str(e)}")
    
    def validate_file(self):
        """
        Validate that the uploaded file is a valid Excel file
        
        Returns:
            tuple: (is_valid, error_message)
        """
        try:
            self.file_bytes.seek(0)
            pd.ExcelFile(self.file_bytes)
            return True, None
        except Exception as e:
            return False, str(e)
