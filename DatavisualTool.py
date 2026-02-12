"""PROGRAM OF WEB SCRAPER WITH BeautifulSoup TO EXTRACT DATA(QUOTES) FROM DATASET
PROGRAM NAME: WEB SCRAPER
AUTHOR: AINEEN SAYYED
DATE CREATED: 6/02/2026"""
import pandas as pd
import plotly.express as px

import numpy as np


def create_visualizations(df):
    """
    Generates a suite of interactive plots from a dataframe.
    """
    # 1. Scatter Plot (Explaining Relationships)
    # Principle: Using position and color to show correlation
    fig1 = px.scatter(df, x="Feature_A", y="Target_Value",
                      color="Category", size="Intensity",
                      hover_data=['ID'],
                      title="Interactive Scatter: Feature A vs Target (Size=Intensity)")

    # 2. Distribution Plot (Understanding Spread)
    # Principle: Using histograms to identify skewness and outliers
    fig2 = px.histogram(df, x="Target_Value", color="Category",
                        marginal="box",  # Adds a box plot on top
                        title="Distribution of Target Values by Category")

    # 3. Trend Analysis (Time/Sequence)
    # Principle: Using lines to show continuity
    df_sorted = df.sort_values("Timeline")
    fig3 = px.line(df_sorted, x="Timeline", y="Feature_B", color="Category",
                   title="Trend Analysis: Feature B Over Time")

    # Displaying the plots
    fig1.show()
    fig2.show()
    fig3.show()


# --- EXECUTION BLOCK ---
if __name__ == "__main__":
    # Generating a mock dataset for demonstration
    np.random.seed(42)
    data = {
        'ID': range(100),
        'Timeline': pd.date_range(start='2023-01-01', periods=100, freq='D'),
        'Feature_A': np.random.randn(100).cumsum(),
        'Feature_B': np.random.rand(100) * 100,
        'Target_Value': np.random.randint(10, 100, size=100),
        'Intensity': np.random.rand(100) * 20,
        'Category': np.random.choice(['Alpha', 'Beta', 'Gamma'], size=100)
    }

    sample_df = pd.DataFrame(data)

    print("Generating interactive charts...")
    create_visualizations(sample_df)
    print("Done! Charts should open in your default browser.")