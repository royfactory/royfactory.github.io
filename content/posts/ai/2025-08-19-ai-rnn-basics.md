---
ShowToc: true
categories: [ai]
date: 2025-08-16
description: Introduction to Recurrent Neural Networks (RNN) with theory and PyTorch implementation. Learn how RNNs process sequential data, their limitations, and practical coding examples for text and time-series prediction.
draft: false
image: /img/rnn-basics.jpg
keywords: recurrent neural network, rnn basics, pytorch rnn, sequential data, nlp, time series prediction, ai fundamentals
tags: [ai, rnn, pytorch, nlp, sequential, time-series, deep-learning, basics]
title: 'Recurrent Neural Network (RNN) Basics: Theory and PyTorch Implementation (Lecture 11)'
slug: ai-rnn-basics
---

# Recurrent Neural Network (RNN) Basics: Theory and PyTorch Implementation (Lecture 11)

In this lecture, we'll explore **Recurrent Neural Networks (RNNs)**, one of the fundamental architectures for handling **sequential data**.  
We'll cover the theory behind RNNs, their mathematical formulation, limitations, and implement simple RNNs in **PyTorch** for both **text** and **time-series prediction**.

---

## Table of Contents
{% toc %}

---

## 1) What is an RNN?

Unlike feedforward networks that treat each input independently, RNNs are designed to **remember previous states** and use them in predicting future outputs.  
This makes RNNs highly effective for tasks where **context and sequence order** matter, such as:

* Natural Language Processing (NLP)
* Speech recognition
* Time-series forecasting

---

## 2) RNN Core Structure

The key idea:  
At each time step **t**, the network combines the **current input (x_t)** with the **previous hidden state (h_(t-1))** to produce a new hidden state **h_t** and output **y_t**.

- **Hidden state update:**
```

h\_t = tanh(W\_hh \* h\_(t-1) + W\_xh \* x\_t + b\_h)

```
- **Output:**
```

y\_t = W\_hy \* h\_t + b\_y

````

Here:
* `x_t`: Input at time t  
* `h_t`: Hidden state at time t  
* `y_t`: Output at time t  

---

## 3) Intuitive Example

Imagine someone says: **"Today the weather is..."**  
Your brain doesn't interpret the last word in isolation.  
It recalls the context (**“Today” + “weather”**) to expect a word like **“sunny”**.  

This contextual awareness is what makes RNNs powerful.

---

## 4) PyTorch Implementation: Simple RNN

```python
import torch
import torch.nn as nn

# Sample input (batch=1, sequence=3, feature=5)
x = torch.randn(1, 3, 5)

# Define RNN layer (input_size=5, hidden_size=4, num_layers=1)
rnn = nn.RNN(input_size=5, hidden_size=4, num_layers=1, batch_first=True)

# Initial hidden state
h0 = torch.zeros(1, 1, 4)

# Forward pass
output, hn = rnn(x, h0)

print("Input shape:", x.shape)
print("Output shape:", output.shape)
print("Final hidden state:", hn.shape)
````

**Expected Output:**

```
Input shape: torch.Size([1, 3, 5])
Output shape: torch.Size([1, 3, 4])
Final hidden state: torch.Size([1, 1, 4])
```

The RNN processes the sequence step by step while passing hidden states forward.

---

## 5) Limitations of RNNs

* **Long-term dependency problem** – information fades over long sequences.
* **Vanishing/exploding gradients** – makes training unstable.
* Solution → **LSTM** and **GRU** architectures.

---

## 6) Lab: Character-Level RNN

A simple example: predict the next character in `"hello"`.

```python
import torch
import torch.nn as nn

chars = "hello"
char_to_idx = {ch: i for i, ch in enumerate(set(chars))}
idx_to_char = {i: ch for ch, i in char_to_idx.items()}

# Input (h, e, l) → Output (e, l, l)
x_data = [char_to_idx[ch] for ch in "hel"]
y_data = [char_to_idx[ch] for ch in "ell"]

x = torch.tensor([x_data], dtype=torch.long)
y = torch.tensor([y_data], dtype=torch.long)

# Embedding + RNN
embedding = nn.Embedding(len(char_to_idx), 10)
rnn = nn.RNN(10, 20, batch_first=True)
fc = nn.Linear(20, len(char_to_idx))

out, _ = rnn(embedding(x))
out = fc(out)

print(out.shape)  # [1, sequence_length, vocab_size]
```

---

## 7) Key Takeaways

* **RNNs** handle sequential data by passing hidden states between time steps.
* They can capture **contextual information**, unlike feedforward networks.
* Suffer from **long-term dependency issues**, later solved by **LSTMs and GRUs**.

---

## 8) What's Next?

In Lecture 12, we'll dive into **Long Short-Term Memory (LSTM)** networks—one of the most important solutions to RNN's limitations.

---

## 🔗 Recommended Links

* [PyTorch RNN Documentation](https://pytorch.org/docs/stable/generated/torch.nn.RNN.html)
* [CS231n RNN Lecture Notes](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture10.pdf)
* [Understanding LSTMs (Colah's Blog)](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)

---