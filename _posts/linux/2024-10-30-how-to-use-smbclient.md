---
categories: linux
cover: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
date: 2024-10-30
description: Windows 파일 공유는 많은 회사와 가정에서 사용하는 중요한 기능입니다. 리눅스에서도 윈도우 파일 서버와 쉽게 연동하여
  파일을 관리할 수 있는데, smbclient는 이러한 작업에 유용한 도구입니다. 이 글에서는 리눅스에서 smbclient를 사용하여 SMB 프로토콜을
  통해 파...
image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
keywords: bash, command line, linux, samba, server management, shell scripting, smbclient,
  smbclient를, system administration, terminal, unix, 리눅스에서, 방법, 사용하는
layout: post
organiser: Royfactory
tags: linux smbclient samba
title: 리눅스에서 smbclient를 사용하는 방법
toc: true
---

# 리눅스에서 smbclient를 사용하는 방법

Windows 파일 공유는 많은 회사와 가정에서 사용하는 중요한 기능입니다. 리눅스에서도 윈도우 파일 서버와 쉽게 연동하여 파일을 관리할 수 있는데, smbclient는 이러한 작업에 유용한 도구입니다. 이 글에서는 리눅스에서 smbclient를 사용하여 SMB 프로토콜을 통해 파일 서버에 접근하고 파일을 전송하는 방법을 안내합니다.

--
## Table of Contents

* ToC
{:toc}

---


## smbclient란?

`smbclient`는 SMB/CIFS 프로토콜을 통해 네트워크 상에서 윈도우 파일 서버에 접근할 수 있게 해주는 CLI 기반 클라이언트입니다. SMB는 Server Message Block의 약자로, Microsoft 네트워크에서 널리 사용되는 파일 공유 프로토콜입니다. `smbclient`는 이를 지원하여 리눅스 환경에서도 윈도우와 호환되는 파일 공유를 할 수 있도록 도와줍니다.

---

## smbclient 설치 방법

대부분의 리눅스 배포판에는 기본 패키지 저장소에 `smbclient`가 포함되어 있습니다. 배포판에 따라 다음 명령어로 설치할 수 있습니다.

```bash
# Debian/Ubuntu
sudo apt update
sudo apt install smbclient

# RHEL/CentOS
sudo yum install samba-client

# Fedora
sudo dnf install samba-client
```

설치가 완료되면 터미널에서 `smbclient` 명령을 사용할 수 있습니다.

---

## 기본 명령어 사용법

`smbclient`를 이용해 특정 파일 서버에 연결하려면, 서버 주소와 공유 폴더 이름을 입력해야 합니다. 기본 구문은 다음과 같습니다.

```bash
smbclient //서버주소/공유폴더 -U 사용자이름
```

연결 후에는 비밀번호를 입력하라는 프롬프트가 나타납니다.

### smbclient 명령어의 기본 동작

연결이 성공하면 `smb:`로 시작하는 프롬프트가 표시됩니다. 이 상태에서 다양한 명령어를 사용하여 서버 상의 파일을 관리할 수 있습니다.

### 디렉토리 나열

현재 디렉토리의 파일과 폴더 목록을 확인하려면 다음과 같이 입력합니다.

```bash
smb: \> ls
```

### 파일 다운로드

서버에서 로컬 컴퓨터로 파일을 다운로드하려면 `get` 명령을 사용합니다.

```bash
smb: \> get 파일이름
```

### 파일 업로드

로컬 파일을 서버에 업로드하려면 `put` 명령을 사용합니다.

```bash
smb: \> put 파일이름
```

예를 들어, 로컬에 있는 `upload.txt`파일을 서버에 업로드하려면 다음과 같이 입력합니다.

```bash
smb: \> put upload.txt
```

### 디렉토리 이동

서버에서 디렉토리를 이동하려면 `cd` 명령을 사용할 수 있습니다.

```bash
smb: \> cd 폴더이름
```

예를 들어, `documents` 폴더로 이동하려면 다음과 같이 입력합니다.

```bash
smb: \> cd documents
```

### 파일 삭제

서버 상의 파일을 삭제하려면 `del` 명령을 사용합니다.

```bash
smb: \> del 파일이름
```

예를 들어, `old_file.txt`를 삭제하려면 다음과 같이 입력합니다.

```bash
smb: \> del old_file.txt
```

### 연결 종료

`smbclient` 세션을 종료하려면 `exit`를 입력합니다.

```bash
smb: \> exit
```

---

## 인증 문제 해결하기

연결 시 인증 오류가 발생할 경우, SMB 프로토콜 버전 설정을 변경해보세요. SMB1, SMB2, SMB3 중 일부 서버는 특정 버전만 지원할 수 있습니다. 프로토콜 버전을 지정하여 연결하려면 `-m` 옵션을 사용할 수 있습니다.

예를 들어, SMB2를 사용하려면 다음과 같이 입력합니다.

```bash
smbclient //192.168.1.100/shared -U user -m SMB2
```

---

## 마무리

`smbclient`는 리눅스 환경에서 윈도우 파일 서버와 통신할 수 있는 강력한 도구입니다. 다양한 명령어를 활용하여 파일 다운로드, 업로드, 삭제 등 여러 작업을 수행할 수 있으며, 스크립트를 통해 자동화할 수도 있습니다. `smbclient`를 잘 활용하면 리눅스와 윈도우 간의 파일 공유가 훨씬 수월해집니다.

---
