# file: main.py
from data_preprocessing import preprocess_data
from clustering import train_kmeans, find_optimal_clusters
from visualization import visualize_clusters, setup_visualization_dir
import os

company_description_path = "data/input/defiance_data_V1_descriptions.csv"
directory = "data/tmp"
experiment_id = "exp007"
visualization_dir = f"data/output/visualizations/{experiment_id}"
columns = ["female", "gen_immigrant", "immigrant", "Solo Founder", "Serial Founder", "STEM", "female-stem", "indian-female-stem"]

columns = [c.lower().replace(" ", "_") for c in columns]
def main():
    setup_visualization_dir(visualization_dir)

    embeddings_reduced_df = preprocess_data(company_description_path, directory, columns)

    n_clusters_file = os.path.join(visualization_dir, "step1_determine_number_of_clusters.png")
    n_clusters = find_optimal_clusters(embeddings_reduced_df, n_clusters_file)  # Uncomment to find optimal clusters
    # n_clusters = 4

    labels, cluster_centers = train_kmeans(embeddings_reduced_df, n_clusters=n_clusters)
    embeddings_reduced_df['kmeans_labels'] = labels
    
    visualize_clusters(embeddings_reduced_df, cluster_centers, visualization_dir, columns, "Defiance Capital Unicorn, DM Analaysis")

if __name__ == "__main__":
    main()
