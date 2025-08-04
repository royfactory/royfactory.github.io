---
ShowToc: true
categories: [kubernetes]
date: 2025-08-04
description: Learn what Kubernetes DaemonSet is, when to use it, and how it works. Includes practical examples, use cases, common errors, and differences from Deployment and StatefulSet.
draft: false
image: /img/kubernetes-daemonset-guide.jpg
keywords: kubernetes daemonset guide, what is daemonset, k8s daemonset vs deployment, deploy pods to all nodes, fluentd, node-exporter, cluster-wide monitoring
tags: [kubernetes, k8s, daemonset, pod-distribution, monitoring, logging, cluster-management, cloud-native]
title: 'Kubernetes DaemonSet Guide: Deploy Pods to All Nodes'
---
```

# Kubernetes DaemonSet Guide: Deploy Pods to All Nodes

In this post, we dive deep into **Kubernetes DaemonSet** — a powerful controller that ensures a specific Pod runs on **every node** (or selected nodes) in your cluster.

We’ll explore:

* What a DaemonSet is and why it exists
* Common real-world use cases
* YAML examples and best practices
* Key differences from Deployment and StatefulSet
* Troubleshooting and common pitfalls

---

## Table of Contents

{% toc %}

---

## 1. What Is a DaemonSet?

A **DaemonSet** is a Kubernetes resource that ensures **one Pod runs on every node** in a cluster.

This is especially useful for cluster-wide background processes, like log collectors, system monitors, or GPU agents.

### Real-World Examples

* `fluentd` or `fluentbit` for log collection
* `prometheus-node-exporter` for metrics
* Custom agents for backups, GPU drivers, or node configuration

---

## 2. Why Use a DaemonSet?

If you want the **same Pod to run on all nodes**, a DaemonSet is the go-to solution.

| Use Case            | Description                                       |
| ------------------- | ------------------------------------------------- |
| System monitoring   | Node-level metrics collection (CPU, memory, etc.) |
| Logging             | Collect logs from all containers across nodes     |
| Node-specific setup | GPU drivers, firewall rules, or system agents     |
| DNS caching         | Cluster-wide DNS cache (e.g., `dnsmasq`)          |

Unlike a Deployment, which spreads replicas across the cluster, a DaemonSet guarantees **one Pod per node**, automatically.

---

## 3. Key Features of DaemonSet

| Feature                 | Description                                           |
| ----------------------- | ----------------------------------------------------- |
| One pod per node        | Ensures each node runs one instance of the Pod        |
| Auto-scaling with nodes | Adds/removes Pods as nodes join/leave the cluster     |
| Node targeting          | Use `nodeSelector` or `affinity` to control placement |
| Taint support           | With `tolerations`, you can run Pods on tainted nodes |

> Tip: DaemonSets are ideal for tasks that require full visibility across the cluster.

---

## 4. Basic DaemonSet YAML Example

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: log-agent
  namespace: kube-system
spec:
  selector:
    matchLabels:
      app: log-agent
  template:
    metadata:
      labels:
        app: log-agent
    spec:
      containers:
      - name: log-agent
        image: fluent/fluentd:latest
        resources:
          limits:
            memory: "200Mi"
            cpu: "200m"
```

This YAML deploys a `fluentd` log collector to **every node** in the cluster, under the `kube-system` namespace.

---

## 5. Real-World Use Case Scenarios

### Example 1: Monitoring Agent

```yaml
image: prom/node-exporter
```

* Scrapes system metrics (CPU, disk, network)
* Prometheus scrapes these Pods across nodes

### Example 2: GPU Agent

```yaml
spec:
  nodeSelector:
    hardware: nvidia
```

* Deploys only to GPU-enabled nodes
* Useful for preparing runtime GPU environments

### Example 3: Local Storage Daemon

* Run a Pod that backs up local `/data` directories
* Uses hostPath volume to access node-specific data

---

## 6. DaemonSet vs Deployment vs StatefulSet

| Feature   | DaemonSet            | Deployment               | StatefulSet           |
| --------- | -------------------- | ------------------------ | --------------------- |
| Pod count | 1 per node           | Defined replicas         | Ordered, unique names |
| Targeting | Every node or filter | Any node (no control)    | Ordered Pod startup   |
| Use case  | Monitoring, system   | Web APIs, stateless apps | DBs, Kafka, Redis     |
| Scaling   | Based on node count  | Replica count            | Stateful & persistent |

> Reminder: DaemonSet is **not scalable** in the traditional sense — you scale by adding/removing nodes.

---

## 7. Managing DaemonSets

### Edit a DaemonSet

```bash
kubectl edit daemonset log-agent -n kube-system
```

### Delete a DaemonSet

```bash
kubectl delete daemonset log-agent -n kube-system
```

> Pro tip: Use `kubectl rollout status daemonset/<name>` to check update progress.

---

## 8. Common Errors and Fixes

| Error                 | Cause                         | Fix                                  |
| --------------------- | ----------------------------- | ------------------------------------ |
| `PodUnschedulable`    | Node taint without toleration | Add toleration to Pod spec           |
| `Insufficient memory` | Not enough node resources     | Reduce resource limits or requests   |
| `No matching labels`  | selector mismatch             | Ensure labels and selectors align    |
| No Pods deployed      | nodeSelector too restrictive  | Verify node labels or affinity rules |

---

## 9. FAQ (Answer Engine Optimization)

**Q1. Can I run DaemonSet Pods only on master nodes?**
Yes — use a `nodeSelector` or `tolerations` to target tainted master nodes.

**Q2. Can DaemonSet Pods use persistent volumes?**
Yes, via `hostPath`, `emptyDir`, or even PVCs with node affinity.

**Q3. What happens when a new node is added?**
A new Pod is automatically created on that node by the DaemonSet controller.

---

## 10. Key Takeaways

* A **DaemonSet** ensures **one Pod per node** — ideal for agents and background tasks.
* Supports **node targeting**, **taints**, and dynamic scaling based on nodes.
* Different from Deployment and StatefulSet — focus is on **coverage**, not replicas.

---

## 11. Final Thoughts

DaemonSets are critical for managing **cluster-wide responsibilities**, such as logging, monitoring, and node configuration.

Mastering this resource will help you build more **robust, observable, and manageable Kubernetes clusters**.