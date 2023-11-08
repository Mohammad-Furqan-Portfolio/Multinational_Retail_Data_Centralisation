# data_extraction.py
import csv
import requests
import tabula
import pandas as pd
import boto3

class DataExtractor:

    def __init__(self):
        self.header = {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}
        self.num_stores_api_endpoint = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'

    def from_csv(self, file_path):
        # Placeholder for extracting from CSV
        pass

    def from_api(self, api_url):
        # Placeholder for extracting from an API
        pass

    def from_s3_bucket(self, s3_url):
        # Placeholder for extracting from an S3 bucket
        pass

    def read_rds_table(self, db_conn, table_name):
        engine = db_conn.init_db_engine()
        df = pd.read_sql(f"SELECT * FROM {table_name}", engine)
        return df

    def retrieve_pdf_data(self, pdf_url):
        response = requests.get(pdf_url)
        if response.status_code == 200:
            with open("temp.pdf", "wb") as f:
                f.write(response.content)
            dfs = tabula.read_pdf("temp.pdf", pages="all", multiple_tables=True)
            return pd.concat(dfs, ignore_index=True)
        else:
            print("Failed to download PDF")
            return None
        
    def extract_from_s3(self, s3_url):
        bucket_name = "data-handling-public"
        file_name = "products.csv"
        s3 = boto3.client('s3')

        # Download the CSV file from S3
        s3.download_file(bucket_name, file_name, '/tmp/products.csv')
        
        # Load the CSV file into a DataFrame and return
        return pd.read_csv('/tmp/products.csv')

    def retrieve_stores_data(self):
        num_stores = []
        try:
            store_number = self.list_number_of_stores()
        except Exception as e:
            print(f"Error getting store number: {e}")
            return None

        for i in range(1, store_number + 1):
            api_url_base = f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{i}'
            response = requests.get(api_url_base, headers=self.header)
            
            if response.status_code != 200:
                print(f"Failed to get data for store {i}")
                continue
            
            num_stores.append(pd.json_normalize(response.json()))
            
        return pd.concat(num_stores)

    def list_number_of_stores(self):
        response = requests.get(self.num_stores_api_endpoint, headers=self.header)
        if response.status_code == 200:
            return response.json().get('number_stores', None)
        else:
            response.raise_for_status()




