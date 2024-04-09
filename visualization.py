# file: visualization.py
import os
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import numpy as np
from scipy.spatial.distance import cdist

pio.templates.default = "seaborn"

def setup_visualization_dir(visualization_dir):
    if not os.path.exists(visualization_dir):
        os.makedirs(visualization_dir)

def wrap_text(text, width):
    """
    Wraps text at a specified width.

    Parameters:
    - text: The text to wrap.
    - width: The maximum width of the text, in characters.

    Returns:
    - A wrapped text string.
    """
    if len(text) <= width:
        return text
    last_space = text.rfind(' ', 0, width)
    if last_space == -1:
        # No spaces found, force break at width
        return text[:width] + "\n" + wrap_text(text[width:], width)
    return text[:last_space] + "\n" + wrap_text(text[last_space+1:], width)


def visualize_clusters(embeddings_reduced_df, cluster_centers, visualization_dir, columns, plot_title="KMeans Clustering"):
    # Functionality for visualization as shown in the original script


    # Prepare the file to list companies by cluster
    cluster_listing_file_path = os.path.join(visualization_dir, "step2_determine_company_clusters.txt")
    with open(cluster_listing_file_path, 'w') as cluster_file:

        # Iterate through each cluster
        for cluster_label in np.unique(embeddings_reduced_df['kmeans_labels']):
            cluster_file.write(f"Cluster {cluster_label}:\n")

            # Subset dataframe to current cluster
            df_subset = embeddings_reduced_df[embeddings_reduced_df['kmeans_labels'] == cluster_label]
            
            # Calculate distances to cluster center
            cluster_center = cluster_centers[cluster_label]
            distances = np.linalg.norm(df_subset[['x', 'y']] - cluster_center, axis=1)
            df_subset['distance_to_center'] = distances
            
            # Sort companies in cluster by distance to center
            sorted_companies = df_subset.sort_values(by='distance_to_center')

            current_line = ""
            for company in sorted_companies.index:
                if len(current_line) + len(company) + 2 > 120:  # 2 accounts for ", "
                    cluster_file.write(wrap_text(current_line, 120) + "\n")
                    current_line = company + ", "
                else:
                    current_line += company + ", "

            # Write any remaining text for the last line in the cluster
            if current_line:
                cluster_file.write(wrap_text(current_line.rstrip(', '), 120) + "\n\n")  # Remove trailing comma and space

    # Mapping 'underdog' status to opacity values
    # embeddings_reduced_df['opacity'] = embeddings_reduced_df['underdog'].apply(lambda x: 1 if x else 0.2)

    # Generating a color scale for the kmeans_labels
    num_clusters = embeddings_reduced_df['kmeans_labels'].nunique()
    color_scale = px.colors.qualitative.Set1[:num_clusters]


    # Custom function to map each cluster label to a color
    def get_color(label):
        return color_scale[label % len(color_scale)]
        

    # Visualization for KMeans with Underdog Highlighting
    fig_kmeans = go.Figure()

    # Adding one trace per cluster for clean legend
    for label in sorted(embeddings_reduced_df['kmeans_labels'].unique()):
        df_subset = embeddings_reduced_df[embeddings_reduced_df['kmeans_labels'] == label]
        fig_kmeans.add_trace(go.Scatter(
            x=df_subset['x'], 
            y=df_subset['y'],
            mode='markers',
            marker=dict(color=get_color(label), size=12, opacity=0.8, line=dict(width=2, color='DarkSlateGrey')),
            name=f"Cluster {label}"
        ))


    # Update layout for better readability and aesthetics
    fig_kmeans.update_layout(
        title=plot_title + " - LLM Embeddings Clusters",
        xaxis_title='X',
        yaxis_title='Y',
        legend_title='Cluster Number',
        showlegend=False,
    )

    # Find the closest data points to the cluster centers
    closest_points = np.argmin(cdist(embeddings_reduced_df[['x', 'y']], cluster_centers), axis=0)
    closest_companies = embeddings_reduced_df.index[closest_points]

    fig_kmeans.write_image(f"{visualization_dir}/step3_visualize_clusters.png")

    # Add text annotations for cluster number and closest company
    for i, cluster_label in enumerate(sorted(embeddings_reduced_df['kmeans_labels'].unique())):
        closest_company = embeddings_reduced_df.loc[closest_companies[i]]
        pos = closest_company[['x', 'y']]
        
        # Attempting to ensure newline is respected by using <br> for HTML-like newline
        annotation_text = f"Cluster {cluster_label}<br>{closest_companies[i]}"
        fig_kmeans.add_annotation(x=pos['x'], y=pos['y'], text=annotation_text,
                                  showarrow=True, arrowhead=1, ax=0, ay=-30,
                                  font=dict(family="Arial, sans-serif", size=14, color="white"),
                                  bgcolor="rgba(0,0,0,0.5)")  # Semi-transparent black background for the text


    fig_kmeans.write_image(f"{visualization_dir}/step4_visualize_clusters_with_tags.png")

    # Generating a color scale for the kmeans_labels
    num_clusters = embeddings_reduced_df['kmeans_labels'].nunique()
    color_scale = px.colors.qualitative.Set1[:num_clusters]

