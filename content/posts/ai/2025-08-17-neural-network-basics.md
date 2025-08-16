---
ShowToc: true
categories: [ai]
date: 2025-08-17
description: Beginner-friendly hands-on guide to building your first neural network for image classification. Learn the basics of neural networks, how they work, and train a simple MNIST model using TensorFlow/Keras.
draft: false
image: /img/neural-network-basics.jpg
keywords: neural network basics, image classification, mnist example, keras tutorial, tensorflow beginner, deep learning introduction
tags: [ai, deep-learning, neural-network, image-classification, tensorflow, keras, mnist, tutorial]
title: 'Neural Network Basics: Build a Simple Image Classification Model (Lecture 8)'
slug: neural-network-basics
---------------------------

# Neural Network Basics: Build a Simple Image Classification Model (Lecture 8)

In this lecture, we'll introduce **Neural Networks**, explain their core components, and build a simple **image classification model** using the MNIST handwritten digits dataset with **TensorFlow/Keras**.

---

## Table of Contents

{% toc %}

---

## 1) What Is a Neural Network?

A **Neural Network** is made up of interconnected units called **neurons**, organized in layers.
Data flows through **Input → Hidden Layers → Output**, with weights and activations applied at each step.

---

### 1.1 Key Components

* **Weights**: Adjust how important each input is.
* **Activation Function**: Decides whether a neuron "fires" (e.g., ReLU, Sigmoid).
* **Loss Function**: Measures error between prediction and true label.
* **Optimizer**: Updates weights to minimize loss (e.g., SGD, Adam).

---

## 2) Why Use Neural Networks?

Unlike traditional ML methods where humans manually define features, neural networks can **automatically learn features** from raw data.

**Example**:

* Traditional ML: Engineer rules like “cat ears are pointy” or “whisker length matters.”
* Neural Networks: Learn these patterns automatically from thousands of cat images.

---

## 3) What Is Image Classification?

Image classification assigns an input image to one of several categories.
Example: The **MNIST dataset** contains 28x28 grayscale images of handwritten digits (0–9).
Our goal: Build a neural network to classify them.

---

## 4) Deep Learning Workflow

1. Prepare data: Train/test split
2. Design model: Stack layers
3. Train: Optimize weights with data
4. Evaluate: Measure accuracy and loss
5. Predict: Apply the model to new inputs

---

## 5) Lab: MNIST Handwritten Digit Classification (TensorFlow/Keras)

> **Setup**
>
> ```bash
> pip install tensorflow
> ```

```python
import tensorflow as tf
from tensorflow.keras import layers, models

# 1. Load dataset
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# 2. Preprocess
X_train = X_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0
X_test = X_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0

# 3. Build model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28, 1)),   # Flatten image to vector
    layers.Dense(128, activation="relu"),      # Hidden layer
    layers.Dense(10, activation="softmax")     # Output layer (10 digits)
])

# 4. Compile
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

# 5. Train
model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))

# 6. Evaluate
test_loss, test_acc = model.evaluate(X_test, y_test)
print("Test Accuracy:", f"{test_acc*100:.2f}%")
```

---

## 6) Example Output

```
Epoch 1/5
1875/1875 [==============================] - 5s 2ms/step - loss: 0.3000 - accuracy: 0.9130 - val_loss: 0.1430 - val_accuracy: 0.9580
...
Test Accuracy: 97.8%
```

---

## 7) Key Takeaways

* Neural Networks are structured with **layers, weights, and activations**.
* They automatically learn features from raw data.
* Image classification is a core deep learning task.
* Using TensorFlow/Keras, even a simple model can achieve **97%+ accuracy** on MNIST.

---

## 8) What's Next?

In Lecture 9, we'll move to **Natural Language Processing (NLP) Basics**—covering text preprocessing and a simple sentiment analysis example.

---