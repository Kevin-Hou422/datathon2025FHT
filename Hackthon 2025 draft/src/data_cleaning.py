import pandas as pd

def clean_ctg_data(file_path:str):
    report = []
    
    try:
        df = pd.read_excel(file_path)
        report.append(f"Loaded data with {df.shape[0]} rows and {df.shape[1]} columns.")
    except Exception as e:
        report.append(f"Error loading data: {e}")
        return None, report
    
    initial_shape = df.shape
    print(f"Initial data shape: {initial_shape}")
    
    df.drop_duplicates(inplace=True)
    report.append(f"Dropped duplicates. New shape: {df.shape}")
    
    for col in df.columns:
        if df[col].nunique == 1:
            df.drop(columns=[col], inplace=True)
            report.append(f"Dropped constant column: {col}")
            
    if df.isnull().sum().sum() > 0:
        for col in df.select_dtypes(include=['float64', 'int64']).columns:
            median_value = df[col].median()
            df[col].fillna(median_value, inplace=True)
            report.append(f"Filled missing values in {col} with median: {median_value}")
    else:
        report.append("No missing values found.")
        
    print(f"Final data shape: {df.shape}")
    print("-" * 40)
    return df, report            
    