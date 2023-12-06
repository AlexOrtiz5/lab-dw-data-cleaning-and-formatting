import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def handle_null_values(df):
    df = df.dropna()
    return df

def handle_duplicates(df):
    df = df.drop_duplicates(keep='first')
    return df

def convert_complaints(num):
    if isinstance(num, str):
        return int(num.split('/')[1])
    return 0

def format_data(df):
    df['Number of Open Complaints'] = df['Number of Open Complaints'].apply(convert_complaints)
    df = df.round(2)
    return df

def save_cleaned_data(df, output_file):
    df.to_csv(output_file, index=False)
