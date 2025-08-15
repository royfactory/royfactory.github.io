---

ShowToc: true
categories: [ai]
date: 2025-08-13
description: Hands-on guide to Supervised Learning with Classification and Regression. Learn key concepts, algorithms, evaluation metrics, and run beginner-friendly examples using scikit-learn.
draft: false
image: /img/supervised-learning-practice.jpg
keywords: supervised learning, classification, regression, machine learning tutorial, sklearn examples, accuracy, rmse, r2 score
tags: [ai, machine-learning, supervised-learning, classification, regression, sklearn, tutorial]
title: 'Supervised Learning Practice: Classification and Regression (Lecture 6)'
slug: supervised-learning-practice
----------------------------------

# Supervised Learning Practice: Classification and Regression (Lecture 6)

In this lecture, we'll explore **Supervised Learning**, understand the difference between **Classification** and **Regression**, review popular algorithms, and implement both tasks using **scikit-learn**.

---

## Table of Contents

{% toc %}

---

## 1) What Is Supervised Learning?

Supervised Learning uses **input data (X)** paired with **labels (y)** to train a model that can predict the correct output for unseen inputs.

---

### 1.1 Classification vs. Regression

| Type           | Description                     | Output Examples        | Use Cases                   |
| -------------- | ------------------------------- | ---------------------- | --------------------------- |
| Classification | Predicts a **category**         | Spam/Not spam, species | Spam detection, diagnosis   |
| Regression     | Predicts a **continuous value** | Price, temperature     | House price, sales forecast |

---

## 2) Classification

### 2.1 Concept

* Assigns each input to one of several **classes**.
* Example: “Is this email spam?”

### 2.2 Common Algorithms

* Logistic Regression
* Decision Tree
* Support Vector Machine (SVM)
* Random Forest

---

## 3) Regression

### 3.1 Concept

* Predicts a **continuous value** based on input features.
* Example: “Predict apartment price given size, location, and year built.”

### 3.2 Common Algorithms

* Linear Regression
* Ridge Regression
* Lasso Regression
* Decision Tree Regression

---

## 4) General Supervised Learning Workflow

1. Prepare data: Separate features (X) and labels (y)
2. Split into training and testing sets
3. Choose a model and train it
4. Predict on test data
5. Evaluate model performance
6. Improve results via hyperparameter tuning

---

## 5) Lab: Classification Example (Iris Species)

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", f"{accuracy_score(y_test, y_pred)*100:.2f}%")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
```

---

## 6) Lab: Regression Example (California Housing Prices)

```python
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Load data
housing = fetch_california_housing()
X, y = housing.data, housing.target

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
reg = LinearRegression()
reg.fit(X_train, y_train)

# Predict
y_pred = reg.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.3f}")
print(f"R² Score: {r2:.3f}")
```

---

## 7) Evaluation Metrics

**Classification**

* Accuracy: % of correct predictions
* Precision, Recall, F1 Score

**Regression**

* MSE / RMSE: Error magnitude
* R² Score: Closer to 1 means better fit

---

## 8) Key Takeaways

* Supervised Learning uses labeled data to make predictions.
* Classification predicts categories, Regression predicts continuous values.
* Evaluation metrics differ by task type.
* We implemented both classification and regression with scikit-learn.

---

## 9) What's Next?

In Lecture 7, we'll cover **Unsupervised Learning Practice**—Clustering and Dimensionality Reduction techniques.

---