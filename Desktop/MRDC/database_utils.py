# database_utils.py

import pandas as pd
import yaml
from sqlalchemy import create_engine

class DataCleaning:
    def clean_user_data(self, df):
        # Your data cleaning logic here.
        # For example:
        df.dropna(inplace=True)  # Just an example operation.
        
        return df

class DatabaseConnector:
    def __init__(self, db_config=None):
        self.db_config = db_config
    
    def read_db_creds(self):
        with open('db_creds.yaml', 'r') as f:
            return yaml.safe_load(f)
    
    def init_db_engine(self):
        creds = self.read_db_creds()
        engine_str = f"postgresql+psycopg2://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
        engine = create_engine(engine_str)
        return engine

    def upload_to_db(self, df, table_name):
        engine = self.init_db_engine()
        df.to_sql(table_name, engine, if_exists='replace')

    def list_db_tables(self):
        engine = self.init_db_engine()
        return engine.table_names()





