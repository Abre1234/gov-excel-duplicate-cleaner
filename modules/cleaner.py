"""
Data Cleaner Module
Removes duplicate rows while preserving original data structure
"""

import pandas as pd
import numpy as np

class DataCleaner:
    """Cleans data by removing duplicate rows"""
    
    def __init__(self, df):
        """
        Initialize data cleaner
        
        Args:
            df (pandas.DataFrame): DataFrame to clean
        """
        self.df = df.copy()
        self.original_row_col = 'Original_Row_Number'
    
    def remove_duplicates(self):
        """
        Remove duplicate rows, keeping the first occurrence
        
        Returns:
            pandas.DataFrame: Cleaned DataFrame with duplicates removed
        """
        # Get columns to compare (exclude original row number)
        comparison_cols = [col for col in self.df.columns if col != self.original_row_col]
        
        # Normalize data for comparison
        normalized_df = self.df.copy()
        
        for col in comparison_cols:
            # Convert to string and strip whitespace for comparison
            normalized_df[col] = normalized_df[col].astype(str).str.strip()
            # Normalize empty values
            normalized_df[col] = normalized_df[col].replace(['', 'nan', 'NaN', 'None', 'NaT'], np.nan)
        
        # Remove duplicates based on normalized data, keeping first occurrence
        duplicate_mask = normalized_df.duplicated(subset=comparison_cols, keep='first')
        
        # Get cleaned DataFrame (original data, not normalized)
        cleaned_df = self.df[~duplicate_mask].copy()
        
        # Remove the Original_Row_Number column from the final output
        if self.original_row_col in cleaned_df.columns:
            cleaned_df = cleaned_df.drop(columns=[self.original_row_col])
        
        # Reset index
        cleaned_df = cleaned_df.reset_index(drop=True)
        
        return cleaned_df
    
    def get_cleaned_statistics(self, cleaned_df):
        """
        Get statistics about the cleaning operation
        
        Args:
            cleaned_df (pandas.DataFrame): Cleaned DataFrame
        
        Returns:
            dict: Statistics about the cleaning operation
        """
        original_count = len(self.df)
        cleaned_count = len(cleaned_df)
        removed_count = original_count - cleaned_count
        
        return {
            'original_count': original_count,
            'cleaned_count': cleaned_count,
            'removed_count': removed_count,
            'removal_percentage': (removed_count / original_count * 100) if original_count > 0 else 0
        }
