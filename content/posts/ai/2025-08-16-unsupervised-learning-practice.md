---
ShowToc: true
categories: [ai]
date: 2025-08-13
description: Hands-on guide to Unsupervised Learning with K-Means clustering and PCA dimensionality reduction. Learn concepts, applications, and run beginner-friendly examples using scikit-learn.
draft: false
image: /img/unsupervised-learning-practice.jpg
keywords: unsupervised learning, clustering, dimensionality reduction, k-means, pca, sklearn examples, machine learning tutorial
tags: [ai, machine-learning, unsupervised-learning, clustering, kmeans, pca, sklearn, tutorial]
title: 'Unsupervised Learning Practice: Clustering and Dimensionality Reduction (Lecture 7)'
slug: unsupervised-learning-practice
------------------------------------

# Unsupervised Learning Practice: Clustering and Dimensionality Reduction (Lecture 7)

In this lecture, we'll explore **Unsupervised Learning**, understand the concepts of **Clustering** and **Dimensionality Reduction**, and implement both techniques using **scikit-learn**.

---

## Table of Contents

{% toc %}

---

## 1) What Is Unsupervised Learning?

Unsupervised Learning finds **patterns, structures, or relationships** in data **without labels**.
Unlike supervised learning, there is no "answer key"—the model discovers hidden rules on its own.

---

### 1.1 Common Applications

* **Customer Segmentation**: Grouping customers based on purchase history
* **Anomaly Detection**: Fraud detection, early fault detection in systems
* **Data Visualization**: Reducing high-dimensional data to 2D/3D for interpretation

---

## 2) Clustering

Clustering groups **similar data points** together.
Popular algorithms include:

| Algorithm        | Characteristics                                              |
| ---------------- | ------------------------------------------------------------ |
| **K-Means**      | Simple and fast, requires predefining number of clusters     |
| **Hierarchical** | Builds a tree of clusters, useful for visualization          |
| **DBSCAN**       | No need to specify number of clusters, handles outliers well |

---

### 2.1 K-Means Concept

* Splits data into **K clusters**.
* Iteratively updates cluster centers (centroids) to group similar points.

---

## 3) Dimensionality Reduction

Dimensionality reduction decreases the number of **features** while retaining essential information.
Useful for visualization and improving learning efficiency.

---

### 3.1 PCA (Principal Component Analysis)

* Finds new axes (principal components) that explain the most variance in data.
* Minimizes information loss while reducing dimensions.

---

## 4) Lab: K-Means Clustering on the Iris Dataset

```python
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

# Load data
iris = load_iris()
X = iris.data

# Train K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X)

# Create DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)
df['cluster'] = clusters

# Visualization
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=df['cluster'], cmap='viridis')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('K-Means Clustering of Iris')
plt.show()
```

---

## 5) Lab: PCA Dimensionality Reduction

```python
from sklearn.decomposition import PCA

# Reduce to 2 dimensions
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Visualization
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Dimensionality Reduction')
plt.show()
```

---

## 6) Key Takeaways

* Unsupervised Learning uncovers patterns without labeled data.
* **Clustering** groups similar data points; **K-Means** is widely used for its simplicity.
* **Dimensionality Reduction** (e.g., PCA) helps visualize and simplify datasets.
* Combining K-Means and PCA provides both grouping and visual insight.

---

## 7) What's Next?

In Lecture 8, we'll move into **Basic Neural Network Practice**—building a simple image classification model.

---