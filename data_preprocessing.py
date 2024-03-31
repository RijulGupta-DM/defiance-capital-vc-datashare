# file: data_preprocessing.py
import pandas as pd
from utils.csv_utils import process_company_description_csv, generate_and_save_embeddings, load_embeddings
# from utils.cluster_utils import  reduce_dimensions

from umap import UMAP
import pandas as pd

def reduce_dimensions(embeddings_df, columns):
    # Extract the numeric embedding columns
    numeric_data = embeddings_df.drop(columns=columns)  # Adjust if you have more non-numeric columns
    
    # Perform UMAP dimensionality reduction
    reducer = UMAP(n_components=2, random_state=42)
    embeddings_reduced = reducer.fit_transform(numeric_data)
    
    # Create a new DataFrame for the reduced data
    reduced_df = pd.DataFrame(embeddings_reduced, index=embeddings_df.index, columns=['x', 'y'])
    
    # Reattach the 'underdog' column (and any others you need)
    # reduced_df['underdog'] = embeddings_df['underdog']
    for column_name in columns:
        reduced_df[column_name] = embeddings_df[column_name]
    
    return reduced_df



def preprocess_data(company_description_path, directory, columns):
    companies_to_search = process_company_description_csv(company_description_path, directory)
    generate_and_save_embeddings(directory)
    embeddings_df = load_embeddings(directory, columns)
    embeddings_reduced_df = reduce_dimensions(embeddings_df, columns)
    return embeddings_reduced_df
