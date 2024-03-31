# Defiance Capital VC Unicorn - Deep Media AI Analysis

## Overview
This project aims to analyze and visualize the clustering of companies based on various attributes such as company descriptions, underdog status, gender representation, and immigration background of leadership. By leveraging text embeddings and clustering techniques, we provide insights into the landscape of companies in our dataset.

## Features
- **Data Preprocessing**: Convert company descriptions into numerical embeddings suitable for machine learning.
- **Dimensionality Reduction**: Apply UMAP to reduce the dimensionality of embeddings for visualization.
- **Clustering Analysis**: Use KMeans to cluster companies based on their reduced embeddings.
- **Attribute Highlighting**: Highlight companies in clusters based on attributes like underdog status, female leadership, and immigration background.
- **Visualization**: Generate interactive plots to visualize clusters and their attribute distributions.

## Requirements
- Python 3.8+
- pandas
- numpy
- scikit-learn
- plotly
- umap-learn
- kaleido (for static image export with Plotly)

## Installation
Clone this repository to your local machine:
```
git clone https://github.com/RijulGupta-DM/Breadcrumbsdefiance-capital-vc-datashare.git
cd Breadcrumbsdefiance-capital-vc-datashare
```

Install the required Python packages:
```
pip install -r requirements.txt
```

## Usage

### Data Preparation
1. Place the Defiance Capital VC analysis as a CSV file in this directory data/input/defiance_data_V1_descriptions.csv

### Running the Analysis
Execute the main script to start the analysis:
```
python main.py
```

### Customization
You can customize the analysis by modifying the `columns` variable in `main.py` to include any attributes of interest (e.g., `"female-immigrant"` for composite attributes).

## Contributing
Contributions to this project are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes.
4. Push to the branch.
5. Submit a pull request.

## Next Steps
1. Create more advanced LLM visualizations, such as word maps overlaid on company points.
2. Label the "underdog" filtered points with company names for better interpretation of data.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

Remember to replace placeholders like `https://github.com/yourusername/your-repository-name.git` with your actual repository URL and adjust any specific instructions or descriptions according to what your project does. This README provides a structured outline for collaborators and users to understand and work with your project effectively.
