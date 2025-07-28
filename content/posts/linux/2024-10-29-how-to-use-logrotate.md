---
categories: ["linux"]
date: 2024-10-29
description: '`logrotate`는 서버 및 애플리케이션 로그 파일의 용량을 효과적으로 관리하기 위해 사용되는 Linux 유틸리티입니다.
  로그 파일이 일정 크기에 도달하거나 일정 기간이 경과했을 때, `logrotate`를 통해 로그를 자동으로 순환(rotating)하고 필요 시
  압축, 삭제할...'
keywords: bash, command line, linux, log, logging, logrotate, server management, shell
  scripting, system administration, terminal, unix, 관리하는, 로그를, 리눅스에서, 방법
author: Royfactory
tags: ["linux", "logrotate", "logging", "log"]
title: 리눅스에서 로그를 관리하는 방법
ShowToc: true
draft: false
---

# Logrotate: 로그 관리를 위한 자동화 도구

`logrotate`는 서버 및 애플리케이션 로그 파일의 용량을 효과적으로 관리하기 위해 사용되는 Linux 유틸리티입니다. 로그 파일이 일정 크기에 도달하거나 일정 기간이 경과했을 때, `logrotate`를 통해 로그를 자동으로 순환(rotating)하고 필요 시 압축, 삭제할 수 있습니다. 이를 통해 시스템의 로그 저장 공간을 절약하고, 로그 관리에 대한 부담을 줄일 수 있습니다.

--
## Table of Contents

## Logrotate의 기본 원리

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

---

## 주요 설정 옵션

다양한 `logrotate` 옵션을 통해 로그 파일 관리 정책을 세부적으로 조정할 수 있습니다.

|옵션|설명|
|---|-----|
|`daily`|로그 파일을 매일 회전합니다.|
|`weekly`|로그 파일을 매주 회전합니다.|
|`monthly`|로그 파일을 매월 회전합니다.|
|`rotate`|보관할 로그 파일의 개수를 지정합니다.|
|`compress`|회전한 로그 파일을 gzip으로 압축합니다.|
|`delaycompress`|회전 후 다음 회전까지 파일 압축을 지연합니다.|
|`create`|새로운 로그 파일을 생성할 때 권한과 소유자를 설정합니다.|
|`notifempty`|로그 파일이 비어있으면 회전을 수행하지 않습니다.|
|`mail`|지정한 이메일 주소로 로그 파일을 보냅니다.|
|`postrotate`|로그 파일이 회전한 후 실행할 명령어를 지정합니다.|

---

## Logrotate 예제

다음은 Apache 로그 파일에 대해 `logrotate` 설정을 적용한 예제입니다.

```conf
/var/log/apache2/*.log {
    daily           # 매일 회전
    missingok       # 로그 파일이 없어도 오류 발생하지 않음
    rotate          # 7일간 로그 보관
    compress        # 회전 후 로그 파일 압축
    delaycompress   # 회전 후 다음 회전까지 압축 지연
    notifempty      # 로그 파일이 비어있으면 회전하지 않음
    create 0640 www-data www-data # 새 로그 파일 생성 시 권한과 소유자 설정
    postrotate
        /etc/init.d/apache2 reload > /dev/null  # 로그 회전 후 Apache 재시작
    endscript
}
```

위 설정은 Apache 로그 파일을 매일 회전하고, 최근 7개의 로그 파일만 보관하며, 오래된 파일은 압축하도록 합니다. 또한, 새 로그 파일을 생성할 때 www-data 사용자와 그룹 소유자로 설정하며, 로그 파일을 회전한 후 Apache 서버를 재시작합니다.

---

## 결론

`logrotate`는 로그 파일 관리를 자동화하고 저장 공간을 효율적으로 사용하는 데 매우 유용한 도구입니다. `logrotate`를 통해 로그 파일의 크기와 개수를 조절하고, 압축 및 삭제를 자동화할 수 있어 시스템 성능 관리와 로그 보관에 도움이 됩니다.

---



