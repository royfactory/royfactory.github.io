---
ShowToc: true
categories: [ai, nlp]
date: 2025-08-16
description: Learn the fundamentals of Word Embeddings in NLP, including Word2Vec, GloVe, and modern transformer-based embeddings. Includes Python examples with gensim and PyTorch.
draft: false
image: /img/word-embedding-guide.jpg
keywords: word embedding, word2vec, glove, nlp embedding, semantic similarity, vector space, gensim, pytorch, transformer embeddings
tags: [ai, nlp, word2vec, glove, embedding, pytorch, gensim, transformers, semantic-similarity]
title: 'Word Embeddings in NLP: From Word2Vec to Transformers (Lecture 10)'
slug: ai-word-embedding
---

# Word Embeddings in NLP: From Word2Vec to Transformers (Lecture 10)

In this lecture, we will explore **Word Embeddings**, a fundamental concept in Natural Language Processing (NLP) that allows machines to understand words in terms of **vectors**. Instead of treating words as discrete symbols, embeddings capture **semantic meaning** by placing similar words closer in a vector space.

---

## Table of Contents

{% toc %}

---

## 1) What Are Word Embeddings?

Word embeddings are numerical representations of words in a continuous vector space.

- Similar words are closer in the space  
- Capture semantic and syntactic relationships  
- Improve machine learning performance for NLP tasks  

Example:  
- "king" - "man" + "woman" ≈ "queen"  

This property is known as **word vector arithmetic**.

---

## 2) Popular Word Embedding Techniques

### 2.1 Word2Vec  
- Introduced by Google (Mikolov et al., 2013)  
- Two models: CBOW (predict word from context) and Skip-gram (predict context from word)  
- Learns embeddings efficiently from large corpora  

### 2.2 GloVe  
- Developed by Stanford (Pennington et al., 2014)  
- Stands for "Global Vectors for Word Representation"  
- Uses co-occurrence matrix factorization  

### 2.3 Transformer-based Embeddings  
- Modern models like **BERT** or **GPT**  
- Contextual embeddings (word meaning changes depending on sentence context)  
- Outperform static embeddings in most NLP tasks  

---

## 3) Implementing Word2Vec with Gensim

```python
from gensim.models import Word2Vec

# Sample corpus
sentences = [
    ["king", "queen", "man", "woman"],
    ["paris", "france", "london", "england"],
    ["apple", "banana", "fruit", "market"]
]

# Train Word2Vec model
model = Word2Vec(sentences, vector_size=50, window=3, min_count=1, workers=2)

# Check similarity
print(model.wv.most_similar("king"))
print(model.wv.similarity("king", "queen"))
````

**Expected Output (example):**

```
[('queen', 0.85), ('man', 0.72), ('woman', 0.70)]
0.85
```

---

## 4) Using Pretrained Embeddings (GloVe)

Download pretrained vectors: [https://nlp.stanford.edu/projects/glove/](https://nlp.stanford.edu/projects/glove/)

```python
import numpy as np

embeddings_index = {}
with open("glove.6B.50d.txt", encoding="utf-8") as f:
    for line in f:
        values = line.split()
        word = values[0]
        vector = np.asarray(values[1:], dtype="float32")
        embeddings_index[word] = vector

print("Vector for 'computer':", embeddings_index["computer"][:10])
```

---

## 5) Contextual Embeddings with Transformers

Using Hugging Face Transformers:

```python
from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

inputs = tokenizer("I love natural language processing", return_tensors="pt")
outputs = model(**inputs)

# Last hidden state (contextual embeddings)
embeddings = outputs.last_hidden_state
print(embeddings.shape)
```

**Expected Output**

```
torch.Size([1, 6, 768])
```

(1 sentence, 6 tokens, embedding dimension 768)

---

## 6) Applications of Word Embeddings

* Sentiment analysis
* Machine translation
* Chatbots and Q\&A systems
* Document classification
* Semantic search

---

## 7) Key Takeaways

* **Word embeddings** transform words into vectors that capture semantic meaning.
* **Word2Vec and GloVe** are static embeddings (same vector regardless of context).
* **Transformers (BERT, GPT)** provide contextual embeddings (different vectors based on sentence usage).
* Embeddings are the backbone of modern NLP systems.

---

## 8) What's Next?

In Lecture 11, we will explore **RNNs (Recurrent Neural Networks)** and how they process sequential data like text.

---

## Recommended Resources

* [Word2Vec Paper (Mikolov et al., 2013)](https://arxiv.org/abs/1301.3781)
* [GloVe Project (Stanford NLP)](https://nlp.stanford.edu/projects/glove/)
* [Hugging Face Transformers](https://huggingface.co/transformers/)

---
