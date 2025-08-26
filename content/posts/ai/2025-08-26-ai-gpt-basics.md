---
ShowToc: true
categories: [ai, nlp]
date: 2025-08-26
description: Introduction to GPT (Generative Pretrained Transformer). Learn its autoregressive architecture, pretraining with next-token prediction, and try a hands-on text generation example with Hugging Face GPT-2.
draft: false
image: /img/ai-gpt-basics.jpg
keywords: gpt basics, generative pretrained transformer, gpt2 text generation, autoregressive model, transformer decoder, huggingface gpt, chatgpt
tags: [ai, gpt, transformer, nlp, text-generation, huggingface, autoregressive, deep-learning]
title: 'GPT Basics: Generative Pretrained Transformer Explained (Lecture 17)'
slug: ai-gpt-basics
---

# GPT Basics: Generative Pretrained Transformer Explained (Lecture 17)

In this lecture, we’ll explore **GPT (Generative Pretrained Transformer)**, a Transformer-based model introduced by OpenAI in 2018.  
While **BERT** excels at understanding text (encoder-based), **GPT specializes in generating text (decoder-based)**.  
GPT has since evolved into the foundation of **ChatGPT and GPT-4**.

---

## Table of Contents
{% toc %}

---

## 1) Why GPT?

GPT is designed to **predict the next token** in a sequence (autoregressive modeling).  
This makes it excellent at generating coherent, human-like text.

- **Pretraining:** Train on massive text corpora with next-token prediction  
- **Fine-tuning:** Adapt the pretrained model to specific tasks (e.g., summarization, QA, dialogue)  
- **Autoregressive Generation:** Words are generated one by one, conditioned on all previous words  

---

## 2) GPT vs BERT

| Feature       | BERT | GPT |
|---------------|------|-----|
| Architecture  | Transformer Encoder | Transformer Decoder |
| Objective     | Masked Language Model + NSP | Next Token Prediction |
| Strength      | Understanding (classification, QA) | Generation (text, dialogue) |
| Applications  | Search, QA, NER | Chatbots, story/article generation, code generation |

---

## 3) GPT Architecture

- Based on **Transformer Decoder blocks**  
- **Masked Self-Attention:** ensures the model only attends to past tokens, not future ones  
- **Positional Encoding:** adds sequence order information  
- **Feed-Forward Layers:** transform token representations  
- Stacked layers enable powerful text generation capabilities  

---

## 4) Hands-On: Text Generation with Hugging Face GPT-2

```python
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# 1. Load tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# 2. Encode input text
input_text = "Today is really"
inputs = tokenizer.encode(input_text, return_tensors="pt")

# 3. Generate text
outputs = model.generate(
    inputs,
    max_length=30,
    num_return_sequences=1,
    do_sample=True,
    top_k=50
)

# 4. Decode output
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
````

**Sample Output:**

```
Today is really beautiful, and I feel like going for a walk in the park.
```

---

## 5) Applications of GPT

* **Chatbots and dialogue systems**
* **Text generation** (articles, stories, marketing copy)
* **Code generation** (e.g., GitHub Copilot)
* **Summarization and translation**

---

## 6) Key Takeaways

* GPT is an **autoregressive, Transformer decoder-based model**
* Excels at **text generation**, complementing BERT’s text understanding
* Can be easily used with Hugging Face’s GPT-2 for experimentation

---

## 7) What’s Next?

In **Lecture 18**, we’ll explore **Practical Applications of Transformers**, focusing on **text summarization and translation** using pretrained models.

---