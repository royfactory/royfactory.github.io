---
ShowToc: true
categories: [cloud]
date: 2025-09-23
description: "A deep dive into Kubernetes Ingress for practitioners. Learn its concepts, how it works with controllers like NGINX, and see practical examples for routing external traffic."
image: /img/kubernetes-ingress-deep-dive-cover.jpg
draft: false
keywords: "Kubernetes, Ingress, NGINX, Networking, DevOps"
tags: ["kubernetes", "ingress", "nginx-ingress", "networking", "cloud-native"]
title: "Kubernetes Ingress Explained: A Practical Guide with NGINX"
slug: "kubernetes-ingress-deep-dive-with-nginx-example"
---

## Introduction

**TL;DR:** Kubernetes Ingress is an API object that defines rules for routing external HTTP and HTTPS traffic to services within a cluster. It acts as a Layer 7 load balancer, providing features like URL path and hostname-based routing, SSL/TLS termination, and virtual hosting. To function, an Ingress resource requires an Ingress controller, such as NGINX, Istio, or Traefik. This approach simplifies external traffic management and allows multiple services to be exposed under a single IP address, making it a highly efficient solution.

When running containerized applications in Kubernetes, exposing them to the outside world is a critical step. While `NodePort` and `LoadBalancer` service types offer ways to do this, **Kubernetes Ingress** provides the most powerful and flexible solution for managing external access to HTTP(S) services within the cluster. This guide provides a standard overview for practitioners on what Ingress is, how it works, and how to use it with the popular NGINX Ingress controller.

---

## What is Kubernetes Ingress?

An Ingress is not a service itself, but rather a collection of routing rules that govern how external users access services running inside a Kubernetes cluster. It is an official Kubernetes API object, with the `networking.k8s.io/v1` version being stable since Kubernetes v1.19. It provides a way to configure and manage a Layer 7 (HTTP/S) load balancer.

Key features include:
* **Host and Path-Based Routing:** You can route traffic based on the requested hostname (e.g., `api.example.com`) or the URL path (e.g., `example.com/users`).
* **SSL/TLS Termination:** Ingress can terminate SSL/TLS connections, meaning it handles the decryption of traffic, which then forwards unencrypted requests to internal services.
* **Virtual Hosting:** A single Ingress can be used to route traffic for multiple hostnames to different services, all sharing the same external IP address.

**Why it matters:** Unlike `LoadBalancer` services, which typically provision a dedicated L4 load balancer and a public IP for each service, Ingress allows you to consolidate routing rules for many services into a single entry point. This significantly reduces costs and simplifies network management.

## The Role of the Ingress Controller

Creating an Ingress resource alone does nothing. For the Ingress rules to be enforced, you must have an **Ingress controller** running in your cluster. The Ingress controller is a specialized application (typically a reverse proxy) that watches the Kubernetes API server for new or updated Ingress resources. When it detects a change, it dynamically reconfigures itself to apply the new routing rules.

Popular Ingress controllers include:
* **ingress-nginx:** One of the most widely used and community-supported controllers.
* **Traefik:** A modern reverse proxy known for its simplicity and automatic configuration.
* **Kong:** A powerful controller that integrates API gateway functionality.
* **Cloud-specific controllers:** Such as the AWS Load Balancer Controller or Azure Application Gateway Ingress Controller, which integrate tightly with cloud provider services.

**Why it matters:** The choice of an Ingress controller determines the available feature set, performance, and configuration complexity. It's the "brain" of the operation, translating your declared Ingress rules into actual traffic routing.

## Practical Example: Routing with NGINX Ingress

Let's walk through a common scenario: routing traffic to two different backend services based on the URL path.

### 1. Deploy the NGINX Ingress Controller
First, you need to install the controller in your cluster. The most straightforward way is by applying the official manifest.

```bash
# As of 2025-09-23, v1.9.6 is a recent stable version.
kubectl apply -f [https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.9.6/deploy/static/provider/cloud/deploy.yaml](https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.9.6/deploy/static/provider/cloud/deploy.yaml)
```

This command creates the necessary deployments, services, and RBAC rules in the ingress-nginx namespace. The controller will be exposed via a LoadBalancer service, which provides the single external IP for all your traffic.

### 2\. Deploy Sample Applications

Next, create two distinct services to serve as our routing backends.

```yaml
# sample-apps.yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 5678
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: echo-web
        image: hashicorp/http-echo
        args: ["-text=This is the main website"]
---
# A separate service for an API
apiVersion: v1
kind: Service
metadata:
  name: api-service
spec:
  selector:
    app: api
  ports:
    - port: 80
      targetPort: 5678
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
      - name: echo-api
        image: hashicorp/http-echo
        args: ["-text=This is the API backend"]
```

