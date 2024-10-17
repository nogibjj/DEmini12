"""
Extract a dataset from a URL like Kaggle or data.gov. 
JSON or CSV formats tend to work well
"""


import os
# import pandas as pd

def extract(dataset1="ankulsharma150/marketing-analytics-project", 
            dataset2="prasertk/top-1000-instagram-influencers", 
            directory="data"):
    """Extracts multiple Kaggle datasets to the specified directory."""
    
    # Ensure the target directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Function to download a dataset from Kaggle
    def download_dataset(dataset_name):
        command = f"kaggle datasets download -d {dataset_name} --unzip -p {directory}"
        os.system(command)

    # Download both datasets
    download_dataset(dataset1)
    download_dataset(dataset2)

    # Handle first dataset: Instagram Data
    csv_path1 = os.path.join(directory, "instagram_Data.csv")
    if not os.path.exists(csv_path1):
        raise FileNotFoundError(f"{csv_path1} not found. ")
    # df1 = pd.read_csv(csv_path1)



    # Handle second dataset: Top 1000 Influencers
    csv_path2 = os.path.join(directory, "instagram_global_top_1000.csv")
    if not os.path.exists(csv_path2):
        raise FileNotFoundError(f"{csv_path2} not found. ")
    # df2 = pd.read_csv(csv_path2)


    return csv_path1, csv_path2

# Example usage
if __name__ == "__main__":
    extract()


