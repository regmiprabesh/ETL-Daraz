#import libraries
import pandas as pd
from services.log_service import log_progress

#Validate Data
def validation(df: pd.DataFrame):
    log_progress('Validation Started')
    """
    Function to check if the date is in a valid format
    """
    # Check if the DataFrame is empty
    if df.empty:
        log_progress('No Products Available! Aborting')
        return False
    
    # Check for duplicate products
    if not pd.Series(df['product_name']).is_unique:
        log_progress('Duplicate Product! Aborting')
        return False

    # Check for empty values
    if df.isnull().values.any():
        log_progress('Contains Null Value! Aborting')
        return False
    log_progress('Validation Completed')
    return True
