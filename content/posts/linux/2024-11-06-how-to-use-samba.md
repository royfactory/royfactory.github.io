---
categories: ["linux"]
date: 2024-11-06
description: 리눅스에서 Samba 서버를 설정하려면, 파일 공유 서비스를 설정하는 방법을 따라야 합니다. Samba를 통해 Windows와
  Linux 간 파일 공유가 가능합니다. 다음은 기본적인 Samba 서버 설정 방법입니다. --- 대부분의 배포판에서 Samba는 패키지 관리자
  통해 설치할...
keywords: bash, command line, linux, samba, sambaserver, server management, setting,
  shell scripting, smbpasswd, system administration, terminal, unix, 리눅스에서, 방법, 서버,
  설정하는
author: Royfactory
tags: ["linux", "samba", "sambaserver", "setting", "smbpasswd"]
title: 리눅스에서 Samba 서버 설정하는 방법
ShowToc: true
draft: false
---

# 리눅스에서 Samba 서버 설정하기

리눅스에서 Samba 서버를 설정하려면, 파일 공유 서비스를 설정하는 방법을 따라야 합니다. Samba를 통해 Windows와 Linux 간 파일 공유가 가능합니다. 다음은 기본적인 Samba 서버 설정 방법입니다.

---
## Table of Contents

## 1. Samba 설치

대부분의 배포판에서 Samba는 패키지 관리자 통해 설치할 수 있습니다.

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install samba

# CentOS/RHEL
sudo yum install samba
```

---

## 2. Samba 구성 파일 편집

Samba의 구성 파일은 /etc/samba/smb.conf에 위치합니다. 파일을 열어 편집합니다.

```bash
sudo nano /etc/samba/smb.conf
```

기본 설정은 다음과 같습니다.

```ini
[global]
   workgroup = WORKGROUP            # Windows와 공유되는 작업 그룹명
   server string = Samba Server
   netbios name = samba             # 서버의 NetBios 이름
   security = user                  # 사용자 인증을 사용하여 보안 강화

[shared]
   path = /path/to/shared/folder   # 공유할 폴더의 경로
   valid users = @sambashare       # 이 그룹에 속한 사용자만 접근 가능
   guest ok = no                   # 게스트 접근 불가
   writable = yes                  # 쓰기 권한 허용
   browsable = yes                 # 탐색 허용
```

---

## 3. 공유 폴더와 권한 설정

공유할 디렉토리를 만들고 해당 디렉토리의 소유자를 Samba 사용자에게 변경합니다.

```bash
sudo mkdir -p /path/to/shared/folder
sudo chown -R root:sambashare /path/to/shared/folder
sudo chmod -R 2770 /path/to/shared/folder
```

---

## 4. Samba 사용자 추가

Samba의 인증을 위한 사용자 계정을 추가합니다. Samba 사용자는 시스템 사용자여야 하므로, 먼저 시스템에 사용자를 추가하고 Samba 전용 패스워드를 설정합니다.

```bash
# 시스템 사용자 추가
sudo adduser 사용자이름
sudo passwd 사용자이름

# Samba 사용자 등록
sudo smbpasswd -a 사용자이름
```

---

## 5. Samba 서비스 시작 및 활성화

Samba 서비스를 시작하고 부팅 시 자동으로 시작되도록 설정합니다.

```bash
# 서비스 시작
sudo systemctl start smbd
sudo systemctl enable smbd
```

---

## 6. 방화벽 설정 (필요 시)

방화벽이 설정되어 있다면 Samba 포트를 열어줘야 합니다.

```bash
# Ubuntu/Debian (UFW 사용 시)
sudo ufw allow Samba

# CentOS/RHEL (firewalld 사용 시)
sudo firewall-cmd --permanent --zone=public --add-service=samba
sudo firewall-cmd --reload
```

---

## 7. Samba 설정 확인

설정이 완료되었으면, Samba 설정을 확인하고 오류가 없는지 검사합니다.

```bash
testparm
```

---

## 8. 클라이언트에서 Samba 접속

이제 Windows 클라이언트 또는 다른 Samba 클라이언트에서 `\\서버IP\shared` 형식으로 접속해 공유 폴더에 접근할 수 있습니다.

---

## 추가 설정

- 파일 공유 권한 관리나 로그 기록 등의 추가 설정이 필요하다면 `/etc/samba/smb.conf` 파일에서 추가 옵션을 설정할 수 있습니다.
- 보안을 강화하기 위해, 필요에 따라 `security` 옵션을 `user`가 아닌 다른 옵션으로 설정하건, `hosts allow`와 `hosts deny` 옵션을 사용해 접근 가능한 IP를 제한할 수 있습니다.

---



