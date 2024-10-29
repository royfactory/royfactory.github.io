---
layout: post

#event information
title:  "로그 관리를 위한 자동화 도구"
cover: "/img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg"
categories: linux
date:   2024-10-29

toc: true

#event organiser details
organiser: "Royfactory"


---

# Logrotate: 로그 관리를 위한 자동화 도구

`logrotate`는 서버 및 애플리케이션 로그 파일의 용량을 효과적으로 관리하기 위해 사용되는 Linux 유틸리티입니다. 로그 파일이 일정 크기에 도달하거나 일정 기간이 경과했을 때, `logrotate`를 통해 로그를 자동으로 순환(rotating)하고 필요 시 압축, 삭제할 수 있습니다. 이를 통해 시스템의 로그 저장 공간을 절약하고, 로그 관리에 대한 부담을 줄일 수 있습니다.

---

## 1. Logrotate의 기본 원리

`logrotate`는 주기적으로 로그 파일의 상태를 점검하고, 설정 파일에 정의된 규칙에 따라 로그 파일을 순환합니다. 예를 들어, 특정 파일의 크기가 일정 이상이 되면, 새 로그 파일을 생성하고 기존 파일을 백업하거나 삭제하여 로그 파일 크기를 관리합니다. 이를 통해 저장 공간을 효율적으로 사용하고, 오래된 로그 데이터가 불필요하게 쌓이는 것을 방지할 수 있습니다.

### 설치 및 기본 설정

대부분의 Linux 배포판에 기본적으로 `logrotate`가 포함되어 있습니다. `logrotate`가 설치되지 않은 경우 다음과 같이 설치할 수 있습니다:

```bash
# Ubuntu/Debian
sudo apt-get install logrotate

# CentOS/RHEL
sudo yum install logrotate
```

`logrotate`의 기본 설정 파일은 `/etc/logrotate.conf`에 위치하며, 개별 애플리케이션의 설정 파일은 `/etc/logrotate.d/` 디렉터리에 배치할 수 있습니다.

## Logrotate 설정 파일 구조

`logrotate`의 설정 파일은 `global` 설정과 `per-logfile` 설정으로 구분됩니다. `global` 설정은 `/etc/logrotate.conf`에 위치하며, 개별 로그 파일에 대한 세부 설정은 `/etc/logrotate.d/` 내 각 파일에서 정의할 수 있습니다.

### 기본 설정 파일 예제 (/etc/logrotate.conf)

```conf
# 주간 회전
weekly

# 로그 파일을 4회전까지 유지
rotate 4

# 오래된 로그 파일 압축
compress

# 빈 로그 파일은 무시
notifempty

# 로테이션으로 생성되는 로그 파일에 해당 날짜를 "YYYYMMDD"형식으로 덧붙여 저장
dateext

# 소유그룹(webserver)의 소유권자(admin)에게 읽기, 쓰기 권한만 지정 하고 다른 사용자에게 권한 부여 안함
create 0600 admin webserver
```

