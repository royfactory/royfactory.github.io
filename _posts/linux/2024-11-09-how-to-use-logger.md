---
layout: post

#event information
title:  "리눅스에서 로그에 메시지를 기록하는 방법"
cover: "/img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg"
categories: linux
date: 2024-11-09
tags: linux quota usrquota grpquota quotacheck quotaon equota repquota quotaoff warnquota

toc: true

#event organiser details
organiser: "Royfactory"

---

# 리눅스에서 로그에 메시지를 기록하는 방법

`logger`는 Linux 및 Unix 시스템에서 시스템 로그에 메시지를 기록하는 명령입니다. 이 명령은 스크립트나 명령의 출력을 syslog에 남길 때 유용합니다. `logger`를 사용하면 /var/log/에 저장된 다양한 로그 파일에 메시지를 기록할 수 있으며, 로그의 우선순위, 태그 등을 지정할 수도 있습니다.

---

## 기본 사용법

```bash
logger [OPTIONS] "로그메시지"
```

---

## 주요 옵션

- `-p`, `--priority <priority>` : 로그의 우선순위를 지정합니다. 우선순위는 `facility.priority` 형식으로 지정하며, 기본값은 `user.notice`입니다.
  - **facility** : 로그가 기록될 시스템의 로그 카테고리입니다. 예 : `auth`, `cron`, `daemon`, `kern`, `local0~local7`, `user`, `syslog` 등
  - **priority** : 로그의 중요도를 나타냅니다. 예 : `emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`
```bash
logger -p local0.info "이것은 info 레벨의 메시지입니다."
```
- `-t`, `--tag <tag>` : 로그 메시지에 태그를 추가합니다. 태그는 보통 로그 메시지의 출처를 나타내기 위해 사용됩니다.
```bash
logger -t MyScript "태그가 포함된 메시지입니다."
```
- `-i` : 프로세스 ID(PID)를 로그 메시지와 함께 기록합니다. 로그를 작성한 프로세스 ID가 포함되므로 문제 해결에 유용합니다.
```bash
logger -i "PID를 포함한 메시지이빈다."
```
- `-f`, `--file <file>` : 로그 메시지를 파일에서 읽어옵니다. 파일의 내용을 그대로 로그로 기록합니다.
```bash
logger -f /path/to/messagefile
```
- `-s` : 표준 오류(stderr)로도 메시지를 출력합니다. 이 옵션은 스크립트 작성 시 유용하며, 화면에 메시지를 동시에 출력하고 로그에도 기록하고자 할 때 사용됩니다.
```bash
logger -s "표준 오류에도 출력되는 메시지입니다."
```
- `-n`, `--server <server>` : 원격 syslog 서버에 로그를 보냅니다. 서버의 IP 주소나 호스트 이름을 지정하여 원격 시스템에 로그를 기록할 수 있습니다.
```bash
logger -n 192.168.1.100 "원격 서버에 전송되는 메시지입니다."
```
- `-P`, `--port <port>` : 원격 syslog 서버의 포트를 지정합니다. 기본 포트는 514입니다.
```bash
logger -n 192.168.1.100 -P 514 "원격 서버와 특정 포트로 전송되는 메시지입니다.
```

---

## 예제

1. **기본 메시지 기록**
```bash
logger "Hello, World!"
```
2. **우선순위와 태그를 지정하여 기록**
```bash
logger -p user.err -t myscript "오류가 발생했습니다."
```
3. **파일 내용을 로그로 기록**
```bash
logger -f /var/log/myfile.log
```
4. **PID와 함께 메시지 기록**
```bash
logger -i "프로세스 ID와 함께 기록되는 메시지입니다."
```

이렇게 `logger`를 활용하면 다양한 형태의 로그 메시지를 시스템에 기록할 수 있어 관리 및 모니터링에 유용합니다.

---
