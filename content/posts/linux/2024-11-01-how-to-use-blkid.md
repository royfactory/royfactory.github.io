---
categories: ["linux"]
date: 2024-11-01
description: 리눅스 시스템에서 디스크와 파티션을 관리할 때, 특히 마운트 정보를 확인하거나 파티션을 식별하기 위해 UUID나 파일시스템
  타입을 조회하는 경우가 많습니다. 이때 유용하게 사용할 수 있는 명령어 중 하나가 바로 `blkid`입니다. 이번 글에서는 `blkid` 명령어의
  사용법과 옵...
keywords: bash, blkid, blkid를, command line, filesystem, filetype, linux, server management,
  shell scripting, system administration, terminal, unix, uuid, 리눅스에서, 방법, 사용하는
author: Royfactory
tags: ["linux", "blkid", "uuid", "filesystem", "filetype"]
title: 리눅스에서 blkid를 사용하는 방법
ShowToc: true
draft: false
---

# blkid - 리눅스 파일시스템 UUID와 타입 확인 명령어

리눅스 시스템에서 디스크와 파티션을 관리할 때, 특히 마운트 정보를 확인하거나 파티션을 식별하기 위해 UUID나 파일시스템 타입을 조회하는 경우가 많습니다. 이때 유용하게 사용할 수 있는 명령어 중 하나가 바로 `blkid`입니다. 이번 글에서는 `blkid` 명령어의 사용법과 옵션들에 대해 자세히 설명하겠습니다.

--
## Table of Contents

## 1. `blkid`란?

`blkid`는 **블록 디바이스(block device)**의 UUID와 파일시스템 타입을 조회할 수 있는 리눅스 명령어입니다. 이 명령어는 디스크나 파티션에 대한 정보를 제공하며, 주로 시스템 관리자가 파일시스템을 식별하거나 마운트할 때 유용하게 사용됩니다.

`blkid`는 단순히 장치 이름만으로는 알 수 없는 UUID, LABEL(레이블), TYPE(파일시스템 유형) 정보를 보여주기 때문에 디스크 관리와 관련된 작업에서 중요한 도구입니다.

---

## 2. `blkid` 명령어 기본 사용법

기본적으로 `blkid` 명령어를 실행하면 현재 시스템에 연결된 모든 블록 디바이스의 정보를 출력합니다. 다음과 같은 기본 형식을 사용합니다:

```bash
blkid
```

이 명령어를 입력하면 시스템에 있는 모든 블록 장치의 정보를 출력하며, 각 장치의 UUID, 파일시스템 타입(TYPE), 레이블(LABEL) 등을 확인할 수 있습니다.

### 예시

```bash
$ blkid
/dev/sda1: UUID="12345abc-6789-def0-1234-56789abcdef0" TYPE="ext4" PARTUUID="0001"
/dev/sda2: UUID="23456bcd-789a-ef01-2345-6789abcdef01" TYPE="swap" PARTUUID="0002"
```

위의 출력 결과에서 볼 수 있듯이, 각 파티션의 UUID와 파일시스템 타입을 한눈에 확인할 수 있습니다.

---

## 3. `blkid`의 주요 옵션
`blkid` 명령어는 다양한 옵션을 제공하여 원하는 정보를 효율적으로 조회할 수 있습니다. 주요 옵션은 다음과 같습니다:

### 특정 장치 정보 조회
특정 장치에 대한 정보만 확인하고 싶을 때는 장치 경로를 추가하여 실행합니다.

```bash
blkid /dev/sda1
```

### 3.2 캐시 파일 새로 고침 (`-c` 옵션)

일반적으로 `blkid`는 정보를 빠르게 조회하기 위해 캐시를 사용합니다. 하지만 파일시스템이 변경되었거나 새 장치가 연결되었을 때, 최신 정보를 위해 캐시를 무시할 필요가 있습니다. 이 경우, `-c` 옵션을 사용하여 캐시 파일을 새로 고칠 수 있습니다.

```bash
blkid -c /dev/null
```

### 3.3 출력 형식 지정 (`-o` 옵션)

`blkid`의 출력 형식을 지정할 수 있습니다. 기본적으로는 short 형식을 사용하며, export 형식을 지정하면 환경 변수 형식으로 출력됩니다.

```bash
blkid -o export
```

### 3.4 파일시스템 정보 필터링 (`-t` 옵션)

특정 파일시스템 타입이나 UUID에 맞는 장치만 표시하고자 할 때는 `-t` 옵션을 사용할 수 있습니다. 예를 들어 `UUID=12345abc-6789-def0-1234-56789abcdef0`인 장치만 보고 싶다면 다음과 같이 실행합니다:

```bash
blkid -t UUID="12345abc-6789-def0-1234-56789abcdef0"
```

또는 특정 파일시스템 타입, 예를 들어 `ext4` 파일시스템만 보고 싶다면 다음과 같이 사용합니다:

```bash
blkid -t TYPE="ext4"
```

---

## `blkid` 사용 예제

### 4.1 시스템의 모든 블록 장치 UUID 및 파일시스템 타입 확인

```bash
blkid
```

### 특정 장치 `/dev/sdb1`의 정보 확인

```bash
blkid /dev/sdb1
```

### 캐시 무시하고 최신 정보 조회

```bash
blkid -c /dev/null
```

### 4.4 특정 UUID에 맞는 장치 검색

```bash
blkid -t UUID="example-uuid"
```

---

## 5. 마무리

`blkid` 명령어는 리눅스에서 디스크와 파티션을 관리할 때 필수적인 도구입니다. 파일시스템 식별, UUID 관리, 특정 파일시스템 타입 필터링 등 다양한 기능을 제공하므로, 이를 잘 활용하면 시스템 디스크 관리 작업을 더욱 효율적으로 수행할 수 있습니다.

파일시스템 관련 작업에서 실수를 줄이기 위해 언제든지 `blkid` 명령어를 사용해 디바이스 정보를 정확하게 확인하는 습관을 들이시기 바랍니다.

---
