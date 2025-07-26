---
categories: ["linux"]
cover:
  image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
date: 2024-11-10
description: '`nmap`(Network Mapper)은 네트워크의 IP, 포트, 서비스 등을 스캔하여 네트워크 구조를 이해하고 보안 점검을
  할 수 있는 강력한 도구입니다. 다음은 `nmap`의 주요 옵션과 그 사용 예시입니다. --- 1. **기본 스캔** nmap <IP 주소> 기본
  스캔 명...'
keywords: bash, command line, linux, monitoring, network, nmap, nmap으로, server management,
  shell scripting, system administration, terminal, topology, unix, 네트워크, 리눅스에서, 분석하기
author: Royfactory
tags: ["linux", "nmap", "network", "monitoring", "topology"]
title: 리눅스에서 nmap으로 네트워크 분석하기
ShowToc: true
draft: false
---

# 리눅스에서 `nmap`으로 네트워크 분석하기

`nmap`(Network Mapper)은 네트워크의 IP, 포트, 서비스 등을 스캔하여 네트워크 구조를 이해하고 보안 점검을 할 수 있는 강력한 도구입니다. 다음은 `nmap`의 주요 옵션과 그 사용 예시입니다.

---
## Table of Contents

## `nmap` 의 주요 옵션

1. **기본 스캔**
```bash
nmap <IP 주소>
```
기본 스캔 명령어로 지정한 IP에 열려 있는 포트를 확인할 수 있습니다.
2. **`-Sp` (Ping 스캔)** 네트워크 내의 장치 목록을 확인할 때 유용합니다.
```bash
nmap -sP 192.168.1.0/24
```
네트워크 대역 내의 모든 장치에 핑을 보내 응답하는 장치를 리스트업합니다.
3. **`-sS` (SYN 스캔)** 빠르고 흔히 사용되는 포트 스캔 방식으로, 열려 있는 포트를 탐색합니다.
```bash
nmap -sS 192.168.1.1
```
4. **`-O` (OS 탐지)** 대상의 운영 체제를 감지합니다.
```bash
nmap -O 192.168.1.1
```
5. **`-p` (포트 지정)** 특정 포트나 포트 범위만 스캔할 수 있습니다.
```bash
nmap -p 22,80,443 192.168.1.1
```
6. **결과 파일로 저장 (`-oN`, `-oX`, `-oG`)**
  - `oN <파일명>` : 일반 텍스트 형식으로 저장
  - `oX <파일명>` : XML 형식으로 저장
  - `oG <파일명>` : 그레프블(grepable) 형식으로 저장
```bash
nmap -sP 192.168.1.0/24 -oN scan_results.txt
```

---



