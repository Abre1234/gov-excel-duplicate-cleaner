"""
Duplicate Detector Module
Detects duplicate rows by comparing all columns
"""

import pandas as pd
import numpy as np

class DuplicateDetector:
    """Detects duplicate rows in a DataFrame"""
    
    def __init__(self, df):
        """
        Initialize duplicate detector
        
        Args:
            df (pandas.DataFrame): DataFrame to analyze
        """
        self.df = df.copy()
        self.original_row_col = 'Original_Row_Number'
    
    def normalize_for_comparison(self, df):
        """
        Normalize data for duplicate comparison while preserving original values
        
        Args:
            df (pandas.DataFrame): DataFrame to normalize
        
        Returns:
            pandas.DataFrame: Normalized DataFrame for comparison
        """
        normalized_df = df.copy()
        
        # Exclude the original row number column from comparison
        comparison_cols = [col for col in df.columns if col != self.original_row_col]
        
        for col in comparison_cols:
            # Convert to string and strip whitespace
            normalized_df[col] = normalized_df[col].astype(str).str.strip()
            
            # Normalize empty values
            normalized_df[col] = normalized_df[col].replace(['', 'nan', 'NaN', 'None', 'NaT'], np.nan)
        
        return normalized_df
    
    def detect_duplicates(self):
        """
        Detect duplicate rows by comparing all columns
        
        Returns:
            dict: Dictionary containing duplicate analysis results
        """
        # Get columns to compare (exclude original row number)
        comparison_cols = [col for col in self.df.columns if col != self.original_row_col]
        
        # Normalize data for comparison
        normalized_df = self.normalize_for_comparison(self.df)
        
        # Detect duplicates (keeping first occurrence)
        duplicate_mask = normalized_df.duplicated(subset=comparison_cols, keep='first')
        
        # Get duplicate rows
        duplicate_rows = self.df[duplicate_mask].copy()
        
        # If no duplicates found
        if len(duplicate_rows) == 0:
            return {
                'total_rows': len(self.df),
                'total_columns': len(comparison_cols),
                'unique_rows': len(self.df),
                'duplicate_count': 0,
                'duplicate_percentage': 0.0,
                'duplicate_groups': 0,
                'duplicate_df': pd.DataFrame(),
                'original_df': self.df
            }
        
        # Create duplicate group IDs
        # For each duplicate row, find its original (first occurrence)
        duplicate_info_list = []
        
        for idx, row in duplicate_rows.iterrows():
            # Find the first occurrence (original) of this duplicate
            row_data = row[comparison_cols]
            
            # Find matching rows (including the original)
            normalized_row = normalized_df.loc[idx, comparison_cols]
            matches = normalized_df[comparison_cols].apply(
                lambda x: x.equals(normalized_row), axis=1
            )
            
            matching_indices = self.df[matches].index.tolist()
            original_idx = matching_indices[0]  # First occurrence is the original
            
            duplicate_info_list.append({
                'index': idx,
                'original_index': original_idx,
                'original_row_number': self.df.loc[original_idx, self.original_row_col],
                'duplicate_row_number': row[self.original_row_col]
            })
        
        # Create a mapping of original indices to duplicate group IDs
        original_to_group = {}
        group_counter = 1
        
        for info in duplicate_info_list:
            original_idx = info['original_index']
            if original_idx not in original_to_group:
                original_to_group[original_idx] = f"DUP-{group_counter:03d}"
                group_counter += 1
        
        # Add duplicate group information to duplicate rows
        for info in duplicate_info_list:
            idx = info['index']
            original_idx = info['original_index']
            
            duplicate_rows.loc[idx, 'Duplicate_Group_ID'] = original_to_group[original_idx]
            duplicate_rows.loc[idx, 'Original_Row_Number_Ref'] = info['original_row_number']
            duplicate_rows.loc[idx, 'Duplicate_Row_Number'] = info['duplicate_row_number']
        
        # Count occurrences per group
        group_counts = duplicate_rows['Duplicate_Group_ID'].value_counts().to_dict()
        duplicate_rows['Occurrences_In_Group'] = duplicate_rows['Duplicate_Group_ID'].map(
            lambda x: group_counts[x] + 1  # +1 to include the original
        )
        
        # Reorder columns for better readability
        ordered_cols = ['Duplicate_Group_ID', 'Original_Row_Number_Ref', 'Duplicate_Row_Number', 
                       'Occurrences_In_Group'] + comparison_cols
        duplicate_rows = duplicate_rows[ordered_cols]
        
        # Rename columns for clarity
        duplicate_rows = duplicate_rows.rename(columns={
            'Original_Row_Number_Ref': 'Original_Row',
            'Duplicate_Row_Number': 'Duplicate_Row',
            'Occurrences_In_Group': 'Total_Occurrences'
        })
        
        # Calculate statistics
        total_rows = len(self.df)
        duplicate_count = len(duplicate_rows)
        unique_rows = total_rows - duplicate_count
        duplicate_percentage = (duplicate_count / total_rows * 100) if total_rows > 0 else 0
        duplicate_groups = len(original_to_group)
        
        return {
            'total_rows': total_rows,
            'total_columns': len(comparison_cols),
            'unique_rows': unique_rows,
            'duplicate_count': duplicate_count,
            'duplicate_percentage': duplicate_percentage,
            'duplicate_groups': duplicate_groups,
            'duplicate_df': duplicate_rows,
            'original_df': self.df,
            'comparison_columns': comparison_cols
        }
