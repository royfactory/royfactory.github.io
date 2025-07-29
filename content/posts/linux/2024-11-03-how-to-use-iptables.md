---
categories: linux
image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
date: 2024-11-03
description: '`iptables`는 Linux의 강력한 방화벽 툴로, 네트워크 트래픽을 제어하는 데 사용됩니다. 각 항목과 설정 방법을
  이해하는 것이 네트워크 보안 및 관리에 필수적입니다.
---
draft: false - **iptables**는 **Netfilter** 프레임워크의 사용자 공간에서
  네트워크 패킷을 ...'
image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
keywords: bash, command line, firewall, iptables-restore, iptables-save, itbales,
  linux, server management, shell scripting, system administration, terminal, unix,
  관리하는, 리눅스에서, 방법, 방화벽을
tags: linux firewall itbales iptables-save iptables-restore
title: 리눅스에서 방화벽을 관리하는 방법
ShowToc: true
draft: false
---
draft: false# 리눅스에서 방화벽을 관리하는 방법 : `iptables`

`iptables`는 Linux의 강력한 방화벽 툴로, 네트워크 트래픽을 제어하는 데 사용됩니다. 각 항목과 설정 방법을 이해하는 것이 네트워크 보안 및 관리에 필수적입니다.

---
draft: false
## Table of Contents
---

## 1. `iptables` 개요

- **iptables**는 **Netfilter** 프레임워크의 사용자 공간에서 네트워크 패킷을 필터링하는 도구입니다.
- **패킷 필터링**을 통해 네트워크 트래픽을 허용, 차단하거나 라우팅할 수 있습니다.

---

## 2. 기본 체인 설명

`iptables`는 기본적으로 **세 가지 체인**을 사용합니다. 각 체인은 특정 조건에서 규칙을 적용합니다.

- **INPUT** : 서버로 들어오는 패킷을 제어합니다.
- **OUTPUT** : 서버에서 나가는 패킷을 제어합니다.
- **FORWARD** : 서버를 경유하는 패킷을 제어합니다 (주로 라우터에서 사용).

---

## 3. `iptables` 기본 명령어

### 3.1 규칙 추가 (`-A` 옵션)

특정 체인에 규칙을 추가합니다.

```bash
sudo iptables -A <체인 이름> -p <프로토콜> -s <소스 IP> -d <목적지 IP> --dport <포트> -j <액션>
```

### 3.2 규칙 목록 조회 (`-L` 옵션)

모든 규칙을 확인할 수 있습니다.

```bash
sudo iptables -L
```

### 3.3 규칙 삭제 (`-D` 옵션)

특정 규칙을 삭제합니다.

```bash
sudo iptables -D <체인 이름> <라인 번호>
```

또는 규칙 조건을 지정해 삭제할 수 있습니다.

```bash
sudo iptables -D <체인 이름> -p <프로토콜> --dport <포트> -j <액션>
```

### 3.4 규칙 초기화 (`-F` 옵션)

모든 규칙을 초기화합니다.

```bash
sudo iptables -F
```

---

## 4. 기본 설정 방법

### 4.1 특정 포트 허용 예시

예를 들어, HTTP(포트 80) 트래픽을 허용하려면 다음과 같이 설정합니다.

```bash
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

### 4.2 특정 IP 차단 예시

특정 IP에서 오는 트래픽을 차단하려면 다음과 같이 설정합니다.

```bash
sudo iptables -A INPUT -s <차단할 IP> -j DROP
```

### 4.3 SSH 접속 허용

SSH(포트 22) 접속을 허용하려면 다음 명령어를 사용합니다.

```bash
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```

### 4.4 기본 정책 설정

기본 정책은 패킷이 어떤 규칙에도 맞지 않는 경우 적용됩니다. 예를 들어, 기본적으로 모든 들어오는 트래픽을 거부하려면:
```
sudo iptables -P INPUT DROP
```

---

## 5. `iptables` 설정 저장 및 복구

`iptables`는 시스템 재부팅 시 설정이 초기화되므로, 설정을 유지하려면 다음 방법을 사용할 수 있습니다.

- 설정 저장:
```bash
sudo iptables-save > /etc/iptables/rules.v4
```

- 설정 복구:
```bash
sudo iptables-restore < /etc/iptables/rules.v4
```

---

## 6. 예시 규칙 구성

### 6.1 기본 정책: 허용 및 차단 규칙 설정

```bash
# 기본 정책 설정
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

# 루프백 인터페이스 허용
sudo iptables -A INPUT -i lo -j ACCEPT

# 기존 연결 및 관련된 트래픽 허용
sudo iptables -A INPUT -m conntract --ctstat ESTABLISHED,RELATED -j ACCEPT

# SSH(22), HTTP(80), HTTPS(443) 포트 허용
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
```

---
draft: false이제 `iptables` 설정과 구성이 완료되었습니다. 네트워크 트래픽을 효과적으로 관리하려면 필요에 따라 규칙을 추가하거나 삭제하고, 기본 정책을 신중하게 설정해야 합니다.

---
