# file: clustering.py
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from kneed import KneeLocator

import plotly.graph_objects as go


def plot_elbow_method_with_plotly(K, ssd, optimal_k, output_file):
    """
    Plots the elbow method graph using Plotly and saves the plot as an image.

    Parameters:
    - K: Range of k values tested.
    - ssd: List of sum of squared distances for each k.
    - optimal_k: The optimal number of clusters determined.
    - output_file: Path to save the output image.
    """
    fig = go.Figure()

    # Adding the SSD line plot
    fig.add_trace(go.Scatter(x=list(K), y=ssd, mode='lines+markers', name='Sum of Squared Distances', marker=dict(color='blue')))

    # Marking the optimal k value
    fig.add_trace(go.Scatter(x=[optimal_k], y=[ssd[optimal_k-1]], mode='markers', name='Optimal K', marker=dict(color='red', size=10)))

    # Optional: Adding a vertical line for the optimal k (this approach is a workaround as Plotly does not have a direct method to draw vertical lines)
    fig.add_shape(type="line", x0=optimal_k, y0=min(ssd), x1=optimal_k, y1=max(ssd), line=dict(color="Red", width=2, dash="dash"))

    # Updating layout for better readability and aesthetics
    fig.update_layout(title='Elbow Method For Optimal K', xaxis_title='Number of clusters', yaxis_title='Sum of squared distances', showlegend=True)

    # Save the figure
    fig.write_image(output_file)


def find_optimal_clusters(data, output_file, max_k=16):
    """
    Finds the optimal number of clusters using the elbow method with automatic detection.

    Parameters:
    - data: DataFrame or array-like, input data for clustering.
    - max_k: int, maximum number of clusters to test.

    Returns:
    - int, the optimal number of clusters based on the elbow method.
    """
    ssd = []  # Sum of squared distances
    K = range(1, max_k+1)

    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=42).fit(data)
        ssd.append(kmeans.inertia_)

    # Using the KneeLocator to find the elbow point
    knee_locator = KneeLocator(K, ssd, curve="convex", direction="decreasing")

    optimal_k = knee_locator.elbow

    plot_elbow_method_with_plotly(K, ssd, optimal_k, output_file)

    return optimal_k

def train_kmeans(data, n_clusters=5, random_state=42):
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    labels = kmeans.fit_predict(data[['x', 'y']])
    return labels, kmeans.cluster_centers_
