---
ShowToc: true
categories:
- kubernetes
date: 2025-07-16
description: Ready to install Kubernetes? In this beginner-friendly guide, we walk
  through how to install Kubernetes on your local machine using Minikube, and how
  to build production-grade clusters with kubeadm.
draft: false
image: /img/installing-kubernetes-cover.jpg
keywords: kubernetes, k8s, install kubernetes, minikube, kubeadm, cluster setup, local
  kubernetes, beginner kubernetes installation, cloud-native devops
tags:
- kubernetes
- k8s
- install
- minikube
- kubeadm
- devops
- local-cluster
- cloud-native
- beginner
title: 'Installing Kubernetes: Minikube and kubeadm Setup for Beginners'
---

# Installing Kubernetes: Minikube and kubeadm Setup for Beginners

So far, we’ve explored what Kubernetes is, how it works, and why it matters.

Now it's time to **get our hands dirty** and install Kubernetes ourselves.

In this post, you’ll learn:

- What installation methods are available
- How to set up Kubernetes easily using **Minikube**
- How to create a production-style cluster using **kubeadm**
- Tips for working with cloud-based Kubernetes

## Table of Contents
---
## 1. Why Is Installing Kubernetes Hard?

Kubernetes is a **distributed system**, not just one program.

You need to install and connect:

- API server
- Scheduler
- Controller manager
- etcd (database)
- kubelet and kube-proxy (on worker nodes)
- Networking plugin
- And more...

But don’t worry — we’ll use beginner-friendly tools like **Minikube** to make this much easier.

---

## 2. Comparing Installation Methods

| Method           | Description                             | Pros                        | Cons                       |
|------------------|-----------------------------------------|-----------------------------|----------------------------|
| **Minikube**     | Local single-node cluster                | Easy, great for learning    | Not for production use     |
| **k3s**          | Lightweight Kubernetes variant           | Fast, low-resource          | Limited advanced features  |
| **kubeadm**      | Official tool for real clusters          | Realistic, flexible         | Requires Linux/VM setup    |
| **Managed K8s**  | Cloud-based Kubernetes (EKS/GKE/AKS)     | Fully automated             | Requires cloud knowledge   |

---

## 3. Getting Started with Minikube

### What is Minikube?

Minikube creates a single-node Kubernetes cluster on your local machine. Perfect for learning and development.

### Prerequisites

- OS: Windows, macOS, or Linux
- Virtualization support (Docker or VirtualBox)
- `kubectl` installed

---

Using Homebrew:

```bash
brew install minikube
````

Or manually:

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64
chmod +x minikube-darwin-amd64
sudo mv minikube-darwin-amd64 /usr/local/bin/minikube
```

---

```bash
minikube start
```

Minikube will:

* Create a virtual machine
* Initialize Kubernetes control plane
* Deploy system components (DNS, dashboard, etc.)

---

```bash
kubectl get nodes
```

Expected output:

```
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   1m    v1.29.0
```

---

```bash
minikube dashboard
```

This opens a GUI in your browser to view and manage your cluster visually.

---

## 4. Installing Kubernetes with kubeadm

### What is kubeadm?

`kubeadm` is the **official tool** to bootstrap a production-ready Kubernetes cluster. It’s more complex than Minikube but more realistic.

---

* 2 or more Linux servers (Ubuntu 22.04)

  * 1 master, 1+ workers
* containerd as container runtime
* `kubelet`, `kubeadm`, `kubectl` installed

---

#### 1) Prepare the OS

```bash
sudo apt update && sudo apt install -y apt-transport-https curl
```

#### 2) Install containerd

```bash
sudo apt install -y containerd
sudo systemctl enable containerd
```

#### 3) Install Kubernetes tools

```bash
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
```

Add Kubernetes repo, then:

```bash
sudo apt update
sudo apt install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```

---

```bash
sudo kubeadm init --pod-network-cidr=10.244.0.0/16
```

---

```bash
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
```

---

```bash
kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
```

---

Run the `kubeadm join` command shown after initialization on each worker node.

---

## 5. Post-Installation Checklist

* ✅ All Nodes show `Ready` in `kubectl get nodes`
* ✅ All system Pods are `Running`
* ✅ DNS works (`coredns`)
* ✅ Optional: Enable Kubernetes dashboard

---

## 6. Installing Kubernetes in the Cloud

If you're using AWS, GCP, or Azure, consider their **managed Kubernetes services**:

| Provider | Service | Highlights                         |
| -------- | ------- | ---------------------------------- |
| AWS      | EKS     | IAM support, VPC integration       |
| GCP      | GKE     | Fast startup, good default configs |
| Azure    | AKS     | Azure DevOps and AD support        |

Benefits:

* No manual setup
* Built-in scalability and HA
* Pay-as-you-go billing

---

## 7. Bonus: Recommended Tools

| Tool   | Use Case                               |
| ------ | -------------------------------------- |
| Lens   | Visual Kubernetes cluster management   |
| k9s    | Terminal UI for exploring Kubernetes   |
| Kind   | Run K8s in Docker for CI/testing       |
| Okteto | Sync local development with Kubernetes |

---

## Summary

Installing Kubernetes can feel overwhelming — but with the right tools and guidance, **you can be up and running in no time**.

Here’s what we covered:

| Method      | Best For                   |
| ----------- | -------------------------- |
| Minikube    | Learning on your local PC  |
| kubeadm     | Building real clusters     |
| EKS/GKE/AKS | Production cloud workloads |

---

## What’s Next?

Now that your cluster is live, it’s time to learn how to **control it using `kubectl`** — the command-line tool that every Kubernetes developer must know.