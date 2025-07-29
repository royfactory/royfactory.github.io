---
ShowToc: true
categories:
- kubernetes
date: 2025-07-22
description: Learn how to pass configuration and sensitive data to Kubernetes Pods
  using ConfigMaps and Secrets. This guide explains the differences, YAML examples,
  and best practices for secure information management.
draft: false
image: /img/kubernetes-pod-configmap-secret.jpg
keywords: kubernetes configmap, kubernetes secret, pass data to pods, pod environment
  variables, kubectl create configmap, kubectl create secret, k8s configuration, devops
tags:
- kubernetes
- k8s
- configmap
- secret
- pod
- environment
- devops
- cloud-native
- beginner
title: 'Kubernetes ConfigMap and Secret: How to Pass Data to Pods'
---

# Kubernetes ConfigMap and Secret: How to Pass Data to Pods

**Question:** *“How do I pass environment variables or sensitive data to a Kubernetes Pod?”*

Hardcoding configuration values or secrets inside container images is a **bad practice**. It complicates updates, poses security risks, and reduces flexibility.

Kubernetes solves this problem with **ConfigMaps** and **Secrets**, which allow you to manage application configuration and sensitive data securely.

## Table of Contents
---
## 1. What Is a ConfigMap?

A **ConfigMap** stores non-sensitive configuration data as key-value pairs.

**Key benefits:**
- Separate configuration from container images
- Pass data as environment variables or files
- Change settings without rebuilding images

### Create a ConfigMap

Using CLI:

```bash
kubectl create configmap app-config \
  --from-literal=APP_MODE=production \
  --from-literal=DB_HOST=db-service
````

Or define it in YAML:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_MODE: "production"
  DB_HOST: "db-service"
```

---

## 2. What Is a Secret?

A **Secret** is designed to store **sensitive data** like passwords, tokens, and API keys.

**Differences from ConfigMap:**

* Data is **Base64 encoded**.
* Can be encrypted in `etcd` for additional security.
* Access is restricted using Kubernetes RBAC (Role-Based Access Control).

### Create a Secret

Using CLI:

```bash
kubectl create secret generic db-secret \
  --from-literal=DB_USER=admin \
  --from-literal=DB_PASS=securepass
```

Or define it in YAML:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  DB_USER: YWRtaW4=         # base64 for 'admin'
  DB_PASS: c2VjdXJlcGFzcw== # base64 for 'securepass'
```

---

## 3. How to Pass ConfigMap/Secret to a Pod

### 1) Pass as Environment Variables

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: env-pod
spec:
  containers:
    - name: app
      image: nginx
      env:
        - name: APP_MODE
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: APP_MODE
        - name: DB_USER
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: DB_USER
```

---

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: file-pod
spec:
  containers:
    - name: app
      image: nginx
      volumeMounts:
        - name: config-volume
          mountPath: /etc/config
  volumes:
    - name: config-volume
      configMap:
        name: app-config
```

The `/etc/config` directory inside the container will contain files for each key in the ConfigMap.

---

## 4. ConfigMap vs Secret

| Feature        | ConfigMap          | Secret                            |
| -------------- | ------------------ | --------------------------------- |
| Data type      | Non-sensitive data | Sensitive data (e.g., password)   |
| Storage format | Plain text         | Base64 encoded                    |
| Use cases      | App configuration  | Credentials, tokens, certificates |
| Security       | Low                | High (with RBAC and encryption)   |

---

## 5. Best Practices for ConfigMap and Secret

* Always use **Secrets for sensitive information** like passwords or tokens.
* Avoid storing secrets in Git repositories.
* Use **Helm** or **Kustomize** to template ConfigMaps/Secrets for different environments.
* Rotate and update secrets regularly for improved security.

---

## 6. FAQ (Answer Engine Optimization)

**Q1. Can I use ConfigMap and Secret together?**
A. Yes, you can use ConfigMap for general settings and Secret for sensitive data in the same Pod.

**Q2. Are Secrets really secure if they’re just Base64 encoded?**
A. Base64 is not encryption. Use `etcd` encryption and RBAC to control access to Secrets.

**Q3. Do Pods automatically reload when ConfigMaps or Secrets change?**
A. Not by default. You need to redeploy or use tools like `Reloader` or perform a rolling update.

---

## 7. Key Takeaways

| Concept      | Summary                                |
| ------------ | -------------------------------------- |
| ConfigMap    | Stores non-sensitive configuration     |
| Secret       | Stores sensitive data                  |
| Usage        | Pass as environment variables or files |
| Security Tip | Use RBAC and encryption for Secrets    |

---

## Final Thoughts

ConfigMaps and Secrets are **essential tools** for managing configuration and sensitive data in Kubernetes.
They provide flexibility, security, and help separate application code from environment-specific settings.