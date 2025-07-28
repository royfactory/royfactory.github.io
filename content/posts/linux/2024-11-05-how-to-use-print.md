---
categories: ["linux"]
date: 2024-11-05
description: '리눅스 환경에서 프린터를 관리하고 설정하는 데 유용한 명령어들을 알아보겠습니다. 리눅스는 다양한 프린터와 호환되며, 터미널
  명령어를 사용하여 프린터를 관리할 수 있습니다. --- 현재 시스템에 연결된 프린터 목록을 확인할 수 있습니다. lpstat -p -d - `-p`
  : 시스템...'
keywords: bash, command line, linux, lp, lpadminn, lpoptions, lpr, lpstat, print,
  server management, shell scripting, system administration, terminal, unix, 리눅스에서,
  방법, 사용하는, 프린트
author: Royfactory
tags: ["linux", "print", "lp", "lpr", "lpstat", "lpadminn", "lpoptions"]
title: 리눅스에서 프린트 사용하는 방법
ShowToc: true
draft: false
---

# 리눅스에서 프린터 관련 명령어 모음

리눅스 환경에서 프린터를 관리하고 설정하는 데 유용한 명령어들을 알아보겠습니다. 리눅스는 다양한 프린터와 호환되며, 터미널 명령어를 사용하여 프린터를 관리할 수 있습니다.

---
## Table of Contents

## 1. 프린터 목록 확인하기

현재 시스템에 연결된 프린터 목록을 확인할 수 있습니다.

```bash
lpstat -p -d
```
- `-p` : 시스템에 설치된 프린터 목록을 출력합니다.
- `-d` : 기본 프린터를 표시합니다.

---

## 2. 프린터 추가하기

프린터를 추가하려면 `lpadmin` 명령어를 사용합니다. 프린터 이름과 드링버 URI를 지정하여 설정할 수 있습니다.

```bash
sudo lpadmin -p 프린터이름 -E -v 프린터_URI -m 드라이버파일
```

- `-p 프린터이름` : 프린터 이름을 지정합니다.
- `-E` : 프린터를 활성화합니다.
- `-v 프린터_URI` : 프린터의 URI를 지정합니다 (예: usb://EPSON/Printer).
- `-m 드라이버파일` : 프린터 드라이버 파일을 지정합니다.

예시 :

```bash
sudo lpadmin -p MyPrinter -E -v usb://EPSON/Printer -m everywhere
```

---

## 3. 기본 프린터 설정하기

여러 프린터가 설치된 경우, 기본 프린터를 설정할 수 있습니다.

```bash
lpoptions -d 프린터이름
```

예시 :

```bash
lpoptions -d MyPrinter
```

---

## 4. 프린터 상태 확인하기

프린터의 상태를 확인하려면 다음 명령어를 사용합니다.

```bash
lpstat -p 프린터이름
```

- '-p 프린터이름` : 특정 프린터의 상태를 확인합니다.

예시 :

```bash
lpstat -p MyPrinter
```

---

## 5. 프린터 작업 목록 확인하기

현재 진행 중이거나 대기 중인 인쇄 작업 목록을 확인할 수 있습니다.

```bash
lpq
```

특정 프린터의 작업 목록을 확인하려면 프린터 이름을 지정합니다.

```bash
lpq -P 프린터이름
```

---

## 6. 인쇄 작업 취소하기

진행 중인 특정 작업을 취소하려면 `cancel` 명령어를 사용합니다. 작업 ID를 입력하여 취소할 수 있습니다.

```bash
cancel 작업ID
```

모든 작업을 취소하려면 `-a` 옵션을 사용할 수 있습니다.

```bash
cancel -a
```

---

## 7. 프린터 삭제하기

더 이상 필요하지 않은 프린터를 삭제할 때는 다음 명령어를 사용합니다.

```bash
sudo lpadmin -x 프린터이름
```

- `-x 프린터이름` : 지정한 이름의 프린터를 삭제합니다.

예시 :

```bash
sudo lpadmin -x MyPrinter
```

---

## 8. 인쇄하기

파일을 프린터로 직접 인쇄할 때는 `lp` 명령어를 사용합니다.

```bash
lp -d 프린터이름 파일명
```

`-d 프린터이름` : 프린터를 지정합니다.

예시 :

```bash
lp -d MyPrinter document.pdf
```

---

##  마무리

리눅스에서 프린터를 관리하는 방법은 매우 직관적이며, 터미널 명령어를 통해 쉽게 설정하고 관리할 수 있습니다. 위 명령어들을 사용하여 프린터 설정, 인쇄 작업, 프린터 상태 확인 등 다양한 기능을 효율적로 활용할 수 있습니다.

---
