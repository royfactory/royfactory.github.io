---
categories: kubernetes
cover: /img/kubernetes-architecture-cover.jpg
date: 2025-07-14
description: Kubernetes is a powerful system, but how does it actually work? In this post, we explore the full architecture of Kubernetes — from Control Plane to Worker Nodes — with simple diagrams and real-world analogies.
image: /img/kubernetes-architecture-cover.jpg
keywords: kubernetes, k8s, kubernetes architecture, cluster, nodes, control plane, api server, kubelet, scheduler, etcd, cloud native
layout: post
organiser: Royfactory
tags: kubernetes k8s architecture cluster node pod control-plane beginner devops cloud-native
title: 'Kubernetes Architecture: How It All Works Behind the Scenes'
toc: true
---

# Kubernetes Architecture: How It All Works Behind the Scenes

If you've already learned the basic concepts of Kubernetes — like Pods, Nodes, and Services — the next big step is understanding **how all these pieces come together**.

This post will guide you through the complete architecture of a Kubernetes cluster. You’ll learn:

- What components make up the Control Plane
- What happens inside Worker Nodes
- How requests flow from your `kubectl` command to actual running containers
- Why Kubernetes is designed the way it is

Let’s get started.

---

## 1. Kubernetes Is Cluster-Based

At its core, Kubernetes is a **cluster** — a group of computers that act as one big system. These machines (called **nodes**) can be physical servers or virtual machines.

The cluster is split into two roles:

| Role             | Description                                          |
|------------------|------------------------------------------------------|
| **Control Plane**| Makes decisions and manages the cluster              |
| **Worker Nodes** | Run your application containers (Pods)               |

When you deploy an application to Kubernetes, the Control Plane decides **how** and **where** it should run, and the Worker Nodes actually run it.

---

## 2. Visualizing the Architecture

Let’s draw a simple text-based diagram of the Kubernetes architecture:

```

+-----------------------------------------------------------+
\|                       Control Plane                       |
\|                                                           |
\|  +------------+     +---------------+    +--------------+ |
\|  |  APIServer | <-> | Scheduler     | -> | Controller    | |
\|  |            |     |               |    | Manager       | |
\|  +------------+     +---------------+    +--------------+ |
\|          |                                         ^      |
\|          v                                         |      |
\|      etcd (DB)                                     |      |
+-----------------------------------------------------------+
|
v
+-----------------------------------------------------------+
\|                     Worker Nodes (Many)                   |
\|                                                           |
\|  +-------------+   +-------------+   +-------------+      |
\|  | Node 1      |   | Node 2      |   | Node 3      | ...  |
\|  | +---------+ |   | +---------+ |   | +---------+ |      |
\|  | |  kubelet | |   | |  kubelet | |   | |  kubelet | |      |
\|  | +---------+ |   | +---------+ |   | +---------+ |      |
\|  | |  Pods    | |   | |  Pods    | |   | |  Pods    | |      |
\|  | +---------+ |   | +---------+ |   | +---------+ |      |
\|  | |kube-proxy| |   | |kube-proxy| |   | |kube-proxy| |      |
\|  +-------------+   +-------------+   +-------------+      |
+-----------------------------------------------------------+

````

---

## 3. Components of the Control Plane

### 1) API Server

The **entry point** to Kubernetes. All requests — from `kubectl`, dashboards, or internal components — go through the API Server.

- Front-end to the cluster
- Validates and processes REST requests
- Talks to `etcd` and other controllers

> **Analogy**: The reception desk of a company

---

### 2) etcd

A **key-value store** that acts as the **single source of truth** for your cluster. Stores configuration, states, secrets, and metadata.

- Highly available distributed database
- Used by the API Server for all reads/writes
- Built on the Raft consensus algorithm

> **Analogy**: Central filing cabinet or ERP system

---

### 3) Scheduler

Decides **which Node** should run a new Pod, based on available resources, affinity rules, and policies.

- Only makes placement decisions — doesn’t run the Pods
- Optimizes for resource utilization

> **Analogy**: Manager assigning tasks to available workers

---

### 4) Controller Manager

Ensures that the cluster’s **desired state** (as defined by YAML files) matches the **actual state**.

- Contains sub-controllers like ReplicaSetController, DeploymentController, etc.
- Handles auto-scaling, rolling updates, and fault recovery

> **Analogy**: Supervisor who watches and corrects the workflow

---

## 4. Components of the Worker Node

### 1) kubelet

The **primary agent** on each Worker Node. Takes instructions from the Control Plane and ensures containers are running.

- Communicates with the API Server
- Monitors Pod health
- Starts and stops containers via the container runtime

> **Analogy**: Team leader on the factory floor

---

### 2) kube-proxy

Handles **network communication** between Pods, across Nodes, and through Services.

- Implements NAT and forwarding rules
- Maintains network consistency

> **Analogy**: The switchboard operator or mailroom

---

### 3) Container Runtime

The software that actually runs containers. Examples include:

- **Docker** (deprecated in favor of containerd)
- **containerd**
- **CRI-O**

---

## 5. How a `kubectl` Request Flows

Let’s walk through what happens when you run `kubectl apply -f app.yaml`.

1. `kubectl` sends a request to the **API Server**
2. The **API Server** validates and stores the object in **etcd**
3. The **Scheduler** notices a new Pod is pending and selects a Node
4. The **kubelet** on that Node gets notified and starts the Pod
5. **kube-proxy** updates networking so the Pod is reachable

---

## 6. Kubernetes Is Declarative

Instead of giving step-by-step commands, you declare **what** you want, and Kubernetes figures out **how** to achieve it.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp
spec:
  containers:
    - name: app
      image: nginx
````

This YAML tells Kubernetes: “I want a Pod named `myapp` that runs nginx.”
Kubernetes ensures that this Pod exists and keeps it running — even if something fails.

---

## 7. High Availability (HA) and Redundancy

Kubernetes is designed for **resilience**. Every critical component can be replicated:

* Control Plane can have multiple API Servers, Schedulers, etc.
* `etcd` uses quorum-based consensus for consistency
* If a Node fails, Pods are moved elsewhere

> This is why Kubernetes is used for mission-critical systems.

---

## 8. On-Premises vs Cloud Architecture

Kubernetes runs anywhere, but setups differ slightly:

| Feature       | On-Premises             | Cloud (e.g. EKS, GKE)      |
| ------------- | ----------------------- | -------------------------- |
| Load Balancer | Manual setup            | Built-in cloud integration |
| Storage       | NFS, local disks        | EBS, GCP Disk, etc.        |
| Auto-scaling  | Requires custom tooling | Built-in                   |
| HA Setup      | Complex to configure    | Often managed by provider  |

---

## 9. Summary Table

| Component          | Role                                         |
| ------------------ | -------------------------------------------- |
| API Server         | Accepts and validates requests               |
| etcd               | Stores all cluster data                      |
| Scheduler          | Assigns Pods to Nodes                        |
| Controller Manager | Maintains desired state                      |
| kubelet            | Executes Pods on Worker Nodes                |
| kube-proxy         | Handles networking between Pods and Services |
| Container Runtime  | Runs the actual containerized applications   |

---

## 10. Final Thoughts

The Kubernetes architecture may seem complex at first, but each part has a clear, focused responsibility.

* The **Control Plane** decides what should happen
* The **Worker Nodes** make it happen
* Together, they form a self-healing, scalable system

Understanding this architecture is crucial before diving deeper into YAML files, kubectl commands, and workload management.