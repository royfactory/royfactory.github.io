---
layout: post

#event information
title:  "리눅스에서 Telnet 서버 설정하는 방법"
cover: "/img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg"
categories: linux
date: 2024-11-04
tags: linux telnet setting

toc: true

#event organiser details
organiser: "Royfactory"


---

# 리눅스에서 Telnet 서버 설정하기

Telnet은 원격 서버에 접속할 수 있는 네트워크 프로토콜입니다. 보안이 필요한 환경에서는 SSH를 사용하지만, 테스트 환경이나 특수한 용도로 여전히 Telnet을 사용하는 경우가 있습니다. 이번 글에서는 리눅스에서 Telnet 서버를 설정하는 방법을 단계별로 설명하겠습니다.

---

## 1. Telnet 서버 설치하기

Telnet 서버를 설정하려면 먼저 패키지를 설치해야 합니다. 다음 명령어를 사용하여 Telnet 서버를 설치할 수 있습니다.

### Debian/Ubuntu 계열

```bash
sudo apt update
sudo apt install -y telnetd
```

### RHEL/CentOS 계열

```bash
sudo yum install -y telnet telnet-server
```

---

## 2. Telnet 서비스 활성화하기

Telnet 서비스가 설치되었으면, 서비스가 실행되도록 설정해야 합니다. CentOS/RHEL 기준으로 설명드리지만, 시스템에 따라 명령어가 다를 수 있습니다.

### 서비스 시작 및 활성화

```bash
sudo systemctl start telnet.socket
sudo systemctl enable telnet.socket
```

### 상태 확인

```bash
sudo systemctl status telnet.socket
```

위 명령어를 통해 Telnet 서비스가 정상적으로 실행 중인지 확인할 수 있습니다.

---

## 3. 방화벽 설정하기

Telnet은 기본적으로 포트 23을 사용합니다. 이 포트가 방화벽에서 열려 있어야 외부에서 접근이 가능합니다. 방화벽 설정을 통해 포트를 열어줍니다.

### 방화벽에서 포트 열기 (Firewalld 사용 시)

```bash
sudo firewall-cmd --permanent --add-port=23/tcp
sudo firewall-cmd --reload
```

이제 Telnet 포트가 열려있으며, 원격지에서 접속할 수 있습니다.

---

## 4. SELinux 설정 확인하기

SELinux가 활성화된 경우 Telnet 서비스가 제약이 있을 수 있습니다. 다음 명령어를 통해 Telnet 사용이 가능하도록 설정할 수 있습니다.

```bash
sudo setsebool -P telnet_disable_trans 1
```

---

## 5. Telnet 서버 보안 설정

Telnet은 암호화되지 않은 텍스트 전송 프로토콜이므로 보안이 취약합니다. 따라서 실제 운영 환경에서는 가능하면 SSH를 사용하는 것이 좋습니다. Telnet을 사용할 경우 다음과 같은 보안 조치를 고려해야 합니다.

- **IP 제한** : `/etc/hosts.allow` 및 `/etc/hosts.deny` 파일을 사용하여 접속을 허용할 IP만 설정합니다.
- **사용자 제한** : Telnet 접근을 허용할 사용자만 선택적으로 설정합니다.

예시로 `/etc/hosts.deny`에 다음과 같이 설정하여 기본적으로 모든 접근을 차단하고 특정 IP만 허용할 수 있습니다.

```plaintext
telnetd: allow
```

그리고 `/etc/hosts.allow`에 허용할 IP를 명시합니다.

```plaintext
telnetd: 192.168.1.00
```

---

## 6. Telnet 서버 테스트

설정이 완료되었으면, 클라이언트 컴퓨터에서 Telnet으로 접속해봅니다. 예시로 로컬에서 접속하려면 다음 명령어를 사용합니다.

```bash
telnet localhost
```

원격지에서 접속하려면 서버의 IP 주소를 사용합니다.

```bash
telnet [서버_IP]
```

---

## 7. Telnet 비활성화하기

Telnet 서비스를 더 이상 사용하지 않는다면 보안을 위해 비활성화하는 것이 좋습니다.

```bash
sudo systemctl stop telnet.socket
sudo systemctl disable telnet.socket
```

---

## 결론

이상으로 리눅스에서 Telnet 서버를 설정하고 관리하는 방법을 알아보았습니다. Telnet은 SSH에 비해 보안이 취약하므로, 운영 환경에서는 SSH를 사용하는 것이 바람직합니다. Telnet은 주로 테스트 용도로 활용되며, 사용 시에는 보안 조치를 꼭 확인하시기 바랍니다.

---



