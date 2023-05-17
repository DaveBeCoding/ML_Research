import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.neural_network import MLPClassifier
from sklearn.impute import SimpleImputer

# Load the dataset
data = pd.read_csv('expanded_dataset.csv')

# Separate features and target variable
X = data.drop('Brand', axis=1).values
y = data['Brand'].values

# Define column transformer for feature preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), [0, 1, 3]),
        ('cat', OneHotEncoder(), [2, 4])
    ])

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocess the features
X_train_scaled = preprocessor.fit_transform(X_train)
X_test_scaled = preprocessor.transform(X_test)

# Impute missing values
imputer = SimpleImputer(strategy='mean')
X_train_scaled = imputer.fit_transform(X_train_scaled)
X_test_scaled = imputer.transform(X_test_scaled)

# Create and train the neural network model
model = MLPClassifier(hidden_layer_sizes=(64, 32), activation='relu', random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate the model
accuracy = model.score(X_test_scaled, y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")

