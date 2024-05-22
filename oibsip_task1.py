# -*- coding: utf-8 -*-
"""OIBSIP_Task1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lTZWHQp7xk-53RSXKKfGbHzeOqdE55IG
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd

# Load the DataFrame
df = pd.read_csv('Iris.csv')
df

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Convert to DataFrame for easier manipulation
df = pd.DataFrame(data=X, columns=iris.feature_names)
df['species'] = y

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Classification report
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

# Add predictions to the DataFrame
df_test = pd.DataFrame(X_test, columns=iris.feature_names)
df_test['true_species'] = y_test
df_test['predicted_species'] = y_pred

# Plot the true species
plt.figure(figsize=(14, 6))

# Plot 1: True labels
plt.subplot(1, 2, 1)
sns.scatterplot(data=df_test, x='sepal length (cm)', y='sepal width (cm)', hue='true_species', palette='viridis', legend='full')
plt.title('True Species')
plt.legend(title='Species', labels=iris.target_names)

# Plot 2: Predicted labels
plt.subplot(1, 2, 2)
sns.scatterplot(data=df_test, x='sepal length (cm)', y='sepal width (cm)', hue='predicted_species', palette='viridis', legend='full')
plt.title('Predicted Species')
plt.legend(title='Species', labels=iris.target_names)

plt.show()