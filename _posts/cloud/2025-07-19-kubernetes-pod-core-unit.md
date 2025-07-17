---
categories: kubernetes
cover: /img/kubernetes-pod-core-unit.jpg
date: 2025-07-19
description: In Kubernetes, the Pod is the smallest deployable unit. This post covers what a Pod is, why it's needed, and how to create and inspect Pods with practical examples.
image: /img/kubernetes-pod-core-unit.jpg
keywords: Kubernetes, Pod, container, cluster, k8s basics, DevOps, kubectl, yaml, sidecar
layout: post
organiser: Royfactory
tags: kubernetes pod k8s containers devops beginner guide kubectl yaml
title: 'Understanding Pods: The Core Unit of Kubernetes'
toc: true
---

# Understanding Pods: The Core Unit of Kubernetes

If you're learning Kubernetes, you'll quickly encounter the term **Pod** — it's not just another buzzword.  
Pods are **the smallest deployable unit in Kubernetes**, and they serve as the foundation for everything else.

In this post, we’ll explore:

- What a Pod actually is
- Why Pods are necessary
- Pod structure and real examples
- How to create and inspect a Pod
- Differences between single and multi-container Pods

---

## 1. What Is a Pod?

A **Pod** is a logical wrapper around one or more containers.

- It provides shared networking and storage resources.
- Most Pods contain **a single container**.
- When multiple containers are tightly coupled (e.g., app + helper), they can live in the same Pod.

Kubernetes does **not manage containers directly**, but manages them through Pods.

---

## 2. Why Do We Need Pods?

You might wonder — why not just run containers directly?

### Reason 1: Kubernetes Resource Unit

Kubernetes manages resources like scaling, scheduling, and health checks **at the Pod level**, not individual containers.

### Reason 2: Sidecar Pattern

In scenarios like:

- An app server + log forwarder
- A web app + cache

Multiple containers can work together in the same Pod, sharing network and sometimes storage.

---

## 3. Inside a Pod: Structure

A Pod consists of:

| Component         | Description                                       |
|------------------|---------------------------------------------------|
| Containers        | One or more app containers                       |
| Shared network    | One IP address shared among all containers       |
| Shared volumes    | For shared data between containers               |
| Metadata          | Name, labels, annotations                        |
| Policies          | Restart policy, readiness/liveness probes       |

### Example: Minimal Pod YAML

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
    - name: nginx
      image: nginx:latest
      ports:
        - containerPort: 80
````

---

## 4. Create a Pod (Quick Start)

```bash
kubectl run nginx-pod --image=nginx
```

Check Pod:

```bash
kubectl get pods
kubectl describe pod nginx-pod
```

Delete Pod:

```bash
kubectl delete pod nginx-pod
```

---

## 5. Single vs Multi-Container Pods

### Single-container Pod (most common)

```yaml
spec:
  containers:
    - name: web
      image: myapp:latest
```

### Multi-container Pod (sidecar pattern)

```yaml
spec:
  containers:
    - name: app
      image: myapp
    - name: sidecar
      image: fluentd
```

**All containers share:**

* The same network namespace
* Optionally, volumes

---

## 6. Pod Lifecycle Phases

When you run `kubectl get pods`, you'll see a **STATUS** column with phases:

| Phase     | Description                                  |
| --------- | -------------------------------------------- |
| Pending   | Pod scheduled but containers not running yet |
| Running   | Pod is up and containers are running         |
| Succeeded | Pod completed successfully (Jobs, etc.)      |
| Failed    | Pod crashed or exited with errors            |
| Unknown   | State cannot be determined                   |

---

## 7. Pods Are Ephemeral

Pods are **not self-healing**.

* If a Pod fails or crashes, **it’s gone**.
* This is why you typically use higher-level resources like **ReplicaSet** or **Deployment** to manage Pods.

We’ll explore those in future posts.

---

## 8. Full Pod YAML Example

Here’s a real-world Pod definition you can try:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: demo-pod
  labels:
    app: demo
spec:
  containers:
    - name: web
      image: nginx
      ports:
        - containerPort: 80
```

Apply it:

```bash
kubectl apply -f demo-pod.yaml
```

Check it:

```bash
kubectl get pods
```

---

## 9. Summary

| Topic              | Key Point                                     |
| ------------------ | --------------------------------------------- |
| What is a Pod?     | The smallest unit of deployment in Kubernetes |
| What’s inside?     | Containers, metadata, shared resources        |
| Single vs Multi    | Most Pods have 1 container; some have 2+      |
| Pods are ephemeral | Use Deployments for auto-recovery             |
| How to create      | With `kubectl run` or YAML manifest           |

---

## Final Thoughts

Pods are the **foundation of all workloads** in Kubernetes. Understanding them is critical before diving into more complex resources.