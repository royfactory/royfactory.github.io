---
ShowToc: true
categories: [cloud]
date: 2025-09-22
description: "An in-depth guide to Kubernetes Volumes, explaining the core concepts of PersistentVolume (PV), PersistentVolumeClaim (PVC), and StorageClass with practical YAML examples for practitioners."
image: /img/kubernetes-volumes-pv-pvc-storageclass-guide-cover.jpg
draft: false
keywords: "Kubernetes, Volume, PersistentVolume, PV, PersistentVolumeClaim, PVC, StorageClass, Storage"
tags: ["kubernetes", "volume", "pv", "pvc", "storageclass", "storage", "devops"]
title: "Kubernetes Volumes Explained: PV, PVC, and StorageClass"
slug: "kubernetes-volumes-pv-pvc-storageclass-guide"
---

## Introduction
- **TL;DR:** Kubernetes Volumes provide a durable storage solution to solve the ephemeral nature of container filesystems, ensuring data persists even when a Pod restarts. The core of Kubernetes storage is an abstraction layer consisting of three key objects: **PersistentVolume (PV)**, **PersistentVolumeClaim (PVC)**, and **StorageClass**. An administrator defines available storage as a PV, a user requests storage with a PVC, and a StorageClass enables the dynamic, automatic provisioning of PVs to satisfy PVCs, streamlining storage management in cloud environments.

By default, a container's filesystem is **ephemeral**. Any data created inside a container is lost when the container is terminated and restarted. To run stateful applications like databases, it's essential to have a mechanism for persistent storage. **Kubernetes Volumes** address this by decoupling the storage lifecycle from the Pod lifecycle. A Volume is essentially a directory, accessible to the containers in a Pod, whose data can be preserved across container restarts.

## Basic Volume Types: `emptyDir` and `hostPath`
Kubernetes supports several volume types, but two of the most basic are `emptyDir` and `hostPath`.

* **`emptyDir`**: This volume is created when a Pod is assigned to a Node and is initially empty. It exists as long as that Pod is running on that Node. Containers within the same Pod can read and write the same files in the `emptyDir` volume. It's useful for scratch space or sharing temporary files between containers. However, if the Pod is deleted, the data in the `emptyDir` is lost forever.
* **`hostPath`**: This volume mounts a file or directory from the host node's filesystem directly into a Pod. This can be a powerful escape hatch for applications that need access to node-level files but should be used with extreme caution. It creates a tight coupling between the Pod and a specific node and can pose significant security risks.

**Why it matters:** These basic types illustrate the core concepts of shared, Pod-scoped storage (`emptyDir`) and node-level integration (`hostPath`). However, they do not provide the durable, network-attached storage required by most stateful production applications.

## The Persistent Storage Trio: PV, PVC, and StorageClass
For robust and scalable storage management, Kubernetes provides a powerful abstraction layer composed of `PersistentVolume` (PV), `PersistentVolumeClaim` (PVC), and `StorageClass`. This model separates the concerns of infrastructure administration from application development.

| Resource | Role & Responsibility | Primary User | Analogy |
| :--- | :--- | :--- | :--- |
| **`PersistentVolume` (PV)** | An abstraction for a piece of physical storage (e.g., a cloud disk, NFS share). It's a cluster-wide resource. | Cluster Administrator | A hotel room |
| **`PersistentVolumeClaim` (PVC)**| A request for storage made by a user. It specifies the required size and access mode. | Developer / User | A room reservation |
| **`StorageClass`** | A template for creating PVs dynamically. It defines the provisioner and parameters for the underlying storage. | Cluster Administrator | Room type (e.g., Standard, Suite) |

This system allows for **dynamic provisioning**: an administrator defines `StorageClass` objects, and when a user creates a `PVC` requesting a specific class, Kubernetes automatically provisions a `PV` that matches the request and binds them together. The developer never needs to know the details of the underlying storage infrastructure.

