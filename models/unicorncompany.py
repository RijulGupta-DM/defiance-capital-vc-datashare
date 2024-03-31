import os
import json

class UnicornCompany:
    def __init__(self, directory, **kwargs):
        self.directory = directory
        # Set all attributes from kwargs, allowing for any CSV column names
        for key, value in kwargs.items():
            new_key = key.replace(" ", "_").lower()
            setattr(self, new_key, value)

        # Initialize description and json_path to empty strings if not present in kwargs
        self.description = kwargs.get('description', '')
        self.json_path = kwargs.get('json_path', '')

    def save_to_json(self, include_embedding_text=False):
        if not os.path.exists(f'{self.directory}/company_jsons'):
            os.makedirs(f'{self.directory}/company_jsons')
        self.json_path = f'{self.directory}/company_jsons/{self.company.replace(" ", "_").replace("/", "_").replace("?", "")}.json'  
        
        # Check if include_embedding_text flag is True, if so, add the embedding text to the data to be saved
        data_to_save = {key: value for key, value in self.__dict__.items() if key not in ['json_path']}
        if include_embedding_text:
            data_to_save['embedding_text'] = self.to_embedding_text()
        
        with open(self.json_path, 'w') as f:
            json.dump(data_to_save, f, indent=4)

    def to_embedding_text(self):
        return self.company_description
        # Information section
        # info_section = f"Company Information\nYear Founded: {self.year_founded}, Industry: {self.industry}, Company: {self.company}.\n\n"
        
        # # Outcome Section
        # outcome_section = "Company Outcome\n"
        # outcomes = [
        #     f"Years to Unicorn: {self.yrs_to_unicorn}" if hasattr(self, 'yrs_to_unicorn') and self.yrs_to_unicorn else "",
        #     "Raised from top 20 (>1% Market Share)" if hasattr(self, 'raised_from_top_20') and self.raised_from_top_20 else "",
        #     f"Seed Investors: {self.seed_investors}" if hasattr(self, 'seed_investors') and self.seed_investors else ""
        # ]
        # outcome_section += ", ".join(filter(None, outcomes)) + ".\n\n"

        # # Founders Section
        # founders_section = "Founders Section\n"
        # founders_details = [
        #     f"Founders: {self.founders}" if hasattr(self, 'founders') and self.founders else "",
        #     "Underdog" if hasattr(self, 'underdog') and self.underdog else "",
        #     "Female" if hasattr(self, 'female') and self.female else "",
        #     f"Heritage: {self.heritage}" if hasattr(self, 'heritage') and self.heritage else "",
        #     f"Ethnicity: {self.ethnicity}" if hasattr(self, 'ethnicity') and self.ethnicity else "",
        #     "Solo Founder" if hasattr(self, 'solo_founder') and self.solo_founder else "",
        #     "STEM CEO" if hasattr(self, 'stem_ceo') and self.stem_ceo else ""
        # ]
        # founders_section += ", ".join(filter(None, founders_details)) + "."

        # # Combining all sections
        # embedding_text = f"{info_section} {outcome_section} {founders_section}"
        # return embedding_text