Apply this file: kubectl apply -f sample-apps.yaml.

### 3\. Create the Ingress Resource

Finally, define the Ingress resource to route traffic. Requests to / will go to web-service, and requests to /api will go to api-service.

```yaml
# example-ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: path-based-routing
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /$2
spec:
  ingressClassName: nginx
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 80
      - path: /api(/|$)(.*)
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 80
```

Apply it with kubectl apply -f example-ingress.yaml. The rewrite-target annotation is crucial for ingress-nginx to properly forward requests to the service's root path.

**Why it matters:** This YAML-based, declarative approach allows you to manage complex L7 routing as code. It's version-controllable, repeatable, and integrates seamlessly into CI/CD pipelines, which is a core tenet of DevOps and Cloud-Native practices.

## The Future: Kubernetes Gateway API

While Ingress is powerful, it has limitations. Many advanced features rely on non-portable, controller-specific annotations, and the single Ingress resource can blur the lines of responsibility between cluster operators and application developers.

To address this, the Kubernetes community has developed the **Gateway API**, a successor to Ingress. It aims to be more expressive, extensible, and role-oriented.

-   **Role-Oriented:** Resources like Gateway (managed by operators) and HTTPRoute (managed by developers) provide a clear separation of concerns.
-   **More Features:** Standardizes features like traffic splitting, header manipulation, and TCP/UDP routing, which required custom annotations in Ingress.
-   **Portable:** Defines a core standard that ensures consistent behavior across different implementations.

**Why it matters:** The Gateway API is the future of Kubernetes networking. While Ingress remains the stable and dominant standard today, practitioners should be aware of the Gateway API as it gains adoption and becomes the recommended approach for new and complex use cases.

## Conclusion

Kubernetes Ingress provides an essential mechanism for managing external L7 traffic in a sophisticated and efficient manner.

-   It centralizes routing rules, enabling multiple services to be exposed under a single IP address.
-   It requires an Ingress controller, like NGINX, to function, which acts as the data plane that enforces the rules.
-   The declarative nature of Ingress resources fits perfectly with modern infrastructure-as-code practices.
-   While the emerging Gateway API is poised to be its successor, Ingress remains a critical, stable, and widely-used tool for any Kubernetes practitioner today.

---

### Summary

-   **Ingress is an API object** for managing external HTTP(S) access to services.
-   **An Ingress Controller** (e.g., NGINX) is required to implement the Ingress rules.
-   Key features include **path/host-based routing, SSL termination, and virtual hosting**.
-   It is more **cost-effective and scalable** than using one LoadBalancer per service.
-   The **Gateway API** is the next-generation successor, offering more standardized features and a role-based design.

### References

1.  Ingress | Kubernetes | 2025-09-23 | [https://kubernetes.io/docs/concepts/services-networking/ingress/](https://kubernetes.io/docs/concepts/services-networking/ingress/)
2.  What is a Kubernetes Ingress controller? | IBM | 2025-07-23 | [https://www.google.com/search?q=https://www.ibm.com/topics/ingress-controller](https://www.google.com/search?q=https://www.ibm.com/topics/ingress-controller)
3.  Kubernetes NodePort vs LoadBalancer vs Ingress? When should I use what? | Medium | 2018-03-11 | [https://medium.com/google-cloud/kubernetes-nodeport-vs-loadbalancer-vs-ingress-when-should-i-use-what-922f010849e0](https://medium.com/google-cloud/kubernetes-nodeport-vs-loadbalancer-vs-ingress-when-should-i-use-what-922f010849e0)
4.  The design of NGINX Ingress Controller | NGINX | 2025-07-31 | [https://docs.nginx.com/nginx-ingress-controller/overview/design/](https://docs.nginx.com/nginx-ingress-controller/overview/design/)
5.  Kubernetes Ingress with NGINX Ingress Controller Example | Spacelift | 2025-09-16 | [https://spacelift.io/blog/kubernetes-ingress](https://spacelift.io/blog/kubernetes-ingress)
6.  Gateway API vs Ingress: The Future of Kubernetes Networking | Kong Inc. | 2024-01-31 | [https://konghq.com/blog/engineering/gateway-api-vs-ingress](https://konghq.com/blog/engineering/gateway-api-vs-ingress)
7.  Deprecated API Migration Guide | Kubernetes | 2025-05-16 | [https://kubernetes.io/docs/reference/using-api/deprecation-guide/](https://kubernetes.io/docs/reference/using-api/deprecation-guide/)