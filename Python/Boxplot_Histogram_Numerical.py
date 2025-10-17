import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the file
df = pd.read_csv("aerofit_treadmill_data.csv")

# Function for Numeric Analysis
def analyze_numeric(df, num_cols, target_col='Product'):
    
    for col in num_cols:
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        fig.suptitle(f"{col} Distribution by {target_col}", fontsize=14)
        
        # Boxplot
        sns.boxplot(data=df, x=target_col, y=col, ax=axes[0], palette='Set2')
        axes[0].set_title(f"{col} by Product (Boxplot)")
        axes[0].set_xlabel("")
        
        # Histogram
        sns.histplot(data=df, x=col, hue=target_col, multiple='stack', bins=20, ax=axes[1])
        axes[1].set_title(f"{col} Distribution (Histogram)")
        
        plt.tight_layout()
        plt.show()

# Run Numeric Analysis
numeric_columns = ['Age', 'Education', 'Usage', 'Fitness', 'Income', 'Miles']
analyze_numeric(df, num_cols=numeric_columns)