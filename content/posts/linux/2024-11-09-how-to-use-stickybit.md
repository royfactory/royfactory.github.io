---
categories: ["linux"]
cover:
  image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
date: 2024-11-09
description: '리눅스에서 **Sticky Bit**, **SetUID**, **SetGID**는 파일이나 디렉토리에 특수 권한을 설정하여
  특정한 조건에서 사용자 권한을 조정할 수 있는 기능입니다. 각 특수 권한의 사용 방법과 동작 방식은 다음과 같습니다. --- - **설명** :
  Sticky ...'
keywords: SetGID, SetUID, StickyBit, bash, command line, linux, server management,
  shell scripting, system administration, terminal, unix, 리눅스에서, 방법, 부여하는, 특수권한을
author: Royfactory
tags: ["linux", "StickyBit", "SetUID", "SetGID"]
title: 리눅스에서 특수권한을 부여하는 방법
ShowToc: true
draft: false
---

# 리눅스에서 특수권한을 부여하는 방법

리눅스에서 **Sticky Bit**, **SetUID**, **SetGID**는 파일이나 디렉토리에 특수 권한을 설정하여 특정한 조건에서 사용자 권한을 조정할 수 있는 기능입니다. 각 특수 권한의 사용 방법과 동작 방식은 다음과 같습니다.

---
## Table of Contents

## 1. Sticky Bit

- **설명** : Sticky Bit는 주로 **디렉토리**에 설정되어, 해당 디렉토리 내 파일을 소유자나 루트 사용자만 삭제하거나 이름을 변경할 수 있도록 합니다. 공용 디렉토리에서 의도치 않은 파일 삭제를 방지하는 데 유용합니다.
- **사용 방법** : `chmod +t 디렉토리명`
- **예시** : `/tmp` 디렉토리처럼 여러 사용자가 파일을 저장할 수 있는 공용 디렉토리에 Sticky Bit를 설정하면 각 사용자들이 자기 소유의 파일만 삭제하거나 수정할 수 있습니다.
```bash
chmod +t /some_directory
ls -ld /some_directory
# 결과 예시: drwxrwxrwxt ...
```

---

## 2. SetUID (Set User ID)

- **설명** : SetUID는 **파일 소유자의 권한으로 프로그램이 실행되도록** 설정하는 특수 권한입니다. 특정 프로그램을 실행할 때 현재 사용자가 아니라 파일 소유자의 권한으로 실행되기 때문에 주로 루트 권한으로 실행되어야 하는 프로그램에 사용됩니다.
- **사용 방법** : `chmod u+s 파일명`
- **예시** : `/usr/bin/passwd` 명령어는 SetUID가 설정되어 있어 일반 사용자가 실행해도 루트 권한으로 암호를 변경할 수 있습니다.
```bash
chmod u+s /some_program
ls -l /some_program
# 결과 예시: -rwsr-xr-x ...
```

---

## 3. SetGID (Set Group ID)

- **설명** : SetGID는 **파일이나 디렉토리의 그룹 소유자 권한으로 실행되도록** 설정하는 특수 권한입니다. 파일에 SetGID가 설정되면 프로그램이 실행될 때 그룹 권한을 변경할 수 있고, 디렉토리에 SetGID가 설정되면 새로 생성되는 파일이나 하위 디렉토리의 그룹 소유자가 해당 디렉토리의 그룹과 동일하게 설정됩니다.
- **사용 방법** : `chmod g+s 파일명(or 디렉토리명)`
- **예시** : 디렉토리에 SetGID를 설정하여 특정 그룹 소속 사용자들끼리 파일을 공유할 때 파일의 그룹 소유자가 동일하게 유지되도록 설정할 수 있습니다.
```bash
chmod g+s /some_directory
ls -l /some_directory
# 결과 예시: drwxrwsr-x ...
```

---

## 추가 예시: 특수 권한 확인하기

파일이나 디렉토리의 특수 권한은 `ls -l` 명령어로 확인할 수 있습니다. 결과에서 권한 위치는 다음과 같습니다.

- Sticky Bit : 디렉토리 권한의 끝에 `t`로 표시됩니다(예: `drwxrwxrwt`).
- SetUID : 사용자 권한 위치에 `s`로 표시됩니다(예: `-rwsr-xr-x`).
- SetGID : 그룹 권한 위치에 `s`로 표시됩니다(예: `drwxrwsr-x`).

---
