---
ShowToc: true
categories: [ai]
date: 2025-08-21
description: Learn the fundamentals of GRU (Gated Recurrent Unit) networks in deep learning. Covers theory, equations, and a hands-on IMDB sentiment analysis example using TensorFlow and Keras.
draft: false
image: /img/gru-basics.jpg
keywords: gru basics, recurrent neural network, rnn vs lstm vs gru, tensorflow gru, keras gru, sentiment analysis, imdb dataset, nlp deep learning
tags: [ai, deep learning, gru, rnn, keras, tensorflow, sentiment-analysis]
title: 'GRU Basics: Simplifying Recurrent Neural Networks (Lecture 13)'
slug: ai-gru-basics
---

# GRU Basics: Simplifying Recurrent Neural Networks (Lecture 13)

In this lecture, we introduce **GRU (Gated Recurrent Unit) networks**, a simpler and faster variant of LSTM. You will learn the **theory behind GRU gates**, compare it with RNN and LSTM, and implement a **sentiment analysis model on the IMDB dataset** using TensorFlow/Keras.

---

## Table of Contents

{% toc %}

---

## 1) Why GRU?

Traditional RNNs suffer from the **vanishing gradient problem**, making it difficult to learn long-term dependencies.  
LSTMs solve this with a more complex structure but at the cost of **slower training**.  

**GRU Advantages:**
- Fewer gates (2 instead of 3 in LSTM)  
- Faster training  
- Comparable accuracy in many tasks  

---

## 2) GRU Architecture

GRUs rely on **two gates**:

1. **Reset Gate (r_t)** – decides how much past information to forget  
2. **Update Gate (z_t)** – decides how much new information to add  

### Key Equations

- Update gate:  
```

z\_t = σ(W\_z · \[h\_{t-1}, x\_t])

```
- Reset gate:  
```

r\_t = σ(W\_r · \[h\_{t-1}, x\_t])

```
- Candidate hidden state:  
```

h̃\_t = tanh(W · \[r\_t \* h\_{t-1}, x\_t])

```
- Final hidden state:  
```

h\_t = (1 - z\_t) \* h\_{t-1} + z\_t \* h̃\_t

````

---

## 3) Example: IMDB Sentiment Analysis with GRU

Let’s implement a GRU model to classify movie reviews as **positive** or **negative**.

```python
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GRU, Dense

# 1. Load dataset
max_features = 10000
maxlen = 200
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

# 2. Pad sequences
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

# 3. Build GRU model
model = Sequential()
model.add(Embedding(max_features, 128))
model.add(GRU(128))
model.add(Dense(1, activation='sigmoid'))

# 4. Compile and train
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(x_train, y_train, epochs=3, batch_size=64, validation_split=0.2)

# 5. Evaluate
loss, acc = model.evaluate(x_test, y_test)
print("Test Accuracy:", acc)
````

**Expected Output:**

```
Epoch 1/3 - val_acc: ~0.83
Epoch 2/3 - val_acc: ~0.86
Epoch 3/3 - val_acc: ~0.87
Test Accuracy: ~0.87
```

---

## 4) GRU vs LSTM

| Feature      | LSTM                      | GRU               |
| ------------ | ------------------------- | ----------------- |
| Gates        | 3 (Forget, Input, Output) | 2 (Reset, Update) |
| Memory Units | Cell state + Hidden state | Hidden state only |
| Speed        | Slower                    | Faster            |
| Accuracy     | Often higher              | Comparable        |

---

## 5) Key Takeaways

* GRU is a **simpler alternative to LSTM**.
* Uses **reset** and **update** gates to balance past and new information.
* Achieves **\~87% accuracy** on IMDB sentiment classification.

---

## Recommended Reading

* [TensorFlow GRU Layer Docs](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GRU)
* [Understanding GRUs - Towards Data Science](https://towardsdatascience.com/understanding-gru-networks-2ef37df6c9be)
* [DeepLearning.AI Sequence Models](https://www.deeplearning.ai/)

---