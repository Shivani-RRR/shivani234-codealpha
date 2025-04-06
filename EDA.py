import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
df = pd.read_csv('D:\python\content.csv')
print(df.shape)  # Number of rows and columns
print(df.dtypes)  # Data types of columns
# Summary statistics for numeric columns
print(df.describe())

# Summary for categorical columns
#print(df['column_name'].value_counts())

# Histogram
df['age'].hist()
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Boxplot
sns.boxplot(x='gender', y='income', data=df)
plt.title('Income Distribution by Gender')
plt.show()

# Correlation heatmap
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()
# Check for missing values
print(df.isnull().sum())

# Visualize missing data with a heatmap
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.show()

# Using a boxplot to detect outliers
sns.boxplot(x=df['age'])
plt.show()

# Remove NaN values
df_cleaned = df['age'].dropna()

# Alternatively, replace NaN with the mean (imputation)
df['age'] = df['age'].fillna(df['age'].mean())


# Scatter plot to explore relationships between two numerical variables
plt.scatter(df['age'], df['income'])
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Age vs. Income')
plt.show()

# Sample DataFrame with a numeric column
data = {
    'age': [25, 30, 35, 40, 50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)

# Check for NaN values and handle if necessary
if df['age'].isnull().any():
    df['age'] = df['age'].fillna(df['age'].mean())

# Calculate Z-scores for the 'age' column
z_scores = stats.zscore(df['age'])

# Print the z-scores
print("Z-scores for the 'age' column:")
print(z_scores)