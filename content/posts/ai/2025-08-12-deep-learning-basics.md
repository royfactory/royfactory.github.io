---
ShowToc: true
categories: [ai]
date: 2025-08-12
description: Learn the basics of Deep Learning, including how CNNs and RNNs work, when to use each, and build a simple CNN to classify MNIST handwritten digits with TensorFlow/Keras.
draft: false
image: /img/deep-learning-basics.jpg
keywords: deep learning basics, cnn vs rnn, convolutional neural network, recurrent neural network, mnist cnn example, tensorflow keras tutorial
tags: [ai, deep-learning, cnn, rnn, tensorflow, keras, tutorial, beginners]
title: 'Deep Learning Basics: CNN vs. RNN and a Hands-On MNIST Example (Lecture 3)'
slug: deep-learning-basics
--------------------------

# Deep Learning Basics: CNN vs. RNN and a Hands-On MNIST Example (Lecture 3)

This is Lecture 3 of our AI 101 series. We'll explain **what Deep Learning is**, compare **CNNs and RNNs**, and finish with a **verified TensorFlow/Keras lab** where you build a CNN to classify MNIST handwritten digits.

---

## Table of Contents

{% toc %}

---

## 1) What Is Deep Learning?

**Deep Learning** is a subset of Machine Learning that uses **multi-layer artificial neural networks** to model complex patterns in data—especially effective for **images, audio, and text**.

---

### 1.1 Neural Network Basics

A neural network consists of:

* **Input Layer**: Where data enters the model.
* **Hidden Layers**: Layers of neurons that transform the data.
* **Output Layer**: Produces the final prediction.

Example: An image → processed through multiple layers → classified as “cat” in the output.

---

## 2) Deep Learning vs. Machine Learning

| Feature            | Machine Learning              | Deep Learning                |
| ------------------ | ----------------------------- | ---------------------------- |
| Feature Extraction | Manual (engineered by humans) | Automatic (learned by model) |
| Data Needs         | Works with smaller datasets   | Requires large datasets      |
| Compute            | CPU-friendly                  | Typically needs GPUs         |
| Examples           | Decision Trees, SVM           | CNN, RNN, Transformers       |

---

## 3) CNN vs. RNN

---

### 3.1 CNN (Convolutional Neural Network)

* Designed for **image processing**.
* Uses **convolutions** to automatically extract visual features like edges, colors, and textures.
* Typical structure: **Convolution Layer → Pooling Layer → Fully Connected Layer**.

**Applications**:

* Image classification
* Facial recognition
* Road scene understanding in autonomous driving

---

### 3.2 RNN (Recurrent Neural Network)

* Designed for **sequential data** (time series, language).
* Passes the output from one step as input to the next—adding a **memory** component.
* Variants: LSTM, GRU (handle long-term dependencies).

**Applications**:

* Natural Language Processing (translation, chatbots)
* Stock price prediction
* Speech recognition

---

## 4) Typical Deep Learning Workflow

1. **Data Preparation**: Gather and format images, text, or audio.
2. **Preprocessing**: Normalize values, tokenize text, etc.
3. **Model Design**: Choose CNN, RNN, or other architectures.
4. **Training**: Use GPU if available for faster convergence.
5. **Evaluation**: Measure accuracy, loss, and other metrics.
6. **Deployment**: Integrate into production systems.

---

## 5) Hands-On Lab: CNN for MNIST Digit Classification

We'll use **TensorFlow/Keras** to build a small CNN that classifies MNIST handwritten digits (0–9).

> **Setup**
>
> ```bash
> pip install tensorflow
> ```

```python
import tensorflow as tf
from tensorflow.keras import layers, models

# 1. Load data
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 2. Preprocess data
X_train = X_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0
X_test = X_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0

# 3. Build model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation="relu"),
    layers.Dense(10, activation="softmax")
])

# 4. Compile
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

# 5. Train
model.fit(X_train, y_train, epochs=3, validation_data=(X_test, y_test))

# 6. Evaluate
test_loss, test_acc = model.evaluate(X_test, y_test)
print("Test accuracy:", f"{test_acc*100:.2f}%")
```

**Expected Output**

```
Epoch 1/3
1875/1875 [==============================] - 12s 6ms/step - loss: 0.1389 - accuracy: 0.9587 - val_loss: 0.0464 - val_accuracy: 0.9858
...
Test accuracy: 98.60%
```

---

## 6) Key Takeaways

* **Deep Learning** uses multi-layer neural networks to handle complex data.
* **CNN**: Best for spatial data like images.
* **RNN**: Best for sequential data like text or time series.
* The MNIST CNN example shows how simple architectures can achieve high accuracy quickly.

---

## 7) FAQ (Answer Engine Optimization)

**Q1. Do I always need a GPU for Deep Learning?**
A. Not for small datasets/models, but GPUs speed up training dramatically.

**Q2. Can CNNs handle text data?**
A. Yes, with some preprocessing—but RNNs or Transformers are usually better for text.

**Q3. Why normalize image data to 0–1?**
A. It helps the optimizer converge faster and more reliably.

**Q4. Can I combine CNN and RNN?**
A. Yes, hybrid architectures are common (e.g., video classification).

---

## 8) Summary Table

| Model Type | Best For        | Key Feature               | Example Application  |
| ---------- | --------------- | ------------------------- | -------------------- |
| CNN        | Spatial data    | Convolutions for features | Image classification |
| RNN        | Sequential data | Memory via recurrence     | Language translation |

---
