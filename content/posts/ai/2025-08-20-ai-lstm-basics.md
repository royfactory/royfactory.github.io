---
ShowToc: true
categories: [ai]
date: 2025-08-20
description: Introduction to LSTM (Long Short-Term Memory) networks with clear explanations and a hands-on TensorFlow/Keras example for sentiment classification using IMDB dataset.
draft: false
image: /img/ai-lstm-basics.jpg
keywords: ai basics, deep learning, lstm, rnn, sequence modeling, nlp, tensorflow keras, sentiment analysis
tags: [ai, deep-learning, lstm, rnn, sequence, nlp, tensorflow, keras, sentiment-analysis]
title: 'LSTM Basics: Understanding Long Short-Term Memory Networks (Lecture 12)'
slug: ai-lstm-basics
---

# LSTM Basics: Understanding Long Short-Term Memory Networks (Lecture 12)

In this lecture, we will explore **LSTM (Long Short-Term Memory)** networks. Unlike simple RNNs that struggle with long-term dependencies, LSTMs use special **gates** to remember or forget information, making them powerful for **NLP, speech recognition, and time-series prediction**.

---

## Table of Contents

{% toc %}

---

## 1) Why Do We Need LSTM?

Traditional **RNNs** suffer from the **vanishing gradient problem**, making it difficult to capture long-term context.  
For example:

> In the sentence, *“Today the weather is sunny and I feel happy because I went to the park with my friend …”*  
> A basic RNN may forget the earlier word “weather” by the time it processes the later words.  

**LSTMs solve this by introducing gates** that regulate the flow of information.

---

## 2) LSTM Architecture Overview

LSTMs consist of three main gates:

- **Forget Gate** → decides what past information to discard.  
- **Input Gate** → decides what new information to store.  
- **Output Gate** → decides what information to pass on.  

Together, they maintain a **cell state (long-term memory)** and a **hidden state (short-term memory)**.

---

## 3) Mathematical Formulation (Simplified)

- Forget gate:  
```

f\_t = σ(W\_f · \[h\_{t-1}, x\_t] + b\_f)

```
- Input gate:  
```

i\_t = σ(W\_i · \[h\_{t-1}, x\_t] + b\_i)
C̃\_t = tanh(W\_c · \[h\_{t-1}, x\_t] + b\_c)
C\_t = f\_t \* C\_{t-1} + i\_t \* C̃\_t

```
- Output gate:  
```

o\_t = σ(W\_o · \[h\_{t-1}, x\_t] + b\_o)
h\_t = o\_t \* tanh(C\_t)

````

Where:  
- `σ` is the sigmoid function  
- `tanh` is hyperbolic tangent  
- `C_t` is the cell state  
- `h_t` is the hidden state  

---

## 4) Hands-on Example: Sentiment Classification with LSTM

We’ll use the **IMDB movie reviews dataset** to classify reviews as **positive** or **negative**.

```python
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# 1. Load data
max_features = 10000  # top 10,000 words
maxlen = 200          # cut reviews to 200 words
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

# 2. Pad sequences
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

# 3. Build model
model = Sequential()
model.add(Embedding(max_features, 128))
model.add(LSTM(128))
model.add(Dense(1, activation='sigmoid'))

# 4. Compile and train
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(x_train, y_train, epochs=3, batch_size=64, validation_split=0.2)

# 5. Evaluate
loss, acc = model.evaluate(x_test, y_test)
print("Test Accuracy:", acc)
````

### Example Output

```
Epoch 1/3
313/313 [==============================] - 50s - loss: 0.45 - acc: 0.78 - val_acc: 0.84
Epoch 2/3
313/313 [==============================] - 45s - loss: 0.30 - acc: 0.87 - val_acc: 0.86
Epoch 3/3
313/313 [==============================] - 46s - loss: 0.22 - acc: 0.91 - val_acc: 0.87

Test Accuracy: 0.87
```

---

## 5) Key Takeaways

* LSTM solves the **long-term dependency problem** of RNNs.
* The gate mechanism allows **selective memory and forgetting**.
* In practice, LSTMs perform well on **text, speech, and time-series data**.
* Our IMDB example achieved \~**87% accuracy**.

---

## 🔗 Recommended Learning Resources

* [TensorFlow Keras LSTM Documentation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM)
* [Understanding LSTMs by Colah](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* [Hugging Face Tutorials](https://huggingface.co/transformers/)

---