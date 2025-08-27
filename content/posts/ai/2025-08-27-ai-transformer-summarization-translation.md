---
ShowToc: true
categories: [ai, nlp]
date: 2025-08-27
description: Learn how to apply Transformers for text summarization and translation. Covers extractive vs abstractive summarization, machine translation basics, and hands-on Hugging Face examples with BART and MarianMT.
draft: false
image: /img/ai-transformer-summarization-translation.jpg
keywords: transformer applications, text summarization, translation, abstractive summarization, bart summarization, marianmt translation, huggingface transformers
tags: [ai, transformer, summarization, translation, nlp, huggingface, bart, marianmt]
title: 'Transformer Applications: Summarization and Translation (Lecture 18)'
slug: ai-transformer-summarization-translation
---

# Transformer Applications: Summarization and Translation (Lecture 18)

In this lecture, we’ll explore two of the most practical applications of Transformers: **text summarization** and **machine translation**.  
Transformers excel at both tasks by leveraging their **self-attention mechanism**, which captures long-range dependencies and contextual meaning far better than RNN-based models.

---

## Table of Contents
{% toc %}

---

## 1) Text Summarization

Text summarization comes in two main forms:

1. **Extractive Summarization**  
   Selects key sentences directly from the original text.  
   Example: Picking the 2–3 most important sentences from a news article.

2. **Abstractive Summarization**  
   Generates new sentences that capture the meaning of the source.  
   Example:  
   - Original: "AI is growing rapidly and applied in healthcare, finance, and manufacturing."  
   - Summary: "AI adoption is accelerating across industries."  

Modern Transformer-based models (e.g., **BART, T5**) typically perform **abstractive summarization**.

---

## 2) Machine Translation

Machine translation was one of the primary motivations for the original Transformer paper.  
Unlike RNN-based translators, Transformers achieve **higher accuracy** and **more natural phrasing**.  

Today’s widely used systems such as **Google Translate** and **DeepL** rely on Transformer architectures.

---

## 3) Hands-On with Hugging Face

### 3.1 Summarization Example (BART)

```python
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

text = """
Artificial Intelligence (AI) has rapidly advanced in recent years,
already being applied in healthcare, finance, and manufacturing.
It is expected to further transform automation, predictive analytics,
and personalized services in the future.
"""

summary = summarizer(text, max_length=40, min_length=10, do_sample=False)
print("Summary:", summary[0]['summary_text'])
````

**Sample Output:**

```
AI is rapidly advancing, impacting industries and driving automation and personalization.
```

---

### 3.2 Translation Example (English → Korean)

```python
from transformers import pipeline

translator = pipeline("translation_en_to_ko", model="Helsinki-NLP/opus-mt-en-ko")

text = "Artificial Intelligence is transforming industries across the world."
translation = translator(text)
print("Translation:", translation[0]['translation_text'])
```

**Sample Output:**

```
인공지능은 전 세계의 산업을 변화시키고 있다.
```

---

## 4) Applications in Real Life

* **Summarization**: News articles, meeting minutes, academic papers
* **Translation**: Global communication, multilingual services, cross-border collaboration
* **Combined**: Summarize and translate simultaneously for international reports

---

## 5) Key Takeaways

* Transformers excel at both **summarization** and **translation**.
* Summarization can be **extractive** or **abstractive**, with modern models favoring abstractive approaches.
* Hugging Face pipelines make it easy to experiment with pretrained models like **BART** and **MarianMT**.

---

## 6) What’s Next?

In **Lecture 19**, we’ll explore **Multimodal AI (Text + Image)** and how Transformers extend beyond language into vision and other domains.

---
