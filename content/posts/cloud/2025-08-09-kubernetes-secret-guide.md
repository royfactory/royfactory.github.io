---
ShowToc: true
categories: \[kubernetes]
date: 2025-08-09
description: Learn how to securely store and manage sensitive data like passwords, API keys, and TLS certificates in Kubernetes using Secrets. Includes examples, best practices, and FAQs.
draft: false
image: /img/kubernetes-secret-guide.jpg
keywords: kubernetes secret, k8s secret, kubernetes store passwords, kubernetes API keys, kubernetes TLS, kubernetes security, sealed secrets
tags: \[kubernetes, k8s, secret, security, vault, rbac, cloudnative, devops, sealedsecrets]
title: 'Kubernetes Secret Guide: Securely Store and Manage Sensitive Data'
slug: kubernetes-secret-guide
-----------------------------

# Kubernetes Secret Guide: Securely Store and Manage Sensitive Data

Kubernetes Secrets allow you to **store sensitive information** such as passwords, API keys, and certificates securely, separate from your application code. In this guide, we’ll cover what Secrets are, how to create and inject them into Pods, and essential security best practices.

---

## Table of Contents

{% toc %}

---

## 1. What Is a Secret?

A Secret is a Kubernetes resource that **stores sensitive data in an encoded or encrypted form**.

* Separate from ConfigMaps for better security
* Base64-encoded values, with optional encryption at rest (etcd)
* Can be injected as **environment variables** or **mounted as files**

---

## 2. Common Use Cases

* Database credentials
* API authentication tokens
* SSH keys and TLS certificates

---

## 3. Creating a Secret

**Method 1: kubectl CLI**

```bash
kubectl create secret generic my-secret \
  --from-literal=username=admin \
  --from-literal=password=1234
```

**Method 2: YAML manifest**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
  namespace: default
type: Opaque
data:
  username: YWRtaW4=
  password: MTIzNA==
```

> Note: `data` values must be base64-encoded.

---

## 4. Injecting Secrets into Pods

**As Environment Variables:**

```yaml
env:
- name: USERNAME
  valueFrom:
    secretKeyRef:
      name: my-secret
      key: username
```

**As Mounted Volumes:**

```yaml
volumes:
- name: secret-volume
  secret:
    secretName: my-secret

volumeMounts:
- name: secret-volume
  mountPath: "/etc/secrets"
  readOnly: true
```

---

## 5. Secret Types

| Type                           | Description                       |
| ------------------------------ | --------------------------------- |
| Opaque                         | Default key-value pairs           |
| kubernetes.io/dockerconfigjson | Docker registry authentication    |
| kubernetes.io/tls              | TLS certificates and private keys |

---

## 6. Security Best Practices

* **Enable etcd encryption** for true data-at-rest security
* **Use RBAC** to limit Secret access to only necessary service accounts
* **Rotate Secrets regularly** using tools like Vault, Sealed Secrets, or External Secrets

---

## 7. Managing Secrets

```bash
kubectl get secrets
kubectl describe secret my-secret
kubectl delete secret my-secret
```

---

## 8. FAQ (Answer Engine Optimization)

**Q1:** Are Secrets encrypted by default?
**A:** No, they are only base64-encoded. Enable etcd encryption for real encryption.

**Q2:** How are Secrets different from ConfigMaps?
**A:** Secrets are for sensitive data with stricter security measures.

**Q3:** Can I manually decode a Secret?
**A:** Yes, base64 decoding will reveal its plain text.

**Q4:** Can multiple Pods share the same Secret?
**A:** Yes, within the same namespace.

---

## 9. Summary Table

| Feature  | Details                                     |
| -------- | ------------------------------------------- |
| Purpose  | Secure storage of sensitive data            |
| Delivery | Env variables or mounted volumes            |
| Security | Optional encryption, RBAC, rotation tools   |
| Types    | Opaque, TLS, Docker registry authentication |

---

**✅ Recommended Slug:** `/kubernetes-secret-guide`
**✅ Recommended Hashtags:** `#kubernetes #k8s #secret #security #vault #rbac #cloudnative #devops #sealedsecrets`
