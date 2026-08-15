"""
Report Generator Module
Generates Excel reports and exports
"""

import pandas as pd
from io import BytesIO
from datetime import datetime

class ReportGenerator:
    """Generates various Excel reports"""
    
    def __init__(self):
        """Initialize report generator"""
        pass
    
    def generate_cleaned_excel(self, cleaned_df):
        """
        Generate Excel file with cleaned data
        
        Args:
            cleaned_df (pandas.DataFrame): Cleaned DataFrame
        
        Returns:
            bytes: Excel file as bytes
        """
        output = BytesIO()
        
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            cleaned_df.to_excel(writer, sheet_name='Cleaned Data', index=False)
        
        output.seek(0)
        return output.getvalue()
    
    def generate_duplicate_excel(self, duplicate_df):
        """
        Generate Excel file with duplicate rows
        
        Args:
            duplicate_df (pandas.DataFrame): DataFrame containing duplicate rows
        
        Returns:
            bytes: Excel file as bytes
        """
        output = BytesIO()
        
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            duplicate_df.to_excel(writer, sheet_name='Duplicate Rows', index=False)
        
        output.seek(0)
        return output.getvalue()
    
    def generate_duplicate_report(self, duplicate_info):
        """
        Generate comprehensive duplicate report
        
        Args:
            duplicate_info (dict): Dictionary containing duplicate analysis results
        
        Returns:
            bytes: Excel file as bytes
        """
        output = BytesIO()
        
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            # Summary sheet
            summary_data = {
                'Metric': [
                    'Report Generated',
                    'Total Rows',
                    'Total Columns',
                    'Unique Rows',
                    'Duplicate Rows',
                    'Duplicate Groups',
                    'Duplicate Percentage'
                ],
                'Value': [
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    duplicate_info['total_rows'],
                    duplicate_info['total_columns'],
                    duplicate_info['unique_rows'],
                    duplicate_info['duplicate_count'],
                    duplicate_info['duplicate_groups'],
                    f"{duplicate_info['duplicate_percentage']:.2f}%"
                ]
            }
            summary_df = pd.DataFrame(summary_data)
            summary_df.to_excel(writer, sheet_name='Summary', index=False)
            
            # Duplicate details sheet
            if not duplicate_info['duplicate_df'].empty:
                duplicate_info['duplicate_df'].to_excel(
                    writer, 
                    sheet_name='Duplicate Details', 
                    index=False
                )
                
                # Group summary sheet
                group_summary = duplicate_info['duplicate_df'].groupby('Duplicate_Group_ID').agg({
                    'Duplicate_Row': 'count',
                    'Total_Occurrences': 'first'
                }).reset_index()
                group_summary.columns = ['Duplicate_Group_ID', 'Duplicate_Count', 'Total_Occurrences']
                group_summary = group_summary.sort_values('Duplicate_Count', ascending=False)
                group_summary.to_excel(writer, sheet_name='Group Summary', index=False)
        
        output.seek(0)
        return output.getvalue()
