---
categories: ["kubernetes"]
date: 2025-07-17
description: Learn the most essential kubectl commands every Kubernetes beginner must know. This guide covers how to get, create, edit, and delete Kubernetes resources — all with real examples and tips.
keywords: kubectl, kubernetes, k8s, basic kubectl commands, kubectl cheatsheet, devops, beginner kubectl, kubectl get, kubectl apply
author: Royfactory
tags: ["kubernetes", "k8s", "kubectl", "cli", "devops", "cloud-native", "beginner", "kubernetes-commands"]
title: 'Basic kubectl Commands: Your First Step to Mastering Kubernetes'
ShowToc: true
draft: false
---

# Basic kubectl Commands: Your First Step to Mastering Kubernetes

If you want to work with Kubernetes, learning `kubectl` is non-negotiable.

`kubectl` is the **command-line tool** that lets you manage and inspect every part of your Kubernetes cluster — from Pods to Nodes, Deployments to Services.

In this post, we’ll walk through **the most important `kubectl` commands** you need to know as a beginner, along with practical examples and real use cases.

--
## Table of Contents

## 1. kubectl Syntax Overview

The basic format of a `kubectl` command is:

```

kubectl \[command] \[resource] \[name] \[flags]

````

| Part     | Description                              |
|----------|------------------------------------------|
| command  | Action to perform (get, describe, apply) |
| resource | Type of object (pod, svc, deployment)    |
| name     | Name of specific object (optional)       |
| flags    | Extra options (e.g. `-n`, `-o`, `--watch`) |

### Example

```bash
kubectl get pods
kubectl describe node my-node
kubectl delete pod nginx-pod
````

---

## 2. Viewing Cluster State

### 1) Check Node Status

```bash
kubectl get nodes
```

Returns a list of nodes in your cluster and their health:

```
NAME        STATUS   ROLES           AGE   VERSION
master      Ready    control-plane   10d   v1.29.0
worker-01   Ready    <none>          10d   v1.29.0
```

---

### 2) List Pods

```bash
kubectl get pods
kubectl get pods -A  # All namespaces
```

---

### 3) List Services

```bash
kubectl get svc
```

Shows Service names, IPs, types (ClusterIP, NodePort, etc.)

---

### 4) List Deployments

```bash
kubectl get deployments
```

Check how many replicas are running and whether updates are complete.

---

## 3. Get Detailed Information

### 1) Describe Resource

```bash
kubectl describe pod my-pod
kubectl describe node my-node
```

This shows detailed info like labels, events, environment variables, and logs.

---

### 2) View Resource YAML

```bash
kubectl get pod my-pod -o yaml
```

See the full manifest as Kubernetes understands it — great for debugging.

---

## 4. Creating Resources

### 1) Apply from YAML File

```bash
kubectl apply -f deployment.yaml
```

Most real-world deployments are done this way — declarative, repeatable.

---

### 2) Create a Pod Manually

```bash
kubectl run nginx --image=nginx
```

Quick way to create a single Pod — good for testing.

---

## 5. Editing Resources

### 1) Edit Live Resource

```bash
kubectl edit deployment my-deploy
```

This opens the resource’s YAML in your default editor (e.g. Vim).

---

### 2) Reapply with New YAML

```bash
kubectl apply -f updated-deployment.yaml
```

Use this to update Deployments, Services, or other resources declaratively.

---

## 6. Deleting Resources

```bash
kubectl delete pod my-pod
kubectl delete -f deployment.yaml
```

Delete by name or from a YAML file.

---

## 7. Real-Time Monitoring

### 1) Watch Resource Changes

```bash
kubectl get pods --watch
```

Live updates as Pods start/stop.

---

### 2) View Logs

```bash
kubectl logs my-pod
```

If your Pod has multiple containers:

```bash
kubectl logs my-pod -c my-container
```

---

## 8. Working with Namespaces

### Get resources in a namespace

```bash
kubectl get pods -n my-namespace
```

### Create a namespace

```bash
kubectl create namespace dev
```

### Set default namespace

```bash
kubectl config set-context --current --namespace=dev
```

---

## 9. Enable Autocomplete (Optional)

```bash
source <(kubectl completion bash)
```

You can also add this to `.bashrc` or `.zshrc`.

---

## 10. kubectl Cheatsheet (Summary)

| Task                  | Command                                                |
| --------------------- | ------------------------------------------------------ |
| Check nodes           | `kubectl get nodes`                                    |
| List pods             | `kubectl get pods`                                     |
| View service          | `kubectl get svc`                                      |
| View YAML             | `kubectl get pod nginx -o yaml`                        |
| Describe resources    | `kubectl describe pod nginx`                           |
| Apply YAML            | `kubectl apply -f file.yaml`                           |
| Edit live resource    | `kubectl edit deployment my-app`                       |
| Delete resource       | `kubectl delete pod nginx`                             |
| Watch for changes     | `kubectl get pods --watch`                             |
| View logs             | `kubectl logs my-pod`                                  |
| Use namespace         | `kubectl get pods -n dev`                              |
| Set default namespace | `kubectl config set-context --current --namespace=dev` |

---

## Final Thoughts

kubectl is the **gateway to mastering Kubernetes**.
Whether you're deploying apps, debugging Pods, or scaling services — it all happens through kubectl.

By learning these basic commands, you’re laying the groundwork for more advanced Kubernetes workflows.