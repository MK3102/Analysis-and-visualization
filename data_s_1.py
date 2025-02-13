import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\MK\Desktop\Python\Python\sales_data.csv"

data = pd.read_csv(file_path)
data['Date'] = pd.to_datetime(data['Date'])
data.dropna(inplace=True)
data['Sales_per_Unit'] = data['Sales'] / data['Quantity']
sales_trend = data.groupby(data['Date'].dt.to_period('M'))['Sales'].sum()
sales_trend.plot(kind='line', figsize=(10, 6), title='Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()
top_regions = data.groupby('Region')['Sales'].sum().sort_values(ascending=False)
sns.barplot(x=top_regions.values, y=top_regions.index, palette='viridis')
plt.title('Top Performing Regions by Sales')
plt.xlabel('Total Sales')
plt.ylabel('Region')
plt.show()
top_products = data.groupby('Product')['Sales'].sum().nlargest(10)
sns.barplot(x=top_products.values, y=top_products.index, palette='coolwarm')
plt.title('Top 10 Products by Sales')
plt.xlabel('Total Sales')
plt.ylabel('Product')
plt.show()
corr = data[['Sales', 'Quantity', 'Sales_per_Unit']].corr()
sns.heatmap(corr, annot=True, cmap='Blues', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()
sns.histplot(data['Sales'], kde=True, bins=20, color='blue')
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()
