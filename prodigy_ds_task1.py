# -*- coding: utf-8 -*-
"""prodigy-DS-task1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x6ns2dEAh8ZC3okr0NBLvehbCbY224pA
"""

import pandas as pd
import matplotlib.pyplot as plt

from google.colab import files
files.upload()

df = pd.read_csv("world_population.csv")
df

df.head()

df.tail()

df.info()

countries = df['Continent']
population = df['2022 Population']

# Create the bar chart
plt.figure(figsize=(12, 6))
plt.bar(countries, population)
plt.xlabel('Countries')
plt.ylabel('2022 Population')
plt.xticks(rotation=45, ha='right')
plt.title('Distribution of Total Population (2022)')
plt.tight_layout()
plt.show()