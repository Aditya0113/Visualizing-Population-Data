import pandas as pd
import matplotlib.pyplot as plt

df_api = pd.read_csv('API.csv', skiprows=4)

df_api = df_api.drop('Unnamed: 69', axis=1)

df_2024 = df_api.dropna(subset=['2024']).copy()

df_2024['2024'] = pd.to_numeric(df_2024['2024'])

top_10_countries = df_2024.sort_values(by='2024', ascending=False).head(10)

# Create a bar chart for the top 10 most populated countries in 2024
plt.figure(figsize=(12, 8))
plt.bar(top_10_countries['Country Name'], top_10_countries['2024'], color='skyblue')
plt.title('Top 10 Most Populated Countries in 2024', fontsize=16)
plt.xlabel('Country Name', fontsize=12)
plt.ylabel('Population', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_10_countries_population_bar_chart.png')
plt.show()
print("Bar chart saved as 'top_10_countries_population_bar_chart.png'")

# Create a histogram for the population distribution in 2024
plt.figure(figsize=(12, 8))
plt.hist(df_2024['2024'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Population Distribution Across Countries in 2024', fontsize=16)
plt.xlabel('Population', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.savefig('population_distribution_histogram.png')
plt.show()
print("Histogram saved as 'population_distribution_histogram.png'")