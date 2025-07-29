---
categories: linux
image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
date: 2024-11-08
description: '`cpio`는 리눅스에서 파일을 백업하고 복원하거나, 패키징하는 데 사용되는 유틸리티입니다. `cpio`는 주로 파일 아카이브를
  만들거나 해제할 때 사용되며, 특히 `find`나 `ls`와 함께 조합하여 특정 파일을 대상으로 작업할 때 유용합니다. 다음은 `cpio`의 기본
  사용법...'
keywords: backup, bash, command line, cpio, linux, restore, server management, shell
  scripting, system administration, terminal, unix, 리눅스에서, 방법, 백업하고, 복원하는, 파일을
tags: linux cpio backup restore
title: 리눅스에서 파일을 백업하고 복원하는 방법
ShowToc: true
draft: false
---
# 리눅스에서 파일을 백업하고 복원하는 방법

`cpio`는 리눅스에서 파일을 백업하고 복원하거나, 패키징하는 데 사용되는 유틸리티입니다. `cpio`는 주로 파일 아카이브를 만들거나 해제할 때 사용되며, 특히 `find`나 `ls`와 함께 조합하여 특정 파일을 대상으로 작업할 때 유용합니다. 다음은 `cpio`의 기본 사용법과 주요 옵션들에 대한 설명입니다.

## Table of Contents
---
## 기본 사용법

`cpio`는 세 가지 모드로 작동합니다.

- **복사 아웃 모드 (Copy-out mode)** : 파일을 아카이브로 만들 때 사용합니다.
  - `cipo -o` 또는 `cpio --create`
- **복사 인 모드 (Copy-in mode)** : 아카이브에서 파일을 추출할 때 사용합니다.
  - `cpio -i` 또는 `cpio --extract`
- **복사 패스 모드 (Copy-pass mode)** : 파일을 디렉토리 간에 복사할 때 사용합니다.
  - `cpio -p` 또는 `cpio --pass-through`

---

## 주요 옵션

- **`-o` / `--create` (아카이브 생성)**
  - 파일 목록을 입력받아 아카이브 파일을 생성합니다.
  - 예시: `find . -name "*.txt" | cpio -o > archive.cpio
    - 현재 디렉토리에서 모든 `.txt` 파일을 찾아 `archive.cpio`라는 아카이브를 만듭니다.
- **`-i` / `--extract` (아카이브 추출)**
  - 아카이브 파일에서 파일을 추출합니다.
  - 예시: `cpio -i < archive.cpio`
    - `archive.cpio` 아카이브에서 모든 파일을 추출합니다.
  - **추가 옵션**
    - `-d` : 파일을 복원할 때 디렉토리도 함께 생성합니다.
    - `-v` : 진행 상황을 자세히 출력합니다.
    - `--no-absolute-filenames` : 절대 경로를 무시하고 상대 경로로 추출합니다.
- **`-p` / `--pass-through` (디렉토리 복사)**
  - 특정 디렉토리에서 다른 디렉토리로 파일을 복사할 때 사용됩니다.
  - 예시 : `find . -name "*.txt" | cpio -pvd /destination_directory`
    - 현재 디렉토리에서 `.txt` 파일을 찾아 `/destination_directory`로 복사합니다.
  - **추가 옵션**
    - `-d` : 필요한 디렉토리를 자동으로 만듭니다.
    - `-v` : 진행 상황을 자세히 출력합니다.
- **기타 유용한 옵션**
  - `-t` 또는 `--list` : 아카이브의 파일 목록을 출력합니다.
    - 예시 : `cpio -t < archive.cpio` 
  - `-u` 또는 `--unconditional` : 파일을 덮어씌울 때 묻지 않고 덮어씌웁니다.
  - `-c` : 아카이브를 Portable ASCII 포맷으로 생성합니다.
  - `--verbose` : 작업을 진행할 때 각 파일 이름을 출력합니다.

---

## 예제 사용법

- **아카이브 생성 및 추출**

```bash
# .txt 파일을 아카이브로 만듦
find /path/to/files -name "*.txt" | cpio -o > files.cpio

# 아카이브에서 파일 추출
cpio -i < files.cpio
```

- **디렉토리 복사**

```bash
find . -name "*.conf" | cpio -pvd /backup/configs
```

`cpio`는 주로 `tar`와 함께 사용되지만, 특정 파일을 대상으로 백업이나 복원할 때는 유용한 도구입니다.
