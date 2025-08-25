---
ShowToc: true
categories: [ai, nlp]
date: 2025-08-25
description: Introduction to BERT architecture and pretraining. Learn how BERT uses bidirectional transformers, Masked Language Modeling (MLM), and Next Sentence Prediction (NSP), with a hands-on Hugging Face example.
draft: false
image: /img/ai-bert-basics.jpg
keywords: bert basics, bert pretraining, masked language model, next sentence prediction, transformers, huggingface, nlp, deep learning
tags: [ai, nlp, bert, transformer, pretraining, huggingface, deep-learning]
title: 'BERT Architecture and Pretraining: From MLM to NSP (Lecture 16)'
slug: ai-bert-basics
---

# BERT Architecture and Pretraining: From MLM to NSP (Lecture 16)

In this lecture, we’ll explore **BERT (Bidirectional Encoder Representations from Transformers)**, a groundbreaking model introduced by Google in 2018.  
BERT significantly advanced NLP by introducing **bidirectional context learning** and a **pretraining + fine-tuning framework**, becoming the foundation for many state-of-the-art models.

---

## Table of Contents
{% toc %}

---

## 1) Why BERT?

Previous language models read text in only one direction (left-to-right or right-to-left).  
BERT, however, learns **context from both directions simultaneously**, making it far better at understanding word meaning in context.

Additionally, BERT is trained with **pretraining** on massive text corpora and then **fine-tuned** on specific downstream tasks like classification, QA, or NER.

---

## 2) Core Pretraining Objectives

### 2.1 Masked Language Model (MLM)  
Randomly mask some words and predict them:  
- Input: *"I ate an [MASK] today."*  
- Output: *"apple"*  

This trains BERT to learn context in both directions.

### 2.2 Next Sentence Prediction (NSP)  
Teach the model to understand relationships between sentences:  
- A: "I watched a movie."  
- B: "It was really fun." → **Is Next (1)**  
- B: "I cooked dinner." → **Not Next (0)**  

By combining MLM and NSP, BERT learns both **word-level** and **sentence-level** context.

---

## 3) BERT Architecture

- Based on the **Transformer Encoder** only  
- Input tokens → token embeddings + positional encoding + segment embeddings  
- Multiple layers of **multi-head self-attention** and **feed-forward networks**  
- Produces deep contextual representations for every word  

---

## 4) Hands-On: Using Pretrained BERT with Hugging Face

Here’s how to load a pretrained BERT model for classification:

```python
from transformers import BertTokenizer, TFBertForSequenceClassification
import tensorflow as tf

# 1. Load tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# 2. Encode input
inputs = tokenizer("BERT is a powerful NLP model", return_tensors="tf")

# 3. Load pretrained BERT model
model = TFBertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

# 4. Run inference
outputs = model(inputs)
logits = outputs.logits

print("Logits:", logits)
````

**Sample Output:**

```
Logits: tf.Tensor([[-0.12  0.45]], shape=(1, 2), dtype=float32)
```

---

## 5) Applications of BERT

* **Text classification** (sentiment analysis, topic classification)
* **Question answering** (SQuAD benchmark, chatbots)
* **Named Entity Recognition (NER)**
* **Semantic similarity and search**

---

## 6) Key Takeaways

* BERT uses **bidirectional transformers** for deep context understanding.
* Pretrained with **MLM and NSP**, then fine-tuned for specific tasks.
* Hugging Face provides easy-to-use implementations for real-world use cases.

---

## 7) What’s Next?

In **Lecture 17**, we’ll study **GPT (Generative Pretrained Transformer)**, a generative language model that powers systems like ChatGPT.