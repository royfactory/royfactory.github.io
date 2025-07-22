---
categories: linux
cover: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
date: 2024-10-28
description: RPM(Red Hat Package Manager)은 Red Hat 계열의 리눅스 배포판에서 사용하는 패키지 관리 도구로,
  소프트웨어의 설치, 업그레이드, 제거, 쿼리 등을 쉽게 수행할 수 있습니다. 이 블로그에서는 RPM의 기본 개념부터 설치 및 관리 방법까지 알아보겠습니다.
  -...
image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
keywords: bash, command line, linux, redhat, rpm, server management, shell scripting,
  system administration, terminal, unix, 명령, 및, 옵션
layout: post
organiser: Royfactory
tags: linux rpm redhat
title: RPM 명령 및 옵션
toc: true
---
# RPM 패키지 관리자 소개

## Table of Contents

* TOC
{:toc}

---

RPM(Red Hat Package Manager)은 Red Hat 계열의 리눅스 배포판에서 사용하는 패키지 관리 도구로, 소프트웨어의 설치, 업그레이드, 제거, 쿼리 등을 쉽게 수행할 수 있습니다. 이 블로그에서는 RPM의 기본 개념부터 설치 및 관리 방법까지 알아보겠습니다.

---

### RPM이란?

RPM은 Red Hat을 비롯한 CentOS, Fedora 등 Red Hat 계열의 리눅스 배포판에서 사용되는 패키지 관리 도구입니다. `.rpm` 확장자를 가진 패키지 파일을 사용하여 소프트웨어를 설치하거나 업데이트할 수 있습니다. RPM은 패키지에 대한 의존성 관리, 버전 관리, 파일 무결성 검사 등 다양한 기능을 제공합니다.

---

### RPM의 동작 방식

RPM은 패키지 파일을 기반으로 소프트웨어를 설치합니다. 패키지 파일에는 설치할 파일과 디렉토리, 그리고 소프트웨어의 버전 정보, 의존성 등이 포함되어 있습니다. RPM을 통해 설치된 모든 패키지 정보는 `/var/lib/rpm` 디렉토리에 저장되어 RPM의 데이터베이스에 기록됩니다.

---

### RPM 패키지 설치

RPM을 사용하여 패키지를 설치하려면 터미널에서 다음 명령어를 사용합니다.

```bash
sudo rpm -ivh [패키지 이름].rpm
```

* `-i` : 패키지 설치
* `-v` : 설치 진행 상황을 상세히 출력
* `-h` : 진행 상황을 해시(#)로 표시

예를 들어, `example.rpm` 패키지를 설치하려면 다음과 같이 입력합니다

```bash
sudo rpm -ivh example.rpm
```

---

### RPM 패키지 제거

설치된 패키지를 제거하려면 다음 명령어를 사용합니다.

```bash
sudo rpm -e [패키지 이름]
```

예를 들어, `example`이라는 이름의 패키지를 제거하려면 다음과 같이 입력합니다.

```bash
sudo rpm -e example
```

주의할 점은 패키지 이름은 `.rpm` 확장자 없이 입력해야 한다는 것입니다.

---

### RPM 패키지 정보 확인

설치된 패키지의 정보를 확인하려면 다음 명령어를 사용합니다.

```bash
sudo -qi [패키지 이름]
```

예를 들어, `example` 패키지의 정보를 확인하려면 다음과 같이 입력합니다.

```bash
sudo -qi example
```

이 명령어를 사용하면 패키지 이름, 버전, 설명, 설치 날짜 등 상세한 정보를 확인할 수 있습니다.

또한, 설치된 모든 패키지 리스트를 보고 싶다면 다음 명령어를 입력하세요.

```bash
sudo -qa
```

---

### RPM 패키지 검증 및 문제 해결

RPM은 설치된 패키지의 무결성을 확인하고 파일이 손상되었는지 검증할 수 있습니다.

```bash
rpm -V [패키지 이름]
```

이 명령어를 통해 패키지 파일의 크기, 권한, 해시 등을 검증할 수 있으며, 검증 결과가 변경되었을 경우 이를 알려줍니다.

---

### 결론

RPM은 Red Hat 계열 리눅스 배포판에서 필수적인 패키지 관리 도구입니다. 이 블로그에서 소개한 RPM의 설치, 제거, 정보 확인 및 검증 방법을 통해 리눅스 시스템에서의 패키지 관리를 쉽게 수행할 수 있습니다. RPM을 잘 활용하면 시스템 유지 보수를 효율적으로 할 수 있습니다.

---