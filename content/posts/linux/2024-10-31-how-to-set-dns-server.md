---
ShowToc: true
categories:
- linux
date: 2024-10-31
description: 리눅스 시스템에서 DNS 서버를 설정할 때, 가장 중요한 설정 파일 중 하나가 바로 `named.conf`입니다. 이 파일은
  BIND (Berkeley Internet Name Domain) DNS 서버의 설정 파일로, 네임 서버의 동작 방식을 정의하는 다양한 옵션을
  포함하고 있습...
draft: false
image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
keywords: BIND, bash, command line, dns, linux, named, named.conf, server management,
  setting, shell scripting, system administration, terminal, unix, 리눅스에서, 방법, 서버,
  설정하는
tags:
- linux
- dns
- setting
- named.conf
- named
- BIND
title: 리눅스에서 DNS 서버 설정하는 방법
---

# 리눅스에서 `named.conf` 설정하기

리눅스 시스템에서 DNS 서버를 설정할 때, 가장 중요한 설정 파일 중 하나가 바로 `named.conf`입니다. 이 파일은 BIND (Berkeley Internet Name Domain) DNS 서버의 설정 파일로, 네임 서버의 동작 방식을 정의하는 다양한 옵션을 포함하고 있습니다. `named.conf` 파일을 설정하는 방법과 주요 설정 요소들을 하나씩 살펴보겠습니다.

## Table of Contents
---
## `named.conf` 파일의 위치

일반적으로 `named.conf` 파일은 아래 위치에 있습니다

- **CentOS/RHEL**: `/etc/named.conf`
- **Ubuntu/Debian**: `/etc/bind/named.conf`

경로는 리눅스 배포판에 따라 다를 수 있으니, `find / -name named.conf` 명령어로 파일 위치를 확인할 수 있습니다.

---

## `named.conf` 파일 구조

`named.conf`는 크게 세 가지 주요 구성 요소로 나눌 수 있습니다:

- **options** : 네임 서버의 기본 옵션을 정의하는 섹션입니다.
- **zone** : 네임 서버가 관리할 도메인에 대한 설정을 정의하는 섹션입니다.
- **include** : 외부 설정 파일을 포함하여, 설정을 더 분할하고 조직화할 수 있습니다.

각 섹션을 하나씩 살펴보겠습니다.

### Options 섹션

`options` 섹션에서는 DNS 서버의 전반적인 설정을 정의합니다. 예를 들어, 포트, 캐시 디렉토리, 쿼리 정책 등을 설정할 수 있습니다.

```conf
options {
    directory "/var/named";                 # 캐시 파일이 저장될 디렉토리
    pid-file "/var/run/named/named.pid";    # PID 파일 위치
    listen-on port 53 { 127.0.0.1; };       # 로컬에서만 쿼리 수신
    allow-query { any; };                   # 쿼리를 허용할 클라이언트 범위
    recursion yes;                          # 재귀적 쿼리 허용 여부
};
```

- **directory** : DNS 캐시 파일이 저장되는 위치를 지정합니다.
- **listen-on** : 특정 IP와 포트에서 쿼리를 수신하도록 설정합니다.
- **allow-query** : 쿼리를 허용할 IP 범위를 지정합니다.
- **recursion** : 재귀적 쿼리 허용 여부를 설정합니다.

### Zone 섹션

`zone` 섹션에서는 DNS 서버가 관리하는 도메인에 대한 정보를 설정합니다. 예를 들어, 도메인 이름과 그에 대한 정보를 포함하는 파일의 경로를 지정할 수 있습니다.

```conf
zone "example.com" {
    type master;
    file "/var/named/example.com.zone";
    allow-update { none; };     # 업데이트를 허용하지 않음
};
```

- `zone` : 관리할 도메인 이름을 지정합니다.
- `type` : DNS 서버의 역할을 지정합니다. (master, slave, forward)
- `file` : 도메인 정보가 포함된 존 파일의 경로를 지정합니다.
- `allow-update` : 해당 도메인에 대한 업데이트 허용 여부를 지정합니다.

#### Slave 서버 설정 예제

Slave 서버는 Master 서버에서 데이터를 복제합니다. 아래와 같이 설정할 수 있습니다.

```conf
zone "example.com" {
    type slave;
    masters { 192.168.1.1; };
    file "/var/named/slave/example.com.zone";
};
```

- `masters` : 마스터 서버의 IP 주소를 지정합니다.

### Include 섹션

`include` 디렉티브를 사용하면 외부 파일을 `named.conf`에 포함시킬 수 있습니다. 이렇게 하면 설정을 더 깔금하게 관리할 수 있습니다.

```conf
include "/etc/named/named.rfc1912.zones";
```

`named.rfc1912.zones`와 같은 파일에는 기본적인 DNS 존 설정이 포함되어 있으며, 필요에 따라 다른 설정 파일을 추가로 포함할 수 있습니다.

---

## 기본 `named.conf` 파일 예제

아래는 간단한 `named.conf` 파일 예제입니다.

```conf
options {
    directory "/var/named";
    listen-on port 53 { any; };
    allow-query { any; };
    recursion yes;
};

zone "." IN {
    type hint;
    file "named.ca";
};

zone "example.com" IN {
    type master;
    file "/var/named/example.com.zone";
};

include "/etc/named.rfc1912.zones";
include "/etc/named.root.key";
```

이 설정은 다음과 같이 동작합니다:

- 모든 IP에서 포트 53으로 쿼리를 수신합니다.
- `example.com`에 대한 마스터 존 파일을 설정합니다.
- 기본 존 설정 파일과 루트 키 파일을 포함합니다.

---

## 설정 파일 테스트 및 재시작

설정 파일을 수정한 후에는 반드시 파일에 오류가 없는지 확인하고, 네임 서버를 재시작해야 합니다.

```bash
# 설정 파일 확인
named-checkconf /etc/named.conf

# 네임 서버 재시작
systemctl restart named
```

---

## 마치며

`named.conf` 파일은 BIND 서버의 핵심 설정 파일로, 올바르게 구성하는 것이 안정적이고 효율적인 DNS 서버 운영에 매우 중요합니다. 필요에 따라 `options`와 `zone` 섹션을 세부적으로 조정하여 네임 서버의 보안성과 성능을 최적화할 수 있습니다. DNS 설정이 익숙해지면 다양한 옵션을 활용하여 더 복잡한 네임 서버 설정을 시도해보세요!