**Why it matters:** The PV/PVC/StorageClass model is a cornerstone of cloud-native storage. It enables a declarative, automated approach, allowing developers to consume storage resources on-demand without manual intervention from administrators, perfectly aligning with modern DevOps workflows.

## Practical Example: Using a PVC in a Pod
Here is a complete workflow showing how a user can request storage with a PVC and mount it in a Pod.

**1. Create a PersistentVolumeClaim (PVC)**
This YAML manifest creates a PVC named `my-pvc` that requests 3 GiB of storage with a `ReadWriteOnce` access mode from the `standard` storage class.

```yaml
# pvc-definition.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  storageClassName: standard
  accessModes:
    - ReadWriteOnce # Can be mounted as read-write by a single node
  resources:
    requests:
      storage: 3Gi
````

**2\. Mount the PVC in a Pod** The Pod manifest references the PVC by its name (claimName). The Pod consumes the storage without any knowledge of the underlying PV.

YAML

```
# pod-with-pvc.yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
    - name: web-server
      image: nginx
      volumeMounts:
        - name: my-storage
          mountPath: /usr/share/nginx/html
  volumes:
    - name: my-storage
      persistentVolumeClaim:
        claimName: my-pvc # Reference the PVC created above
```

When these manifests are applied, the StorageClass provisioner creates a suitable PV, which Kubernetes then binds to my-pvc. The my-pod starts, and the persistent volume is mounted into its Nginx container at the specified path.

**Why it matters:** This YAML demonstrates the clean separation of concerns. The application definition (Pod) is completely decoupled from the storage infrastructure. The storage backend could be changed (e.g., from GCP Persistent Disk to AWS EBS) by simply changing the StorageClass definition, with no changes required to the application's manifest.

## Conclusion

Kubernetes Volumes are essential for running stateful applications by providing data persistence. While basic types like emptyDir and hostPath have their uses, the real power lies in the PV, PVC, and StorageClass abstraction. This model enables a scalable, declarative, and automated approach to storage management, which is critical for modern, cloud-native environments.

---

### Summary

-   **Problem:** Container filesystems are ephemeral; data is lost on restart.
-   **Solution:** Kubernetes Volumes decouple storage from the Pod lifecycle.
-   **Persistent Storage Model:**
    -   **PersistentVolume (PV):** Admin-provisioned storage resource in the cluster.
    -   **PersistentVolumeClaim (PVC):** A user's request for storage from a PV.
    -   **StorageClass:** A template for dynamically provisioning PVs to fulfill PVCs.
-   **Benefit:** This model separates infrastructure from application concerns, enabling automated and declarative storage management.

### Recommended Hashtags

#kubernetes #volume #persistentvolume #pv #pvc #storageclass #k8s #storage #devops #statefulapps

### References

1.  Volumes | Kubernetes | 2025-09-22 | [https://kubernetes.io/docs/concepts/storage/volumes/](https://kubernetes.io/docs/concepts/storage/volumes/)
2.  Persistent Volumes | Kubernetes | 2025-09-22 | [https://kubernetes.io/docs/concepts/storage/persistent-volumes/](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
3.  \[Kubernetes\] 스토리지 - PersistentVolume(PV), PersistentVolumeClaim(PVC), StorageClass(SC) | 불곰 | 2025-01-31 | [http://brownbears.tistory.com/679](http://brownbears.tistory.com/679)
4.  Kubernetes의 Persistent Volume과 Persistent Volume Claim | 일단 시작하는 블로그 | 2025-01-25 | [https://hajinnote.tistory.com/146](https://hajinnote.tistory.com/146)
5.  5 Types of Kubernetes Volumes and How to Work with Them | NetApp | 2022-06-12 | [https://www.netapp.com/learn/cvo-blg-5-types-of-kubernetes-volumes-and-how-to-work-with-them/](https://www.netapp.com/learn/cvo-blg-5-types-of-kubernetes-volumes-and-how-to-work-with-them/)