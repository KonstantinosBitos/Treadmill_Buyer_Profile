import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the file
df = pd.read_csv("aerofit_treadmill_data.csv")

#Create all the charts
plt.figure(figsize=(6,4))
sns.barplot(x='Product', y='Income', data=df, estimator='mean', errorbar=None)
plt.title("Average Income per Product")
plt.ylabel("Average Income ($)")
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x='Product', y='Age', data=df, estimator='mean', errorbar=None)
plt.title("Average Age per Product")
plt.ylabel("Average Age")
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x='Product', y='Usage', data=df, estimator='mean', errorbar=None)
plt.title("Average Weekly Usage per Product")
plt.ylabel("Average Usage (times/week)")
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x='Product', y='Fitness', data=df, estimator='mean', errorbar=None)
plt.title("Average Fitness Level per Product")
plt.ylabel("Average Fitness (1–5)")
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x='Product', y='Miles', data=df, estimator='mean', errorbar=None)
plt.title("Average Miles per Product")
plt.ylabel("Average Miles per Week")
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x='Product', y='Education', data=df, estimator='mean', errorbar=None)
plt.title("Average Education Level per Product")
plt.ylabel("Years of Education")
plt.show()


#To create a stacked bar chart
def plot_stacked_distribution(df, category_col, colors=None):
    # Prepare the data
    pivot = (
        df.groupby(['Product', category_col])
          .size()
          .unstack(fill_value=0)
    )

    # Convert counts to percentages
    pivot_percent = pivot.div(pivot.sum(axis=1), axis=0) * 100

    # Set default colors if none provided
    if colors is None:
        colors = sns.color_palette("pastel", len(pivot_percent.columns))

    # Plot
    pivot_percent.plot(
        kind='bar',
        stacked=True,
        figsize=(8,5),
        color=colors,
        edgecolor='black'
    )

    # Formatting
    plt.title(f"{category_col} Distribution per Product", fontsize=13)
    plt.ylabel("Percentage (%)")
    plt.xlabel("Product")
    plt.legend(title=category_col, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

plot_stacked_distribution(df, 'Gender', colors=['violet', 'blue'])
plot_stacked_distribution(df, "MaritalStatus", colors=['orange', 'brown'])

