import matplotlib.pyplot as plt
import seaborn as sns

# Example Data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [23, 45, 56, 78]

# Create bar chart
plt.bar(categories, values)
plt.title('Category Comparison')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Example Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [200, 250, 300, 350, 400]

# Create line chart
plt.plot(months, sales)
plt.title('Sales Trend')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()

# Example Data
labels = ['Company A', 'Company B', 'Company C', 'Company D']
market_share = [40, 20, 30, 10]

# Create pie chart
plt.pie(market_share, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Market Share Distribution')
plt.show()

# Example Data
ad_spend = [100, 200, 300, 400, 500]
sales = [20, 40, 60, 80, 100]

# Create scatter plot
plt.scatter(ad_spend, sales)
plt.title('Advertising Spend vs Sales')
plt.xlabel('Advertising Spend')
plt.ylabel('Sales')
plt.show()

import seaborn as sns
import numpy as np

# Example Data (correlation matrix)
data = np.random.rand(10, 12)

# Create heatmap
sns.heatmap(data, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Example Data
ages = [23, 25, 27, 28, 29, 35, 40, 41, 50, 55, 60, 65, 70]

# Create histogram
plt.hist(ages, bins=5, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Example Data
income = [2000, 2500, 3000, 4000, 5000, 10000, 12000, 15000]

# Create box plot
sns.boxplot(income)
plt.title('Income Distribution')
plt.show()

# Example Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [100, 200, 300, 400, 500]

# Create area chart
plt.fill_between(months, sales, color='skyblue', alpha=0.5)
plt.plot(months, sales, color='Slateblue', alpha=0.6)
plt.title('Sales Over Time')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()
