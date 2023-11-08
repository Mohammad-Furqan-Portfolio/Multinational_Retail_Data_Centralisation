# data_cleaning.py
import pandas as pd

class DataCleaning:
    def __init__(self):
        pass
    
    def clean_csv_data(self, csv_data):
        # Placeholder for code to clean CSV data
        pass
    
    def clean_api_data(self, api_data):
        # Placeholder for code to clean API data
        pass
    
    def clean_s3_data(self, s3_data):
        # Placeholder for code to clean S3 data
        pass

    def clean_user_data(self, df):
        df.dropna(inplace=True)  # Drop NULL values as an example
        # Add more cleaning logic here
        return df

    def clean_card_data(self, df):
        # Your cleaning logic here
        df.dropna(inplace=True)  # Remove rows with NULL values
        # Other cleaning operations can go here
        return df
    
    def clean_store_data(self,df):
        df.drop(columns='lat',inplace=True)
        df                  =  self.clean_invalid_date(df,'opening_date')                     
        df['staff_numbers'] =  pd.to_numeric( df['staff_numbers'].apply(self.remove_char_from_string),errors='coerce', downcast="integer") 
        df.dropna(subset = ['staff_numbers'],how='any',inplace= True)
        return df


    def convert_product_weights(self, products_df):
        def convert_weight(weight_str):
            weight_str = weight_str.lower()
            if 'kg' in weight_str:
                return float(weight_str.replace('kg', '').strip())
            if 'g' in weight_str:
                return float(weight_str.replace('g', '').strip()) / 1000
            if 'ml' in weight_str:
                return float(weight_str.replace('ml', '').strip()) / 1000
            return 0.0  # or other error handling
        
        products_df['Weight'] = products_df['Weight'].apply(convert_weight)
        return products_df

    def clean_products_data(self, products_df):
        # Perform additional cleaning, e.g., drop NA, remove outliers, etc.
        products_df.dropna(inplace=True)
        # ... more cleaning ...
        return products_df
    
    def clean_orders_data(self, orders_df):
        # Remove unnecessary columns
        orders_df.drop(['first_name', 'last_name', '1'], axis=1, inplace=True)
        
        return orders_df
