---
categories: ["linux"]
cover:
  image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
date: 2024-11-07
description: Linux에서 네트워크 보안을 위해 자주 사용되는 방화벽 서비스 중 하나가 **firewalld**입니다. `firewalld`는
  동적 방화벽 관리 도구로, 실시간으로 방화벽 설정을 적용할 수 있으며 iptables의 대체 도구로 많이 사용됩니다. 이번 포스팅에서는 `firewal...
keywords: bash, command line, firewall, firewalld, linux, server management, shell
  scripting, system administration, terminal, unix, 리눅스에서, 방법, 사용하는
author: Royfactory
tags: ["linux", "firewalld", "firewall"]
title: 리눅스에서 firewalld 사용하는 방법
ShowToc: true
draft: false
---

# Firewalld 이해 및 사용법 가이드

Linux에서 네트워크 보안을 위해 자주 사용되는 방화벽 서비스 중 하나가 **firewalld**입니다. `firewalld`는 동적 방화벽 관리 도구로, 실시간으로 방화벽 설정을 적용할 수 있으며 iptables의 대체 도구로 많이 사용됩니다. 이번 포스팅에서는 `firewalld`의 기본 개념, 주요 기능, 설치 방법, 사용법 등에 대해 알아보겠습니다.

--
## Table of Contents

## 1. Firewalld란?

**firewalld**는 Linux에서 방화벽 설정을 관리하기 위한 유틸리티로, iptables와는 다르게 동적이며 더 유연한 설정 변경을 지원합니다. `firewalld`를 사용하면 네트워크 영역(zone)별로 접근 정책을 정의하고 관리할 수 있습니다.

### 주요 특징
- **영역(Zones)**: 트래픽 유형에 따라 네트워크를 여러 영역으로 분리하여 설정할 수 있습니다.
- **서비스 기반 규칙**: 포트나 프로토콜을 직접 지정하는 대신 서비스 기반으로 규칙을 설정할 수 있습니다.
- **동적 변경**: 방화벽 규칙을 재시작 없이 실시간으로 적용할 수 있습니다.
- **D-Bus 인터페이스**: 다른 애플리케이션에서 `firewalld` 설정을 제어할 수 있도록 D-Bus 인터페이스를 제공합니다.

---

## 2. Firewalld 설치

`firewalld`는 대부분의 Linux 배포판에 기본적으로 설치되어 있습니다. 설치가 필요한 경우 아래 명령어로 설치할 수 있습니다.

```bash
# CentOS/RHEL
sudo yum install firewalld

# Ubuntu/Debian
sudo apt-get install firewalld
```

설치 후 `firewalld` 서비스를 시작하고, 부팅 시 자동으로 시작되도록 설정할 수 있습니다.

```bash
sudo systemctl start firewalld
sudo systemctl enable firewalld
```

---

## 3. Firewalld 기본 사용법

### 서비스 상태 확인

`firewalld`의 현재 상태를 확인하는 명령어는 다음과 같습니다.

```bash
sudo firewall-cmd --state
```

`running`으로 출력되면 `firewalld`가 정상적으로 실행 중인 것입니다.

### 영역(Zones) 관리

`firewalld`에서는 네트워크를 **영역(zone)**으로 구분하여 트래픽을 제어할 수 있습니다. 기본적으로 제공되는 영역은 다음과 같습니다.

- **public** : 외부 네트워크에 노출된 영역. 기본적으로 신뢰할 수 없는 네트워크.
- **work** : 사무실과 같이 신뢰할 수 있는 네트워크.
- **home** : 가정용 네트워크로 신뢰할 수 있는 네트워크.
- **internal** : 매우 신뢰할 수 있는 네트워크.
- **dmz** : 최소한의 접근만 허용하는 비무장지대(DMZ).

### 활성화된 영역 확인

현재 설정된 기본 영역과 활성화된 영역을 확인할 수 있습니다.

```bash
sudo firewall-cmd --get-default-zone
sudo firewall-cmd --get-active-zones
```

### 서비스 추가 및 제거

특정 포트나 서비스를 허용하거나 제거하는 방법입니다. 예를 들어, HTTP 서비스를 `public` 영역에서 허용하려면 아래와 같이 실행합니다.

```bash
# 서비스 허용
sudo firewall-cmd --zone=public --add-service=http --permanent

# 서비스 제거
sudo firewall-cmd --zone=public --remove-service=http --permanent
```

- `--permanent` 옵션을 사용하면 방화벽 규칙이 영구적으로 적용됩니다. 옵션을 생략하면 일시적으롬나 적용됩니다.

변경 사항을 적용하려면 다음 명령어를 실행합니다.

```bash
sudo firewall-cmd --reload
```

### 포트 추가 및 제거

특정 포트를 허용하거나 제거할 수도 있습니다. 예를 들어, `8080` 포트를 허용하려면 다음과 같이 실행합니다.

```bash
# 포트 허용
sudo firewall-cmd --zone=public --add-port=8080/tcp --permanent

# 포트 제거
sudo firewall-cmd --zone=public --remove-port=8080/tcp --permanent
```

### 방화벽 규칙 확인

현재 설정된 방화벽 규칙을 확인하려면 다음 명령어를 사용합니다.

```bash
sudo firewall-cmd --list-all
```

이 명령어를 사용하면 설정된 영역, 허용된 서비스, 포트 등을 한눈에 확인할 수 있습니다.

---

## 4. 방화벽 규칙 예시

아래는 몇 가지 방화벽 규칙 예시입니다.

### HTTP/HPPTS 허용

```bash
sudo firewall-cmd --zone=public --add-service=http --permanent
sudo firewall-cmd --zone=public --add-service=https --permanent
sudo firewall-cmd --reload
```

### SSH 포트 변경 및 허용

만약 SSH 포트를 기본 22에서 2222로 변경했다면 다음과 같이 허용할 수 있습니다.

```bash
sudo firewall-cmd --zone=public --add-port=2222/tcp --permanent
sudo firewall-cmd --reload
```

---

## 5. Firewalld 비활성화 및 재설정

firewalld를 일시적으로 비활성화하고 싶을 때는 다음 명령어를 사용할 수 있습니다.

```bash
# 비활성화
sudo systemctl stop firewalld

# 영구 비활성화
sudo systemctl disable firewalld
```

규칙을 초기화하고 싶다면 `--complete-reload` 옵션을 사용할 수 있습니다.

```bash
sudo firewall-cmd --complete-reload
```

---

## 결론

`firewalld`는 Linux에서 방화벽을 유연하고 간편하게 관리할 수 있게 해주는 도구입니다. 네트워크 보안은 시스템 운영에서 매우 중요한 부분이므로 `firewalld`의 기본 사용법을 이해하고 이를 적용하는 것이 중요합니다.

---



