---
ShowToc: true
categories:
- linux
date: 2024-11-11
description: '`passwd` 명령어는 리눅스에서 사용자 계정의 비밀번호를 설정하거나 변경할 때 사용하는 명령어입니다. 특히 시스템 관리자가
  여러 계정의 비밀번호를 설정하거나 정책을 관리할 때 유용합니다. 이번 글에서는 `passwd` 명령어의 다양한 옵션과 실제 사용 예시를 살펴보겠습니다.
  -...'
draft: false
image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
keywords: bash, command line, linux, passwd를, samba, sambaserver, server management,
  setting, shell scripting, smbpasswd, system administration, terminal, unix, 리눅스에서,
  방법, 사용하는
tags:
- linux
- samba
- sambaserver
- setting
- smbpasswd
title: 리눅스에서 passwd를 사용하는 방법
---

# 리눅스에서 `passwd`를 사용하는 방법
`passwd` 명령어는 리눅스에서 사용자 계정의 비밀번호를 설정하거나 변경할 때 사용하는 명령어입니다. 특히 시스템 관리자가 여러 계정의 비밀번호를 설정하거나 정책을 관리할 때 유용합니다. 이번 글에서는 `passwd` 명령어의 다양한 옵션과 실제 사용 예시를 살펴보겠습니다.

## Table of Contents
---
## 1. 기본 사용법
기본적으로 `passwd` 명령어를 입력하면 현재 로그인한 사용자의 비밀번호를 변경할 수 있습니다. `passwd` 명령어만 입력하면 아래와 같은 프롬프트가 나타나며, 새 비밀번호를 입력하라는 요청이 뜹니다.
```bash
passwd
```

---

## 2. 주요 옵션
### 1. 특정 사용자 비밀번호 변경
```bash
passwd [username]
```
관리자(root) 계정에서는 특정 사용자의 비밀번호를 변경할 수 있습니다. 사용자 계정을 지정하지 않으면 현재 사용자의 비밀번호가 변경됩니다.
```bash
sudo passwd roy
```
이 명령어는 `roy`라는 사용자 계정의 비밀번호를 변경합니다.
### 2. 비밀번호 만료일 설정
```bash
sudo passwd -e [username]
```
`-e` 옵션을 사용하면 특정 사용자의 비밀번호를 즉시 만료 처리할 수 있습니다. 이는 다음 로그인 시 사용자에게 비밀번호를 변경하도록 강제하는 데 유용합니다.
```bash
sudo passwd -e roy
```
이 명령어는 `roy`의 비밀번호를 만료시키며, 로그인 시 비밀번호 변경을 요구합니다.
### 3. 계정 잠금
```bash
sudo passwd -l [username]
```
`-l` 옵션은 사용자의 계정을 잠그는 데 사용됩니다. 잠긴 계정은 비밀번호를 올바르게 입력해도 로그인할 수 없습니다. 계정 잠금 시 보안에 민감한 계정을 일시적으로 차단할 수 있습니다.
```bash
sudo passwd -l roy
```
이 명령어는 `roy` 계정의 잠금을 잠급니다.
### 4. 계정 잠금 해제
```bash
sudo passwd -u [username]
```
계정이 잠겨있을 때 `-u` 옵션을로 잠금을 해제할 수 있습니다.
```bash
sudo passwd -u roy
```
이 명령어는 `roy` 계정의 잠금을 해제하여 다시 로그인할 수 있도록 합니다.
### 5. 비밀번호 변경 주기 설정
```bash
sudo passwd -x [최대사용기간(일)] -n [최소사용기간(일)] -w [유예기간(일)]
```
비밀번호의 변경 주기를 설정할 때 `-x` 옵션을 사용하여 최대 사용 기간을 지정할 수 있습니다. 또한 `-n` 옵션은 최소 사용 기간을, `-w` 옵션은 만료 경고 기간을 설정합니다.
- **최대 사용 기간 설정 예시**
```bash
sudo passwd -x 90 roy
```
이 며령어는 `roy`의 비밀번호를 90일 동안 사용할 수 있도록 설정합니다. 90일 후에는 비밀번호가 만료되어 새 비밀번호를 설정해야 합니다.
- **최소 사용 기간 설정 예시**
```bash
sudo passwd -n 10 roy
```
이 명령어는 `roy`가 비밀번호를 변경한 후 최소 10일 동안은 다시 변경할 수 없도록 설정합니다.
- **만료 경고 기간 설정 예시**
```bash
sudo passwd -w 7 roy
```
이 명령어는 비밀번호 만료 7일 전부터 경고 메시지를 표시하여 비밀번호 변경을 유도합니다.
### 6. 비밀번호 없이 로그인 가능 설정
```bash
sudo passwd -d [username]
```
`-d` 옵션은 특정 계정에서 비밀번호를 삭제하여, 비밀번호 없이 로그인할 수 있도록 설정합니다. 다만, 이는 보안에 매우 취약할 수 있으므로 권장되지 않습니다.
```bash
sudo passwd -d roy
```
이 명령어는 `roy`의 비밀번호를 삭제합니다.
### 7. 정보 확인
```bash
sudo passwd -S [username]
```
`-S` 옵션을 사용하면 사용자의 비밀번호 상태 정보를 확인할 수 있습니다. 상태 정보에는 잠금 상태, 만료일 설정, 비밀번호 변경 주기 등이 포함됩니다.
```bash
sudo passwd -S roy
```
이 명령어는 `roy`의 비밀번호 상태 정보를 출력합니다.

---

## 3. `passwd` 옵션 요약

|옵션|설명|사용 예시|
|---|-----|-----|
|[username]|특정 사용자 비밀번호 변경|`sudo passwd roy`|
|`-e`|비밀번호 즉시 만료 처리|`sudo passwd -e roy`|
|`-l`|계정 잠금|`sudo passwd -l roy`|
|`-u`|계정 잠금 해제|`sudo passwd -u roy`|
|`-x`|비밀번호 최대 사용 기간 설정|`sudo passwd -x 90 roy`|
|`-n`|비밀번호 최소 사용 기간 설정|`sudo passwd -n 10 roy`|
|`-w`|만료 경고 기간 설정|`sudo passwd -w 7 roy`|
|`-d`|비밀번호 없이 로그인 가능 설정|`sudo passwd -d roy`|
|`-S`|비밀번호 상태 정보 확인|`sudo passwd -S roy`|

---

## 결론

`passwd` 명령어는 시스템 관리자가 사용자 비밀번호와 보안을 관리하는 데 필수적인 도구입니다. 각 옵션을 적절히 사용하면 사용자 계정에 대한 강력한 보안 설정을 할 수 있습니다.

---