import numpy as np
import pandas as pd

#existing_data = pd.DataFrame({
#    'Age': [25, 18, 30, 22, 28, 20, 26, 23],
#    'Height': [180, 165, 175, 172, 185, 160, 178, 170],
#    'Region': ['USA', 'Europe', 'USA', 'Europe', 'USA', 'Asia', 'USA', 'Europe'],
#    'Years_Skateboarding': [5, 2, 10, 3, 8, 4, 6, 3],
#    'Experience': ['Pro', 'Beginner', 'Advanced', 'Pro', 'Advanced', 'Beginner', 'Advanced', 'Pro'],
#    'Brand': ['Brand A', 'Brand B', 'Brand C', 'Brand B', 'Brand A', 'Brand D', 'Brand C', 'Brand B']
#})

existing_data = pd.read_csv('existing_dataset.csv')

num_examples = 1000  # Number of additional examples to generate

new_data = pd.DataFrame({
    'Age': np.random.randint(10, 40, size=num_examples),
    'Height': np.random.randint(150, 200, size=num_examples),
    'Region': np.random.choice(['USA', 'Europe', 'Asia'], size=num_examples),
    'Years_Skateboarding': np.random.randint(1, 15, size=num_examples),
    'Experience': np.random.choice(['Beginner', 'Advanced', 'Pro'], size=num_examples),
    'Brand': np.random.choice(['Brand A', 'Brand B', 'Brand C', 'Brand D'], size=num_examples)
})

# Combine Datasets
expanded_data = pd.concat([existing_data, new_data], ignore_index=True)

expanded_data.to_csv('expanded_dataset.csv', index=False)

