import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix

# Load the Olivetti Faces dataset
faces_data = fetch_olivetti_faces()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(faces_data.data, faces_data.target, test_size=0.2, random_state=42)

# Train a Multi-layer Perceptron (MLP) classifier
mlp_classifier = MLPClassifier(hidden_layer_sizes=(100,), max_iter=1000, random_state=42)
mlp_classifier.fit(X_train, y_train)

# Evaluate the model on the testing data
predictions = mlp_classifier.predict(X_test)

# Display ten entries from the testing data along with their true labels and predictions
plt.figure(figsize=(10, 10))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_test[i].reshape(64, 64), cmap='gray')
    plt.title(f'True: {y_test[i]}\nPredicted: {predictions[i]}')
    plt.axis('off')
plt.tight_layout()
plt.show()

# Display the confusion matrix for the testing data
conf_matrix = confusion_matrix(y_test, predictions)
plt.figure(figsize=(8, 6))
plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.colorbar()
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.xticks(np.arange(len(np.unique(y_test))), np.unique(y_test), rotation=45)
plt.yticks(np.arange(len(np.unique(y_test))), np.unique(y_test))
plt.tight_layout()
plt.show()
