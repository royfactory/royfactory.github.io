---
categories: ["linux"]
date: 2024-11-06
description: '`rsync`는 Linux에서 파일과 디렉토리를 빠르고 효율적으로 동기화하거나 백업할 수 있는 강력한 명령어입니다. 네트워크를
  통해 원격 서버와 파일을 동기화할 수 있어 서버 관리 및 백업 작업에 자주 사용됩니다. 이 글에서는 `rsync`의 기본 개념과 주요 옵션들을
  알아보겠습니...'
keywords: bash, command line, linux, rsync, rsync를, server management, shell scripting,
  system administration, terminal, unix, 리눅스에서, 방법, 사용하는
author: Royfactory
tags: ["linux", "rsync"]
title: 리눅스에서 rsync를 사용하는 방법
ShowToc: true
draft: false
---

# `rsync`를 사용하는 방법

`rsync`는 Linux에서 파일과 디렉토리를 빠르고 효율적으로 동기화하거나 백업할 수 있는 강력한 명령어입니다. 네트워크를 통해 원격 서버와 파일을 동기화할 수 있어 서버 관리 및 백업 작업에 자주 사용됩니다. 이 글에서는 `rsync`의 기본 개념과 주요 옵션들을 알아보겠습니다.

--
## Table of Contents

## 기본 `rsync` 명령어 형식

`rsync` 명령어는 다음과 같은 기본 형식을 가집니다:

```bash
rsync [옵션] 원본경로 대상경로
```

---

## 주요 옵션 설명

`rsync`의 다양한 옵션들은 동기화 방식을 세밀하게 조정할 수 있도록 도와줍니다. 여기서는 자주 사용하는 옵션들을 설명하겠습니다.

### 1. `-a` : 아카이브 모드 (archive mode)

- **설명** : `-a`는 여러 옵션(`-rlptgoD`)의 조합으로, 디렉토리 구조와 속성을 유지한 채 복사합니다.
- **세부 옵션** :
  - `-r` : 재귀적으로 복사
  - `-l` : 심볼릭 링크 유지
  - `-p` : 권한 유지
  - `-t` : 타임스탬프 유지
  - `-g` : 그룹 유지
  - `-o` : 소유자 유지
  - `-D` : 디바이스 파일과 특수 파일 유지
- **예시** :
```bash
rsync -a /home/user/source/ /home/suer/backup/
```

### 2. `-v` : 자세한 출력 (verbose)

- **설명** : 동기화 작업의 진행 상황을 자세히 출력합니다.
- **예시** :
```bash
rsync -av /home/user/source/ /home/user/backup/
```

### 3. `-z` : 압축 (compress)

- **설명** : 전송 중 데이터를 압축하여 네트워크를 통해 데이터를 빠르게 전송할 수 있습니다.
- **예시** :
```bash
rsync -az /home/user/source/ remote_user@remote_host:/home/remote_user/backup/
```

### 4. `-P` : 진행 상황 표시 (progress)

- **설명** : 복사 진행 상황을 표시하며, 부분적으로 전송된 파일을 유지하여 중단 후 다시 시작할 수 있습니다. `--progress`와 `--partial` 옵션의 결합입니다.
- **예시** :
```bash
rsync -aP /home/user/source/ /remote_user@remote_host:/home/remote_user/backup/
```

### 5. `--delete` : 대상 디렉토리에서 삭제 (delete)

- **설명** : 원본에 없는 파일을 대상에서 삭제하여 두 디렉토리의 파일을 완전히 동기화합니다.
- **주의사항** : 백업 시 실수로 데이터 손실을 방지하려면 신중히 사용해야 합니다.
- **예시** :
```bash
rsync -av --delete /home/user/source/ /home/user/backup/
```

### 6. `--exclude` 및 `--include` : 파일/디렉토리 제외 및 포함
- **설명** : 특정 파일이나 디렉토리를 제외(`--exclude`)하거나 포함(`--include``)하여 복사합니다.
- **예시** :
```bash
rsync -av --exclude='*.tmp' /home/user/source/ /home/user/backup/
```

### 7. `-e` : 원격 쉘 지정 (remote shell)
- **설명** : `-e` 옵션을 통해 SSH와 같은 원격 쉘을 지정하여 보안이 강화된 전송을 수행합니다.
- **예시** :
```bash
rsync -av -e ssh /home/user/source/ remote_user@remote_host:/home/remote_user/backup/
```

### 8. `-u` : 최신 파일만 복사 (update)
- **설명** : 대상에 이미 존재하는 파일보다 최신 파일만 복사합니다.
- **예시** :
```bash
rsync -avu /home/user/source/ /home/user/backup/
```

### 9. `--dry-run` : 실제 전송 없이 테스트 (dry run)
- **설명** : 명령어 실행 전 실제 파일 복사 없이 어떤 파일이 복사될지 미리 확인합니다.
- **예시** :
```bash
rsync -av --dry-run /home/user/source/ /home/user/backup/
```

---

## 사용 예시

### 로컬에서 디렉토리 복사

```bash
rsync -av /home/user/source/ /home/user/backup/
```

### 원격 서버로 파일 전송 (SSH 사용)

```bash
rsync -avz -e ssh /home/user/source/ remote_user@remote_host:/home/remote_user/backup/
```

### 틀정 파일 형식을 제외하고 전송

```bash
rsync -av --exclude='*.log' /home/user/source/ /home/user/backup/
```

### 완전 동기화를 위한 `--delete` 옵션 사용

```bash
rsync -av --delete /home/user/source/ /home/user/backup/
```

---

## 결론

`rsync`는 파일 동기화와 백업에 최적화된 유용한 도구입니다. 옵션을 조합하여 원하는 방식으로 파일을 전송하고 백업할 수 있으며, 네트워크를 통한 원격 전송 시에도 매우 효율적입니다.

---