# Other visualizations
# TODO: Visualize words/tags from company description the clustering graph - use this on all the following graphs to help understand where the company/dots lie

# Underdogs
# TODO: Add statistics for each graph - e.g. percentage within cluster that have underdog
# 
    # Visualization for KMeans with Underdog Highlighting


    for column_idx, column_name in enumerate(columns):

        # Example of creating a combined label for color mapping
        embeddings_reduced_df[f'cluster_{column_name}'] = embeddings_reduced_df.apply(lambda x: f"{x['kmeans_labels']}_{f'{column_name}' if x[f'{column_name}'] else f'Non-{column_name}'}", axis=1)

        # Mapping 'underdog' status to opacity values
        embeddings_reduced_df[f'opacity_{column_name}'] = embeddings_reduced_df[f'{column_name}'].apply(lambda x: 1 if x else 0.2)

        columns_dir = os.path.join(visualization_dir, "filters")
        setup_visualization_dir(columns_dir)
        fig_kmeans = go.Figure()

        for label in sorted(embeddings_reduced_df['kmeans_labels'].unique()):
            df_subset = embeddings_reduced_df[embeddings_reduced_df['kmeans_labels'] == label]
            
            # Add scatter trace for each company
            for i, row in df_subset.iterrows():
                fig_kmeans.add_trace(go.Scatter(
                    x=[row['x']], 
                    y=[row['y']],
                    mode='markers',
                    marker=dict(
                        color=get_color(label), 
                        size=12, 
                        opacity=0.8 if row[column_name] else 0.2,  # Apply conditional opacity
                        line=dict(width=2, color='DarkSlateGrey')
                    )
                ))


        # Update layout for better readability and aesthetics
        fig_kmeans.update_layout(
            title=plot_title + f" - LLM Embeddings Clusters, {column_name}",
            xaxis_title='X',
            yaxis_title='Y',
            legend_title='Cluster Number',
            showlegend=False
        )

        # Add text annotations for cluster number and closest company
        for i, cluster_label in enumerate(sorted(embeddings_reduced_df['kmeans_labels'].unique())):
            closest_company = embeddings_reduced_df.loc[closest_companies[i]]
            pos = closest_company[['x', 'y']]
            
            # Attempting to ensure newline is respected by using <br> for HTML-like newline
            annotation_text = f"Cluster {cluster_label}<br>{closest_companies[i]}"
            fig_kmeans.add_annotation(x=pos['x'], y=pos['y'], text=annotation_text,
                                    showarrow=True, arrowhead=1, ax=0, ay=-30,
                                    font=dict(family="Arial, sans-serif", size=14, color="white"),
                                    bgcolor="rgba(0,0,0,0.5)")  # Semi-transparent black background for the text


        # Save the figure with underdog highlighting
        fig_kmeans.write_image(f"{columns_dir}/step5_{str(column_idx).zfill(3)}_visualize_clusters_with_filters_{column_name}.png")


    pass
