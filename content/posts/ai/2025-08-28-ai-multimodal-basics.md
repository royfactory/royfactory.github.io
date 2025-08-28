---
ShowToc: true
categories: [ai, multimodal]
date: 2025-08-28
description: Introduction to Multimodal AI combining text and images. Learn core concepts, key models like CLIP and BLIP, and try hands-on examples for image captioning and text-to-image retrieval using Hugging Face.
draft: false
image: /img/ai-multimodal-basics.jpg
keywords: multimodal ai, clip, blip, huggingface, image captioning, text to image retrieval, deep learning, ai basics
tags: [ai, multimodal, clip, blip, huggingface, image-captioning, retrieval, deep-learning]
title: 'Multimodal AI Basics: Text + Image Understanding with CLIP and BLIP (Lecture 19)'
slug: ai-multimodal-basics
---

# Multimodal AI Basics: Text + Image Understanding with CLIP and BLIP (Lecture 19)

In this lecture, we’ll explore **Multimodal AI**, which combines different modalities like **text and images** to create more powerful and human-like AI systems.  
Just as humans can read a sentence while looking at a picture, multimodal AI models learn to connect language and vision.

---

## Table of Contents
{% toc %}

---

## 1) What is Multimodal AI?

- **Modality:** A type of input data (e.g., text, image, audio)  
- **Multimodal AI:** Processes and integrates multiple modalities at once  

### Examples:
- **Image Captioning** → Generate a description of an image  
- **Text-to-Image Retrieval** → Find images based on text queries  
- **Text-to-Image Generation** → Create images from textual prompts (e.g., DALL·E, Stable Diffusion)  

---

## 2) Why Is It Important?

- **Human-like intelligence**: Humans naturally combine vision, speech, and text  
- **Expanded applications**: Search engines, recommendation systems, self-driving cars, healthcare  
- **Generative AI growth**: Beyond text-only, multimodal AI powers new experiences like text-to-image and text-to-video  

---

## 3) Key Multimodal Models

1. **CLIP (Contrastive Language-Image Pretraining)** – OpenAI  
   - Maps text and images into the same embedding space  
   - Example: “a photo of a cat” and an actual cat image end up close together  

2. **BLIP, Flamingo, Kosmos-1**  
   - Advanced multimodal models that combine image + text inputs for reasoning and generation  

---

## 4) Hands-On Example: Image Captioning with BLIP

```python
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

# 1. Load an example image
url = "https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png"
image = Image.open(requests.get(url, stream=True).raw)

# 2. Load BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# 3. Process input
inputs = processor(images=image, return_tensors="pt")

# 4. Generate caption
out = model.generate(**inputs)
caption = processor.decode(out[0], skip_special_tokens=True)

print("Caption:", caption)
````

**Sample Output:**

```
Caption: Two parrots sitting on a branch.
```

---

## 5) Hands-On Example: Text-to-Image Retrieval with CLIP

```python
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import requests
import torch

# 1. Load two sample images
urls = [
    "https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png",
    "https://huggingface.co/datasets/Narsil/image_dummy/raw/main/cheetah.png"
]
images = [Image.open(requests.get(u, stream=True).raw) for u in urls]

# 2. Load CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# 3. Encode text and images
text = ["a photo of parrots", "a photo of a cheetah"]
inputs = processor(text=text, images=images, return_tensors="pt", padding=True)

# 4. Compute similarity
outputs = model(**inputs)
logits_per_image = outputs.logits_per_image
probs = logits_per_image.softmax(dim=1)

print("Similarity probabilities:", probs)
```

**Sample Output:**

```
Similarity probabilities: tensor([[0.95, 0.05]])
```

→ Confirms the first image is strongly related to “a photo of parrots.”

---

## 6) Key Takeaways

* **Multimodal AI** combines text + images (and beyond) for richer understanding
* **CLIP** maps text and images into a shared embedding space
* **BLIP** enables natural image captioning
* Hugging Face provides ready-to-use pretrained models for experimentation

---

## 7) What’s Next?

In **Lecture 20**, we’ll wrap up this series by discussing **AI Project Planning and Real-World Applications**, showing how to design and apply AI systems in practice.