# import pandas as pd
# import numpy as np

# existing_data = pd.read_csv('existing_dataset.csv')

# num_new_examples = 1000

# new_age = np.random.randint(18, 40, size=num_new_examples)
# new_height = np.random.normal(170, 10, size=num_new_examples)
# new_region = np.random.choice(['North', 'South', 'East', 'West'], size=num_new_examples)
# new_years_skateboarding = np.random.randint(1, 10, size=num_new_examples)
# new_experience = np.random.choice(['Beginner', 'Intermediate', 'Advanced'], size=num_new_examples)


# expanded_data = pd.DataFrame({
#     'Age': np.concatenate([existing_data['Age'].values, new_age]),
#     'Height': np.concatenate([existing_data['Height'].values, new_height]),
#     'Region': np.concatenate([existing_data['Region'].values, new_region]),
#     'Years_Skateboarding': np.concatenate([existing_data['Years_Skateboarding'].values, new_years_skateboarding]),
#     'Experience': np.concatenate([existing_data['Experience'].values, new_experience]),
#     'Brand': np.concatenate([existing_data['Brand'].values, np.repeat('', num_new_examples)])  # Fill new examples with empty values
# })


# expanded_data.to_csv('expanded_dataset.csv', index=False)

