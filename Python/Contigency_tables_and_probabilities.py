import pandas as pd

# Load the file
df = pd.read_csv("aerofit_treadmill_data.csv")

# Function for Two-Way Analysis (Categorical)
def analyze_two_way(df, cat_col, target_col='Product'):
    
    # Contingency Table
    table = pd.crosstab(df[target_col], df[cat_col],margins=True, margins_name="Total")
    total = table.loc["Total", "Total"]
    
    # Marginal probabilities (excluding the "Total" row/column)
    marginal_product = (table.loc[df[target_col].unique(), "Total"] / total) * 100
    marginal_category = (table.loc["Total", df[cat_col].unique()] / total) * 100

    # Conditional probabilities: P(category | product)
    conditional = table.loc[df[target_col].unique(), df[cat_col].unique()].div(table.loc[df[target_col].unique(), "Total"], axis=0) *100
    
    # Display tables
    print(f"\n===== {target_col} × {cat_col} =====")
    print("\nContingency Table:")
    print(table)
    print("\nMarginal Probabilities (Product):")
    print(marginal_product.round(1).astype(str) + "%")
    print("\nMarginal Probabilities (Category):")
    print(marginal_category.round(1).astype(str) + "%")
    print("\nConditional Probabilities (Category | Product):")
    print(conditional.round(1).astype(str) + "%")

# Run Categorical Analysis
categorical_columns = ['Gender', 'MaritalStatus']
for col in categorical_columns:
    analyze_two_way(df, cat_col=col)


