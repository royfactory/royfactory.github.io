---
layout: post

#event information
title:  "리눅스에서 VSFTP 서버를 설정하는 방법"
cover: "/img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg"
categories: linux
date:   2024-10-30

toc: true

#event organiser details
organiser: "Royfactory"


---

# 리눅스에서 VSFTP 서버를 설정하는 방법

VSFTP(Very Secure FTP)는 빠르고 안전한 FTP 서버 프로그램으로, Linux에서 손쉽게 설정할 수 있습니다. 이 글에서는 Linux 환경에서 VSFTP 서버를 설치하고 설정하는 방법을 다룹니다.

---

## VSFTP 서버 설치

먼저, 터미널에서 VSFTP를 설치합니다.

```bash
sudo apt update
sudo apt install vsftpd
```

설치가 완료되면 VSFTP 서버가 자동으로 시작됩니다.

---

## VSFTP 서비스 상태 확인

설치 후 서버가 정상 작동하는지 확인합니다.

```bash
sudo systemctl status vsftpd
```

정상 작동 중이라면 `active (running)` 상태로 표시됩니다.

---

## 기본 설정 파일 수정

VSFTP의 기본 설정 파일은 `/etc/vsftpd.conf`입니다. 이 파일을 편집하여 기본적인 FTP 서버 설정을 변경할 수 있습니다.

```bash
sudo nano /etc/vsftpd.conf
```

### 주요 설정 항목

#### 익명 접속 비활성화

보안을 위해 익명 접속을 비활성화 합니다.

```plaintext
anonymous_enable=NO
```

#### 로컬 사용자 허용

로컬 사용자의 FTP 접속을 허용하려면 다음 옵션을 활성화합니다.

```plaintext
local_enable=YES
```

#### 쓰기 권한 부여

로컬 사용자에게 파일을 업로드하거나 수정할 수 있는 권한을 부여합니다.

```plaintext
write_enable=YES
```

#### chroot 활성화

사용자가 자신의 홈 디렉토리 외부로 이동하지 못하도록 제한할 수 있습니다.

```plaintext
chroot_local_user=YES
```

---

## 사용자 전용 FTP 디렉토리 설정

보안 및 관리 용이성을 위해 FTP 전용 디렉토리를 만들고 설정하는 것이 좋습니다. 예를 들어 `ftpuser`라는 사용자를 생성하여 전용 디렉토리를 할당할 수 있습니다.

```bash
sudo adduser ftpuser
sudo mkdir -p /home/ftpuser/ftp/upload
sudo chown nobody:nogroup /home/ftpuser/ftp
sudo chown ftpuser:ftpuser /home/ftpuser/ftp/upload
```

* `ftp` 폴더는 읽기 전용, `upload` 폴더는 업로드 전용으로 설정됩니다.

### vsftpd.conf 설정 파일에 사용자 정의 추가

```plaintext
user_sub_token=$USER
local_root=/home/$USER/ftp
```

---

## 방화벽 설정

FTP 기본 포트(21번)를 방화벽에서 허용해줍니다.

```bash
sudo ufw allow 21/tcp
sudo ufw reload
```

---

## VSFTP 서비스 재시작

설정이 완료되었으면 VSFTP 서비스를 재시작하여 변경 사항을 반영합니다.

```bash
sudo systemctl restart vsftpd
```

---

## FTP 서버 테스트

FTP 클라이언트를 사용하여 서버에 접속해보세요. 로컬 네트워크에서 다음과 같이 접속할 수 있습니다.

```bash
ftp localhost
```

사용자명과 비밀번호를 입력하여 로그인합니다. 업로드 및 다운로드가 정상적으로 이루어지는지 확인하세요.

---
