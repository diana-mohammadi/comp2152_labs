# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

# Load the IRIS dataset
iris = load_iris()

# Extract features, labels, and their names
X = iris.data
y = iris.target
feature_names = iris.feature_names
label_names = iris.target_names

# Explore the dataset shape
print(f"Feature dataset shape: {X.shape}")
print(f"Label dataset shape: {y.shape}")

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Instantiate Decision Tree Classifier
model = DecisionTreeClassifier()

# Train the model
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Print actual labels vs predicted labels
print(f"Actual labels: {y_test}")
print(f"Predicted labels: {y_pred}")

# Calculate and print accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of the model: {accuracy:.2f}")

# Plot the decision tree
plt.figure(figsize=(15, 10))
plot_tree(model, feature_names=feature_names, class_names=label_names, filled=True)
plt.show()
