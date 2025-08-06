---
ShowToc: true
categories: [kubernetes]
date: 2025-08-07
description: Learn how to use Kubernetes CronJob to schedule jobs for automated recurring tasks. This guide covers YAML syntax, concurrency policies, history limits, and common use cases.
draft: false
image: /img/kubernetes-cronjob-guide.jpg
keywords: kubernetes cronjob tutorial, schedule kubernetes jobs, k8s cron schedule, kubernetes batch job, job history limit, concurrency policy, devops automation
layout: post
tags: [kubernetes, k8s, cronjob, schedule, batch-job, devops, cloud-native, automation]
title: 'Kubernetes CronJob Guide: Schedule and Automate Batch Jobs'
slug: kubernetes-cronjob-guide
---

# Kubernetes CronJob Guide: Schedule and Automate Batch Jobs

Kubernetes CronJob allows you to schedule jobs for automated recurring tasks, similar to `crontab` in Linux. Whether it’s daily database backups, hourly log cleanups, or periodic alerts, CronJobs are a powerful way to automate jobs in a Kubernetes cluster.

---

## Table of Contents

{% toc %}

---

## 1. What is a Kubernetes CronJob?

A **CronJob** in Kubernetes is a controller that runs Jobs on a time-based schedule. It uses cron format to define when the job should be created, and handles the job execution just like a normal `Job` resource.

It’s ideal for:
- Scheduled backups
- Log rotation
- Periodic notifications or reporting
- Temporary cleanup operations

---

## 2. Why Use CronJob?

Manual execution of recurring jobs increases the risk of:
- Human error
- Inconsistent timing
- Missed critical operations

Using CronJob automates and standardizes this process, ensuring reliability and repeatability in a scalable cluster environment.

---

## 3. Basic Structure of CronJob

A CronJob consists of:
- `schedule`: When to run the job (in cron format)
- `jobTemplate`: The template used to create a Job
- `concurrencyPolicy`: Behavior if a job is still running at next schedule
- `successfulJobsHistoryLimit`, `failedJobsHistoryLimit`: Cleanup old jobs

---

## 4. CronJob vs Job: Key Differences

| Feature                | Job                   | CronJob                            |
|------------------------|------------------------|-------------------------------------|
| Trigger Type           | Manual or once         | Scheduled and repeating             |
| Use Case               | One-time tasks         | Recurring tasks                     |
| Job History Cleanup    | Manual                 | Automatic via history limit fields  |
| Cron Expression        | Not supported          | Supported                           |

---

## 5. YAML Example

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: hello-cronjob
spec:
  schedule: "0 * * * *" # Every hour
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: hello
            image: busybox
            args:
            - /bin/sh
            - -c
            - date; echo Hello from the Kubernetes CronJob!
          restartPolicy: OnFailure
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 1
  concurrencyPolicy: Forbid
```

---

## 6. Understanding Cron Expressions

Cron format: `minute hour day month weekday`

Examples:
- `0 0 * * *` → Every day at midnight
- `*/10 * * * *` → Every 10 minutes
- `0 9 * * MON` → Every Monday at 9 AM

You can test your cron expressions using tools like crontab.guru.

---

## 7. Job History Limits

Use the following fields to manage job logs and avoid excessive job buildup:

- `successfulJobsHistoryLimit`: Number of successful jobs to keep
- `failedJobsHistoryLimit`: Number of failed jobs to retain

Recommended: Keep a limited history to monitor patterns but avoid clutter.

---

## 8. Concurrency & Restart Policies

**Concurrency Policy**:
- `Allow`: Default. Multiple jobs can run concurrently.
- `Forbid`: Skip new job if the previous one is still running.
- `Replace`: Terminate existing job and replace it.

**Restart Policy**:
- `OnFailure`: Restart container if it fails.
- `Never`: Don’t restart the container.

---

## 9. Real-World Use Cases

- Daily DB snapshots and upload to S3
- Regular system report generation
- Temporary cleanup jobs for old logs or temp files
- Periodic scraping or API pulling

Each of these can be containerized and automated reliably.

---

## 10. Operational Tips

- Ensure timezone awareness (cluster default may be UTC)
- Always specify `restartPolicy`
- Set resource requests/limits to avoid cluster overload
- Monitor logs using `kubectl logs <pod-name>`

---

## 11. FAQ (Answer Engine Optimization)

**Q1: Can a CronJob overlap if the previous job is still running?**  
A: Yes, unless `concurrencyPolicy` is set to `Forbid` or `Replace`.

**Q2: Will changing the schedule delete existing jobs?**  
A: No, but it only affects future job scheduling.

**Q3: Can I run CronJob every second?**  
A: No, minimum resolution is 1 minute.

---

## 12. Summary

| Setting                      | Description                                  |
|-----------------------------|----------------------------------------------|
| `schedule`                  | When to run the job (cron format)            |
| `jobTemplate`               | Pod spec for the actual job                  |
| `concurrencyPolicy`         | Behavior when jobs overlap                   |
| `successfulJobsHistoryLimit`| Cleanup successful job history               |
| `failedJobsHistoryLimit`    | Cleanup failed job history                   |

---

CronJob in Kubernetes enables reliable, automated scheduling of jobs without external tools. Understanding how it works and tuning concurrency or history policies can help maintain a clean, efficient workload management system.
