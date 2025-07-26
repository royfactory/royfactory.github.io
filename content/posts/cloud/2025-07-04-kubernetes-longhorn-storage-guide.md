---
categories: ["cloud-native"]
cover:
  image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
date: 2025-07-04
description: Learn how to install, use, and monitor Longhorn — an open-source distributed block storage system for Kubernetes. Easy setup with Helm, built-in dashboard access, and Prometheus integration.
keywords: longhorn, kubernetes storage, persistent volume, helm, longhorn monitoring, grafana, prometheus, cloud native, block storage
author: Royfactory
tags: ["cloud-native", "kubernetes", "storage", "longhorn", "helm", "grafana", "prometheus", "persistent-volume"]
title: 'Longhorn Tutorial: Kubernetes Storage Made Simple (Install & Monitor Guide)'
ShowToc: true
draft: false
---

# Longhorn Tutorial: Kubernetes Storage Made Simple (Install & Monitor Guide)

In this guide, we’ll explore **Longhorn**, a lightweight, reliable, and open-source **distributed block storage system** for Kubernetes.

You’ll learn what Longhorn is, how it works, how to install it using Helm, and how to monitor it with Grafana and Prometheus.

--
## Table of Contents

## 1. What is Longhorn?

**Longhorn** turns the local disks of your Kubernetes cluster nodes into **persistent volumes** — making stateful apps like databases possible in Kubernetes.

Think of it this way:

> You run a blog inside a Kubernetes pod. What happens to your blog content when the pod restarts?  
> Without persistent storage, the data is gone.  
> Longhorn ensures that data is stored on disk, replicated, and recoverable — even if nodes go down.

### Key Features

- Easy installation with Helm
- Web UI for managing volumes and nodes
- Built-in snapshot and backup
- Supports high availability with volume replication
- Integrates with Prometheus for monitoring

---

## 2. How to Install Longhorn (with Helm)

We’ll use Helm to install Longhorn on your Kubernetes cluster.

### Step 1: Install Helm (if not installed)

```bash
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
````

### Step 2: Create a Namespace

```bash
kubectl create namespace longhorn-system
```

### Step 3: Add the Longhorn Helm Repository

```bash
helm repo add longhorn https://charts.longhorn.io
helm repo update
```

### Step 4: Install Longhorn

```bash
helm install longhorn longhorn/longhorn --namespace longhorn-system
```

This installs the Longhorn controller, manager, UI, and CRDs.

---

## 3. Access the Longhorn Dashboard

Longhorn comes with a built-in web UI to view and manage volumes.

### Port Forward to Access Locally

```bash
kubectl port-forward -n longhorn-system service/longhorn-frontend 8080:80
```

Then visit:

```
http://localhost:8080
```

Here, you can view your volumes, replicas, disk usage, and even take snapshots and backups.

---

## 4. Monitor Longhorn with Prometheus & Grafana

Longhorn exports metrics to Prometheus and has an official Grafana dashboard.

### Enable Monitoring Support via Helm

You can enable monitoring by setting these values during installation:

```yaml
serviceMonitor:
  enabled: true
defaultSettings:
  telemetryOpt: true
```

If already installed, go to the Longhorn UI > `Settings` and enable telemetry.

### Import Grafana Dashboard

In Grafana, use the official dashboard ID:

* **Grafana Dashboard ID**: `13032`

This dashboard includes disk usage, replica health, volume throughput, and more.

---

## 5. Summary

Longhorn makes persistent storage on Kubernetes clusters easy and reliable. With a simple Helm install, built-in dashboard, and strong monitoring support, it’s ideal for running stateful workloads in production.

### Highlights:

* Lightweight distributed block storage
* Easy to install and scale
* Supports snapshots and backups
* Works with Prometheus and Grafana

---

## Conclusion

Whether you're running databases, message queues, or other stateful apps in Kubernetes, **Longhorn provides a robust and user-friendly storage solution**.

In future posts, we’ll dive deeper into **backup to S3**, **disaster recovery**, and **volume snapshot automation** with Longhorn.
