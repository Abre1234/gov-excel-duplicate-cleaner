"""
Utility Module
Common utility functions
"""

def format_number(num):
    """
    Format number with thousand separators
    
    Args:
        num (int): Number to format
    
    Returns:
        str: Formatted number
    """
    return f"{num:,}"

def calculate_percentage(part, total):
    """
    Calculate percentage
    
    Args:
        part (int): Part value
        total (int): Total value
    
    Returns:
        float: Percentage value
    """
    if total == 0:
        return 0.0
    return (part / total) * 100
