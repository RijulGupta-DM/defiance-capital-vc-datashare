import csv
import os
import openai
import json
import pandas as pd

from models.unicorncompany import UnicornCompany

def process_csv(data_path, directory):
    companies = []
    with open(data_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            company_name = row.get('Company', row.get('company'))  # Ensure you get the company name correctly
            company_json_path = f'{directory}/company_jsons/{company_name.replace(" ", "_").replace("/", "_").replace("?", "")}.json'
            
            # Check if JSON already exists for the company
            if os.path.exists(company_json_path):
                print(f"Skipping {company_name}, JSON already exists.")
                continue
            
            # If JSON does not exist, create a new UnicornCompany object and save it
            company = UnicornCompany(directory, **row)
            company.save_to_json(include_embedding_text=True)
            print(f"Processed and saved: {company.company}")
            companies.append(company)

    return companies


def process_company_description_csv(data_path, directory):
    companies = []
    with open(data_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            company_name = row.get('Company', row.get('Company'))  # Ensure you get the company name correctly
            company_json_path = f'{directory}/company_jsons/{company_name.replace(" ", "_").replace("/", "_").replace("?", "")}.json'
            
            # Check if JSON already exists for the company
            if os.path.exists(company_json_path):
                print(f"Skipping {company_name}, JSON already exists.")
                continue
            
            # If JSON does not exist, create a new UnicornCompany object and save it
            company = UnicornCompany(directory, **row)
            company.save_to_json(include_embedding_text=True)
            print(f"Processed and saved: {company.company}")
            companies.append(company)

    return companies


# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )

def generate_and_save_embeddings(directory):
    openai.api_key = ""  # Replace with your actual API key, or ensure it's set in your environment variables
    
    for filename in os.listdir(f'{directory}/company_jsons'):
        if filename.endswith(".json"):
            print(os.path.join(f'{directory}/company_jsons', filename))
            json_path = os.path.join(f'{directory}/company_jsons', filename)
            with open(json_path, 'r') as f:
                company_data = json.load(f)

            # Check if the embedding already exists
            if "embedding" not in company_data:
                # Generate the embedding
                response = openai.Embedding.create(
                    input=company_data['embedding_text'],
                    model="text-embedding-3-small"  # Use the correct model identifier
                )
                # Save the embedding back to the company data
                company_data['embedding'] = response['data'][0]['embedding']

                # print(company_data)
                
                # Save the updated company data back to JSON
                with open(json_path, 'w') as f:
                    json.dump(company_data, f, indent=4)
                
                print(f"Updated {filename} with embedding.")
            else:
                print(f"Embedding already exists for {filename}.")


# def load_embeddings(directory, columns):
#     embeddings = []
#     attributes = {column: [] for column in columns}  # Prepare to store attributes for each column
#     company_names = []

#     for filename in os.listdir(f'{directory}/company_jsons'):
#         if filename.endswith(".json"):
#             json_path = os.path.join(f'{directory}/company_jsons', filename)
#             with open(json_path, 'r') as f:
#                 company_data = json.load(f)
                
#                 # Skip if company_description is not available or is "#N/A"
#                 if company_data.get("company_description", "#N/A") == "#N/A":
#                     continue

#                 # Process embedding
#                 if "embedding" in company_data:
#                     embeddings.append(company_data['embedding'])
#                     company_names.append(company_data['company'])
                    
#                     # Process each attribute according to columns list
#                     for column in columns:
#                         # Assuming boolean TRUE/FALSE values, convert them appropriately
#                         # Adjust logic here if the data types or expected values differ
#                         attribute_value = company_data.get(column, False)
#                         attribute_value = True if attribute_value == "TRUE" else False
#                         attributes[column].append(attribute_value)

#     # Initialize DataFrame with embeddings and company names
#     embeddings_df = pd.DataFrame(embeddings, index=company_names)

#     # Add each attribute column to the DataFrame
#     for column, values in attributes.items():
#         embeddings_df[column] = values

#     return embeddings_df


def load_embeddings(directory, columns):
    embeddings = []
    attributes = {column: [] for column in columns}  # Prepare to store attributes for each column
    company_names = []

    for filename in os.listdir(f'{directory}/company_jsons'):
        if filename.endswith(".json"):
            json_path = os.path.join(f'{directory}/company_jsons', filename)
            with open(json_path, 'r') as f:
                company_data = json.load(f)
                
                # Skip if company_description is not available or is "#N/A"
                if company_data.get("company_description", "#N/A") == "#N/A":
                    continue

                # Process embedding
                if "embedding" in company_data:
                    embeddings.append(company_data['embedding'])
                    company_names.append(company_data['company'])
                    
                    # Process each attribute according to columns list
                    for column in columns:
                        # Check for composite column names
                        if '-' in column:
                            flags = column.split('-')
                            # Set attribute_value to True only if all specified flags are True
                            attribute_value = all(company_data.get(flag, "0") == "1" for flag in flags)
                        else:
                            # For single flag, process as before
                            attribute_value = company_data.get(column, "0") == '1'

                        attributes[column].append(attribute_value)

    # Initialize DataFrame with embeddings and company names
    embeddings_df = pd.DataFrame(embeddings, index=company_names)

    # Add each attribute column to the DataFrame
    for column, values in attributes.items():
        embeddings_df[column] = values

    return embeddings_df