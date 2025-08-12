---
ShowToc: true
categories: [ai]
date: 2025-08-12
description: Step-by-step guide to setting up your AI development environment with Anaconda, Jupyter Notebook, and GPU acceleration. Includes installation commands, verification scripts, and best practices for a stable ML/DL workflow.
draft: false
image: /img/ai-development-environment.jpg
keywords: ai development environment, anaconda setup, jupyter notebook, gpu configuration, cuda cudnn, tensorflow gpu, pytorch gpu
tags: [ai, setup, environment, anaconda, jupyter, gpu, cuda, cudnn, tensorflow, pytorch]
title: 'AI Development Environment Setup: Anaconda, Jupyter, and GPU Acceleration (Lecture 4)'
slug: ai-development-environment
--------------------------------

# AI Development Environment Setup: Anaconda, Jupyter, and GPU Acceleration (Lecture 4)

In this lecture, we’ll set up a **stable AI development environment** for Machine Learning and Deep Learning projects. You’ll learn how to install **Anaconda**, run **Jupyter Notebook**, and configure **GPU acceleration** with CUDA and cuDNN.

---

## Table of Contents

{% toc %}

---

## 1) Why Environment Setup Matters

A well-configured environment prevents common issues such as:

* Library version conflicts
* Slow training due to CPU-only execution
* Non-reproducible results across team members

**Goals:**

1. Create isolated Python environments
2. Install essential ML/DL libraries
3. Enable GPU acceleration
4. Set up a convenient coding workspace

---

## 2) Essential Tools Overview

### 2.1 Anaconda

* Manages Python versions and packages in isolated environments.
* Avoids dependency conflicts between projects.

### 2.2 Jupyter Notebook

* Interactive browser-based Python IDE.
* Perfect for experiments, data analysis, and sharing code.

### 2.3 GPU (CUDA + cuDNN)

* NVIDIA GPUs drastically speed up training.
* Requires correct CUDA Toolkit and cuDNN installation.

---

## 3) Installing Anaconda and Creating an Environment

> **Download Anaconda**: [https://www.anaconda.com/download](https://www.anaconda.com/download)

1. Create a new virtual environment:

   ```bash
   conda create -n ai_env python=3.10
   ```
2. Activate the environment:

   ```bash
   conda activate ai_env
   ```
3. Install essential packages:

   ```bash
   conda install numpy pandas matplotlib scikit-learn
   pip install tensorflow torch
   ```

---

## 4) Installing and Running Jupyter Notebook

1. Install Jupyter:

   ```bash
   conda install jupyter
   ```
2. Launch Jupyter:

   ```bash
   jupyter notebook
   ```
3. Open the provided URL (e.g., `http://localhost:8888`) in your browser.
4. Create a new Python notebook and start coding.

---

## 5) Configuring GPU (NVIDIA Only)

### 5.1 Install CUDA Toolkit & cuDNN

* **CUDA Toolkit**: [https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads)
* **cuDNN**: [https://developer.nvidia.com/cudnn](https://developer.nvidia.com/cudnn)
* After installation, add `CUDA_PATH` to your system environment variables.

### 5.2 Verify GPU Availability (TensorFlow Example)

```python
import tensorflow as tf
print("TensorFlow version:", tf.__version__)
print("GPU available:", tf.config.list_physical_devices('GPU'))
```

**Example Output**

```
TensorFlow version: 2.15.0
GPU available: [PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```

---

## 6) Lab: Environment Verification Script

Run the following in Jupyter Notebook to confirm your setup:

```python
import numpy as np
import tensorflow as tf
import torch

print("NumPy version:", np.__version__)
print("TensorFlow GPU:", tf.config.list_physical_devices('GPU'))
print("PyTorch GPU:", torch.cuda.is_available())
print("PyTorch CUDA version:", torch.version.cuda)
```

**Expected Output**

```
NumPy version: 1.26.4
TensorFlow GPU: [PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
PyTorch GPU: True
PyTorch CUDA version: 12.1
```

---

## 7) Key Takeaways

* **Anaconda** keeps Python environments isolated and conflict-free.
* **Jupyter Notebook** is ideal for ML/DL experiments.
* **GPU acceleration** significantly boosts training speed.
* Always verify your setup after installation.

---

## 8) What’s Next?

In Lecture 5, we’ll cover **Data Preprocessing and Visualization**—handling missing values, detecting outliers, normalizing data, and creating visualizations.

---