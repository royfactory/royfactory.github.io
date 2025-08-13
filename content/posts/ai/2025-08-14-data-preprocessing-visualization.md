---
ShowToc: true
categories: [ai]
date: 2025-08-14
description: Learn how to preprocess and visualize data for AI projects, including handling missing values, detecting outliers, scaling features, encoding categorical variables, and creating visualizations. Includes a beginner-friendly Iris dataset example.
draft: false
image: /img/data-preprocessing-visualization.jpg
keywords: data preprocessing, ai data cleaning, missing values, outliers, feature scaling, encoding, data visualization, iris dataset example
tags: [ai, data-preprocessing, visualization, cleaning, missing-values, outliers, scaling, encoding, tutorial]
title: 'Data Preprocessing and Visualization for AI: A Complete Guide (Lecture 5)'
slug: data-preprocessing-visualization
--------------------------------------

# Data Preprocessing and Visualization for AI: A Complete Guide (Lecture 5)

In this lecture, we'll cover **data preprocessing**—the crucial step to ensure your AI models work with clean, structured, and meaningful data. We'll also explore **data visualization** techniques to better understand your dataset.

---

## Table of Contents

{% toc %}

---

## 1) Why Data Preprocessing Matters

Model performance depends heavily on data quality.
Even the most advanced algorithms can fail if the input data is noisy or inconsistent.

**Preprocessing Goals:**

1. Handle **missing values**
2. Detect and manage **outliers**
3. **Scale features** for model compatibility
4. **Encode categorical variables**
5. Use **visualization** for deeper insight

---

## 2) Handling Missing Values

### 2.1 Checking for Missing Data

```python
import pandas as pd

df = pd.read_csv("data.csv")
print(df.isnull().sum())
```

### 2.2 Filling or Removing Missing Values

* **Drop missing rows/columns**:

```python
df = df.dropna()
```

* **Fill with mean/median/mode**:

```python
df['age'] = df['age'].fillna(df['age'].mean())
```

---

## 3) Detecting and Handling Outliers

* **Outlier**: Data points far from the normal distribution.
* **Detection Methods**:

  * Statistical: IQR (Interquartile Range)
  * Visualization: Boxplots

```python
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['value'] < Q1 - 1.5*IQR) | (df['value'] > Q3 + 1.5*IQR)]
```

---

## 4) Feature Scaling

Scaling ensures features contribute equally to the model.

* **Standardization**: Mean = 0, Std = 1
* **Normalization**: Range = 0–1

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[['feature1', 'feature2']])
```

---

## 5) Encoding Categorical Variables

Models can't handle raw text categories—convert them to numeric form.

**One-Hot Encoding**:

```python
df_encoded = pd.get_dummies(df, columns=['category'])
```

---

## 6) Data Visualization

### 6.1 Histogram

```python
import matplotlib.pyplot as plt

df['age'].hist(bins=20)
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()
```

### 6.2 Boxplot

```python
df.boxplot(column='value', by='category')
plt.show()
```

### 6.3 Scatter Plot

```python
plt.scatter(df['feature1'], df['feature2'])
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
```

---

## 7) Lab: Preprocessing and Visualizing the Iris Dataset

```python
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Check missing values
print(df.isnull().sum())

# Standardize features
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df.iloc[:, :-1])

# Visualization
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=df['target'])
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()
```

---

## 8) Key Takeaways

* Preprocessing improves data quality and model accuracy.
* Handle missing values before training.
* Detect and mitigate outliers to avoid skewed results.
* Scale features for fair model contribution.
* Visualize data to identify trends and patterns.

---

## 9) What's Next?

In Lecture 6, we'll move into **Supervised Learning Practice**—building classification and regression models from scratch.

---
