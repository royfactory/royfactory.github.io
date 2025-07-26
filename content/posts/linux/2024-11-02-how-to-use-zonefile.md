---
categories: ["linux"]
cover:
  image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
date: 2024-11-02
description: 리눅스 서버에서 DNS 서버를 설정할 때, **zone 파일**은 도메인의 각종 정보(IP 주소, 도메인 정보 등)를 정의하는
  중요한 파일입니다. 이 글에서는 zone 파일의 설정 방법과 각 항목의 의미에 대해 자세히 설명하겠습니다. --- 리눅스에서 DNS 서버는 보통
  **BIN...
keywords: BIND, bash, command line, dns, dnsserver, linux, server management, setting,
  shell scripting, system administration, terminal, unix, zone, 리눅스에서, 방법, 사용되는, 서버에,
  작성하는, 파일
author: Royfactory
tags: ["linux", "dnsserver", "dns", "zone", "setting", "BIND"]
title: 리눅스에서 DNS 서버에 사용되는 Zone 파일 작성하는 방법
ShowToc: true
draft: false
---

# 리눅스에서 DNS Zone 파일 설정 방법

리눅스 서버에서 DNS 서버를 설정할 때, **zone 파일**은 도메인의 각종 정보(IP 주소, 도메인 정보 등)를 정의하는 중요한 파일입니다. 이 글에서는 zone 파일의 설정 방법과 각 항목의 의미에 대해 자세히 설명하겠습니다.

---
## Table of Contents

## 1. Zone 파일의 위치와 기본 형식

리눅스에서 DNS 서버는 보통 **BIND**를 사용하여 구성됩니다. BIND의 zone 파일은 보통 `/etc/bind/` 디렉토리에 위치하며, 각 도메인에 대한 정보를 담고 있습니다. 예시로 `/etc/bind/db.example.com`에 작성된 zone 파일을 살펴보겠습니다.

```plaintext
$TTL 86400
@       IN  SOA ns1.example.com. admin.example.com. (
                2023102501 ; Serial
                3600       ; Refresh
                1800       ; Retry
                604800     ; Expire
                86400      ; Minimum TTL
                )
        IN  NS  ns1.example.com.
        IN  NS  ns2.example.com.
        IN  MX  10 mail.example.com.
@       IN  A   192.0.2.1
www     IN  A   192.0.2.1
mail    IN  A   192.0.2.2
```

---

## 2. Zone 파일 항목 설명

각 항목이 어떤 의미를 가지는지 하나씩 살펴보겠습니다.

### $TTL

- `$TTL`은 Time To Live의 약자로, 각 레코드의 기본 유효시간을 초 단위로 설정합니다.
- 예: `TTL 86400`는 24시간 동안 캐시됨을 의미합니다.

### SOA

- SOA는 해당 도메인에 대한 권한을 가지고 있는 DNS 서버와 관리자 정보를 정의합니다.
- `@`는 현재 도메인 (`example.com`)을 의미합니다.
- `ns1.example.com.` : 권한을 가진 기본 네임서버입니다.
- `admin.example.com.` : 관리자의 이메일 주소로, `@` 기호 대신 `.` 을 사용합니다.

#### SOA 필드 설명

- **Serial** : zone 파일이 변경될 때마다 증가시키는 숫자입니다. 일반적으로 `YYYYMMDDNN` 형식으로 작성됩니다.
- **Refresh** : Secondary 서버가 Primary 서버에서 데이터를 다시 가져오는 주기를 초 단위로 설정합니다.
- **Retry** : Secondary 서버가 데이터 전송 실패 시 재시도하는 주기를 초 단위로 설정합니다.
- **Expire** : Secondary 서버가 Primary 서버에 연결할 수 없을 때 zone 파일의 유효 기간을 초 단위로 설정합니다.
- **Minimum TTL** : Negative caching(없는 레코드에 대한 캐싱)의 기본 TTL을 설정합니다.

### NS (Name Server)

- `NS` 레코드는 해당 도메인의 네임서버를 지정합니다.
- `IN NS ns1.example.com.` : 네임서버로 `ns1.example.com`을 지정합니다. 추가적으로 여러 개의 네임서버를 설정할 수 있습니다.

### MX (Mail Exchange)

- `MX` 레코드는 해당 도메인의 메일 서버를 지정하며, 우선 순위를 함께 설정할 수 있습니다.
- `IN MX mail.example.com.` : `example.com` 의 메일 서버로 `mail.example.com`을 지정하며, `10`은 우선 순위를 나타냅니다. 낮은 숫자일수록 우선 순위가 높습니다.

### A (Address)

- `A` 레코드는 호스트 이름에 대응하는 IPv4 주소를 설정합니다.
- `@ IN A 192.0.2.1` : `example.com` 도메인의 기본 주소를 `192.0.2.1`로 설정합니다.
- `www IN A 192.0.2.1` : `www.example.com`의 주소를 `192.0.2.1`로 설정합니다.
- `mail IN A 192.0.2.2` : `mail.example.com`의 주소로 `192.0.2.2`로 설정합니다.

---

## 3. Zone 파일 설정 적용하기

zone 파일을 수정한 후 BIND 서버를 재시작하거나 zone 파일을 리로드하여 설정을 적용합니다.

```bash
# BIND 서버 재시작
sudo systemctl restart bind9

# BINd 서버 리로드 (zone 파일만 새로고침)
sudo rndc reload
```

설정이 적용된 후에는 DNS 서버가 zone 파일을 내용을 기반으로 요청을 처리하게 됩니다.

---

## 4. Zone 파일 설정 확인하기

zone 파일이 제대로 설정되었는지 확인하기 위해 `named-checkzone` 명령을 사용할 수 있습니다.

```bash
# 예시: example.com zone 파일 확인
sudo named-checkzone example.com /etc/bind/db.example.com
```

문법 오류가 있는 경우 해당 명령을 통해 오류를 발견하고 수정할 수 있습니다.

---

## 결론

이 글에서는 리눅스에서 DNS 서버를 설정할 때 중요한 역할을 하는 zone 파일의 설정 방법과 각 항목의 의미에 대해 알아보았습니다. zone 파일은 도메인의 DNS 정보를 관리하는 핵심 파일이므로, 설정 시 정확한 구성이 필요합니다. 이를 통해 DNS 서버가 제대로 작동하도록 설정할 수 있습니다.

---
