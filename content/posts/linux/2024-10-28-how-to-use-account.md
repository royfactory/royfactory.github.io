---
categories: linux
image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
date: 2024-10-28
description: 리눅스에서는 사용자를 생성, 수정 및 삭제하는 다양한 명령어를 제공합니다. 그 중 가장 기본이 되는 `useradd`, `usermod`,
  `userdel` 명령어에 대해 알아보겠습니다.
---
draft: false `useradd` 명령어는 새로운 사용자를 생성할 때 사용합니다. 사용자의 홈 디렉토리...
image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
keywords: account, bash, command line, linux, server management, shell scripting,
  system administration, terminal, unix, useradd, userdel, usermod, 관리, 리눅스, 사용자
tags: linux account useradd usermod userdel
title: 리눅스 사용자 관리
ShowToc: true
draft: false
---
# 사용자 관리 명령어
리눅스에서는 사용자를 생성, 수정 및 삭제하는 다양한 명령어를 제공합니다. 그 중 가장 기본이 되는 `useradd`, `usermod`, `userdel` 명령어에 대해 알아보겠습니다.

---
draft: false
## Table of Contents
---

## useradd - 사용자 생성

`useradd` 명령어는 새로운 사용자를 생성할 때 사용합니다. 사용자의 홈 디렉토리, UID, 기본 쉘 등을 설정할 수 있습니다.

### 기본 사용법
```bash
useradd [옵션] 사용자이름
```

### 주요 옵션
* `-d [경로]` : 홈 디렉토리 경로를 지정합니다. 기본값은 `/home/사용자이름` 입니다.
* `-m` : 홈 디렉토리를 생성합니다. 홈 디렉토리 경로를 지정하지 않으면 `/home/사용자이름`에 생성됩니다.
* `-s [쉘]` : 기본 쉘을 지정합니다. 기본값은 `/bin/bash`입니다.
* `-u [UID]` : 사용자 ID를 지정합니다. UID는 고유해야 합니다.
* `-g [그룹]` : 기본 그룹을 지정합니다.

### 예제
```bash
# 기본 설정으로 사용자 생성
useradd user1

# 홈 디렉토리를 `/home/user1`으로 생성하고 기본 쉘을 `/bin/bash`로 설정
useradd -m -s /bin/bash user1
```

---

## usermod - 사용자 수정

`usermod` 명령어는 기존 사용자의 정보를 수정할 때 사용합니다.

### 기본 사용법
```bash
usermod [옵션] 사용자이름
```

### 주요 옵션
* `-d [경로]` : 홈 디렉토리 경로를 변경합니다. `-m` 옵션과 함께 사용하면 홈 디렉토리 내의 파일도 이동됩니다.
* `-s [쉘]` : 기본 쉘을 변경합니다.
* `-u [UID]` : 사용자 ID를 변경합니다.
* `-g [그룹]` : 기본 그룹을 변경합니다.
* `-G [그룹1,그룹2,...]` : 추가 그룹을 변경합니다.
* `-aG [그룹]` : 사용자를 추가 그룹에 추가합니다. (`-G`와 달리 기존 그룹을 유지하고 추가합니다.)

### 예제
```bash
# 사용자의 홈 디렉토리 경로를 `/home/newhome`으로 변경하고 파일도 이동
usermod -d /home/newhome -m user1

# 사용자의 기볼 쉘을 `/bin/zsh`로 지정
usermod -s /bin/zsh user1

# 사용자 user1에게 그룹 `sudo`를 추가
usermod -aG sudo user1
```

---

## userdel - 사용자 삭제

`userdel` 명령어는 사용자를 삭제할 때 사용합니다.

### 기본 사용법
```bash
userdel [옵션] 사용자이름
```

### 주요 옵션
* `-r` : 사용자의 홈 디렉토리 및 메일 스풀도 삭제합니다.

### 예제
```bash
# 사용자 user1 삭제
userdel user1

# 사용자 user1과 해당 홈 디렉토리 및 메일 스풀 삭제
userdel -r user1
```

---

## 요약

|명령어|기능|
|---|-----|
|`useradd`|새로운 사용자 생성|
|`usermod`|기존 사용자 정보 수정|
|`userdel`|사용자 삭제|

각 명령어의 옵션을 적절히 활용하면 사용자 계정 관리가 훨씬 수월해집니다.
