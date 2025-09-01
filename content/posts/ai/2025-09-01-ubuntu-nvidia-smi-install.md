---
categories: [GPU, CUDA, Linux]
cover: /img/ubuntu-cuda-cover.jpg
date: 2025-09-01
description: Step-by-step guide to install NVIDIA driver (nvidia-smi) and test CUDA on Ubuntu, including toolkit setup, sample builds, and common troubleshooting.
image: /img/ubuntu-cuda-cover.jpg
keywords: ubuntu,nvidia-smi,cuda,nvcc,driver,linux,gpu,installation,troubleshooting
layout: post
organiser: Royfactory
tags: [ubuntu, nvidia, cuda, linux, gpu]
title: "Install nvidia-smi and Test CUDA on Ubuntu: A Practical Guide"
slug: install-nvidia-smi-and-test-cuda-ubuntu
toc: true
---

## Introduction
This post walks through installing the NVIDIA driver so that `nvidia-smi` works on Ubuntu, setting up the CUDA Toolkit, and validating the stack with a tiny kernel and `deviceQuery`. It targets Ubuntu 22.04/24.04 (20.04 is similar).

## Prepare the System
- Verify GPU visibility:
```bash
lspci | grep -i nvidia
````

* Update packages and tools:

```bash
sudo apt update && sudo apt -y upgrade
sudo apt -y install build-essential dkms linux-headers-$(uname -r) wget git
```

* Check Secure Boot status:

```bash
mokutil --sb-state
```

## Install NVIDIA Driver (includes `nvidia-smi`)

```bash
ubuntu-drivers devices
sudo ubuntu-drivers autoinstall
sudo reboot
```

After reboot:

```bash
nvidia-smi
lsmod | grep nvidia
```

If `nvidia-smi` is missing, ensure the matching `nvidia-utils-<version>` package is installed.

## Install CUDA Toolkit

### Option A: Ubuntu repo (simple)

```bash
sudo apt install -y nvidia-cuda-toolkit
nvcc --version
```

### Option B: NVIDIA repo (newer)

Install the CUDA keyring, enable the repo for your codename (e.g., `jammy`, `noble`), then:

```bash
sudo apt update
sudo apt install -y cuda-toolkit-12-4
sudo ln -sfn /usr/local/cuda-12.4 /usr/local/cuda
echo 'export PATH=/usr/local/cuda/bin:$PATH' | sudo tee /etc/profile.d/cuda.sh
echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' | sudo tee -a /etc/profile.d/cuda.sh
source /etc/profile.d/cuda.sh
```

## Test CUDA

Minimal sample:

```cpp
#include <cstdio>
#include <cuda_runtime.h>
__global__ void noop() {}
int main(){ int c=0; cudaGetDeviceCount(&c); if(!c){puts("No CUDA"); return 1;}
cudaDeviceProp p; cudaGetDeviceProperties(&p,0);
printf("GPU: %s, SMs: %d\n", p.name, p.multiProcessorCount);
noop<<<1,1>>>(); cudaDeviceSynchronize(); puts("OK");}
```

Build & run:

```bash
nvcc -O2 hello.cu -o hello
./hello
```

Or compile NVIDIA’s `deviceQuery` from `cuda-samples` and ensure `Result = PASS`.

## Troubleshooting

* **Secure Boot**: Disable or enroll MOK; otherwise the kernel module may not load.
* **nouveau conflict**: Blacklist and rebuild initramfs if necessary.
* **GCC mismatch**: Use a supported GCC and pass `-ccbin g++-<ver>` to `nvcc`.
* **Library paths**: Ensure `LD_LIBRARY_PATH` includes `/usr/local/cuda/lib64` when using NVIDIA repo.

## Conclusion

Get `nvidia-smi` working by installing the recommended driver, then add CUDA Toolkit via Ubuntu or NVIDIA repo. Validate with `nvcc --version`, a minimal kernel, and `deviceQuery`. Watch for Secure Boot, nouveau, and GCC compatibility to avoid common pitfalls.

---

### Summary

* Install the recommended NVIDIA driver; `nvidia-smi` should work after reboot.
* Choose CUDA via Ubuntu repo (simple) or NVIDIA repo (newer).
* Verify with `nvcc`, a tiny kernel, and `deviceQuery`.
* Mind Secure Boot, nouveau, and GCC compatibility.