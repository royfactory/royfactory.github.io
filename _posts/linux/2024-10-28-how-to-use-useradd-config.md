---
layout: post

#event information
title:  "리눅스 사용자 설정 파일"
cover: "/img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg"
categories: linux
date:   2024-10-28

toc: true

#event organiser details
organiser: "Royfactory"


---
# 리눅스 사용자 설정 파일 :

`/etc/default/useradd`
리눅스 시스템에서 `useradd` 명령어를 통해 사용자를 생성할 때 기본적으로 적용되는 설정값을 지정할 수 있는 파일이 바로 `/etc/default/useradd`입니다. 이 파일을 통해 사용자 계정 생성 시 기본 옵션을 설정할 수 있어, 일관성 있고 효율적인 사용자 계정 관리를 할 수 있습니다.

---

## 파일의 역할

`/etc/default/useradd` 파일은 새 사용자 계정을 생성할 때 적용되는 기본 설정값을 정의합니다. 시스템 관리자는 이 파일을 통해 사용자가 생성될 때 적용되는 홈 디렉토리 위치, 만료 기간, 기본 그룹 등을 미리 지정할 수 있습니다.

이 파일에 설정된 값은 `useradd` 명령어를 실행할 때 기본 옵션으로 자동 적용됩니다.

---

## 주요 설정 항목

### 1. GROUP

새로 생성되는 사용자의 기본 그룹 ID(GID)를 지정합니다.

```bash
GROUP=100
```

* 설명 : 기본 그룹 ID를 설정합니다. 만약 이 값을 지정하지 않으면 시스템에서 자동으로 새로운 그룹을 생성합니다.

### 2. HOME

사용자의 홈 디렉토리 루트 경로를 지정합니다. 예를 들어, `/home`으로 설정하면 사용자의 홈 디렉토리는 `/home/사용자이름`으로 생성됩니다.

```bash
HOME=/home
```

### 3. INACTIVE

비밀번호가 만료된 후 계정을 비활성화하기까지의 일수를 설정합니다. -1로 설정하면 비활성화되지 않습니다.

```bash
INACTIVE=-1
```

* 설명 : 비밀번호 만료 후 계정 비활성화까지의 기간을 일수로 지정합니다. 기본값은 -1로, 비활성화되지 않음을 의미합니다.

### 4. EXPIRE

사용자의 계정 만료일을 설정합니다. 날짜 형식은 `YYYY-MM-DD`입니다.

```bash
EXPIRE=2024-12-31
```

* 설명 : 계정의 만료일을 2024년 12월 31일로 설정하며, 특정 날짜 이후 계정이 만료되도록 설정할 수 있습니다. 기본값은 빈 칸으로, 만료일이 없음을 의미합니다.

### 5. SHELL

사용자의 기본 쉘을 설정합니다. 일반적으로 `/bin/bash` 또는 `/bin/sh`가 기본으로 설정됩니다.

```bash
SHELL=/bin/bash
```

* 설명 : 새로 생성된 사용자가 사용할 기본 쉘을 지정합니다.

### 6. SKEL

사용자의 초기 설정 파일을 가져오는 디렉토리를 지정합니다. 기본적으로 `/etc/skel`을 사용합니다.

```bash
SKEL=/etc/skel
```

* 설명 : `/etc/skel` 디렉토리에 있는 파일들은 새로 생성된 사용자의 홈 디렉토리에 복사됩니다. 이를 통해 기본적인 환경 설정 파일(`.bashrc`, `.profile` 등)을 제공할 수 있습니다.

### 7. CREATE_MAIL_SPOOL

사용자 계정을 생성할 때 메일 스풀 파일 생성 여부를 결정합니다. 일반적으로 `yes` 또는 `no`로 설정됩니다.

```bash
CREATE_MAIL_SPOOL=yes
```

* 설명 : `yes`로 설정할 경우, 새 계정 생성 시 `/var/spool/mail/사용자이름` 파일이 생성됩니다.

---

## 설정 예제

다음은 `/etc/default/useradd`의 예제 설정입니다.

```bash
# 기본 그룹 ID 설정
GROUP=100

# 홈 디렉토리 기본 경로 설정 (부모 경로)
HOME=/home

# 비밀번호 만료 후 비활성화 기간 (-1인 경우 체크안함)
INACTIVE=-1

# 계정 만료일 설정 (YYYY-MM-DD, 공란인 경우 만료일 없음)
EXPIRE=

# 기본 쉘 설정
SHELL=/bin/bash

# 초기 파일 디렉토리 설정
SKEL=/etc/skel

# 메일 스풀 생성 여부
CREATE_MAIL_SPOOL=yes
```

---

## 요약

|설정 항목|설명|
|---|-----|
|`GROUP`|기본 그룹 ID 지정|
|`HOME`|홈 디렉토리 기본 경로 설정|
|`INACTIVE`|비밀번호 만료 후 계정 비활성화 일수 설정|
|`EXPIRE`|계정 만료일 설정|
|`SHELL`|기본 쉘 설정|
|`SKEL`|초기 파일 디렉토리 설정|
|`CREATE_MAIL_SPOOL`|메일 스풀 생성 여부 설정|

`/etc/default/useradd` 파일을 통해 기본 설정을 고나리하면, 사용자를 생성할 때 별도의 옵션 없이도 일관된 설정을 적용할 수 있어 시스템 관리가 더욱 효율적입니다.

---