# main.py

import pandas as pd
from database_utils import DatabaseConnector  
from data_cleaning import DataCleaning

if __name__ == "__main__":
    db_config = {}  # This could contain real config details when connecting to a real database
    db_conn = DatabaseConnector(db_config)
    
    engine = db_conn.init_db_engine()
    print("Initialized SQLAlchemy engine:", engine)

    # Sample DataFrame 
    sample_df = pd.DataFrame({'column1': [1, 2, 3], 'column2': ['a', 'b', 'c']})

    # Data cleaning
    cleaner = DataCleaning()
    cleaned_df = cleaner.clean_user_data(sample_df)  # Assume cleaned_df gets modified inside clean_user_data method
    
    if cleaned_df is not None:  # Check if it's not None
        # Upload data to the database
        db_conn.upload_to_db(cleaned_df, 'table_name_')
    else:
        print("Data cleaning did not return a DataFrame. Aborting upload.")
