---
layout: post

#event information
title:  "리눅스에서 TCP Wrapper를 사용하는 방법"
cover: "/img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg"
categories: linux
date: 2024-10-31
tags: tcp wrapper linux hosts.allow hosts.deny

toc: true

#event organiser details
organiser: "Royfactory"


---

# Linux에서 TCP Wrapper란 무엇인가?

TCP Wrapper는 Linux와 Unix 시스템에서 네트워크 서비스 접근을 제어하는 보안 도구입니다. 보통 **inetd(super-server)**와 같은 서비스 관리자가 관리하는 네트워크 서비스의 접근을 제한하기 위해 사용됩니다. TCP Wrapper는 허가된 IP 주소나 호스트 이름을 바탕으로 서비스 접근을 제어할 수 있어, 네트워크 보안의 기본적인 계층을 제공합니다.

---

## TCP Wrapper의 작동 방식

TCP Wrapper는 연결 요청을 감시하고 이를 확인한 후, 접근을 허용하거나 거부하는 방식을 취합니다. 보통 다음과 같은 절차로 동작합니다:

1. **네트워크 요청 감시**: 클라이언트가 서버에 연결 요청을 보낼 때, TCP Wrapper가 이를 먼저 감지합니다.
2. **접근 제어 파일 확인**: `/etc/hosts.allow`와 `/etc/hosts.deny` 파일을 확인하여 클라이언트가 허용된 IP 또는 호스트인지 확인합니다.
3. **허용 또는 거부**: 접근이 허가되면 요청을 서비스로 전달하여 연결이 진행됩니다. 허가되지 않으면 연결이 거부됩니다.

---

## 설정 파일: `/etc/hosts.allow`와 `/etc/hosts.deny`

TCP Wrapper는 두 가지 파일을 통해 접근을 제어합니다:

### `/etc/hosts.allow`

`/etc/hosts.allow` 파일은 특정 서비스와 호스트가 연결을 허용할 수 있도록 설정하는 파일입니다. 파일에 정의된 규칙에 따라, 여기서 허용된 IP나 호스트는 접근이 허용됩니다. 일반적인 설정 예시는 다음과 같습니다:

```plaintext
sshd: 192.168.1.10  # IP 주소 192.168.1.10의 클라이언트가 sshd 서비스에 접근 가능
httpd: .example.com  # example.com 도메인의 모든 클라이언트가 httpd 서비스에 접근
```

### `/etc/hosts.deny`

`/etc/hosts.deny` 파일은 접근을 거부할 호스트를 지정하는 파일입니다. 이 파일은 `/etc/hosts.allow`에 정의되지 않은 나머지 모든 호스트와 IP에 대해 적용됩니다. 예를 들어:

```plaintext
ALL: ALL  # 기본적으로 모든 서비스에 대해 모든 호스트의 접근을 거부
```

이 규칙을 통해 기본적으로 모든 접근을 거부하고, `/etc/hosts.allow`에서 명시적으로 허용된 호스트만 접근할 수 있도록 구성할 수 있습니다.

---

## TCP Wrapper의 장점

TCP Wrapper는 다음과 같은 장점을 제공합니다:

* **접근 제어** : 특정 IP나 호스트 기반으로 네트워크 서비스에 대한 접근을 허용하거나 거부할 수 있습니다.
* **보안 강화** : 기본적인 방화벽 역할을 수행하여 서비스에 대한 무단 접근을 차단할 수 있습니다.
* **로그 기능** : 네트워크 접근을 로그 파일에 기록하여 추후 보안 모니터링과 문제 해결에 활용할 수 있습니다.

---

## 예제: SSH 접근 제어 설정

서버의 SSH 서비스에 대해 특정 IP에서만 접근을 허용하고 싶다면 다음과 같이 설정할 수 있습니다.

1. `/etc/hosts.allow` 파일에서 SSH 서비스에 대한 허용 규칙을 추가합니다:

```plaintext
sshd: 192.168.1.10
```

2. `/etc/hosts.deny` 파일에서 기본적으로 모든 접근을 거부하도록 설정합니다:

```plaintext
sshd: ALL
```

이 설정을 통해 `192.168.1.10` IP를 가진 클라이언트만 SSH 서비스에 접근할 수 있으며, 나머지 모든 IP는 접근이 거부됩니다.

---

## TCP Wrapper 사용 시 고려 사항

* **내부 네트워크 보안 강화** : TCP Wrapper는 방화벽 설정과 함께 사용할 때 보안성을 더욱 높일 수 있습니다.
* **Deprecated 상태** : 최근의 리눅스 시스템에서는 firewalld나 iptables와 같은 고급 방화벽 도구로 접근 제어를 수행하는 경우가 많습니다. TCP Wrapper는 여전히 유효하지만, 일부 배포판에서는 기본적으로 제공되지 않을 수 있습니다.

---

## 결론

TCP Wrapper는 Linux와 Unix 시스템에서 간단한 접근 제어를 제공하는 보안 도구입니다. `/etc/hosts.allow`와 `/etc/hosts.deny` 파일을 통해 서비스에 대한 접근을 쉽게 제한할 수 있으며, 네트워크 보안을 강화할 수 있는 기본적인 방법 중 하나입니다. 다만 최신 방화벽 솔루션의 발전으로 TCP Wrapper의 사용 빈도는 줄어들고 있지만, 여전히 유효한 네트워크 접근 제어 수단으로 활용될 수 있습니다.

---



