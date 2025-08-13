---
ShowToc: true
title: "리눅스에서 파일 속성 관리하는 방법"
categories:
- linux
date: 2024-11-02
description: 리눅스에서는 파일의 속성을 설정하여 삭제, 수정, 추가 등을 제어할 수 있습니다. 이때 사용하는 명령어가 바로 `lsattr`와
  `chattr`입니다. 이 글에서는 이 두 명령어의 사용법과 주요 옵션에 대해 알아보겠습니다.
draft: false
image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
---

  확인...
  shell scripting, system administration, terminal, unix, 관리하는, 리눅스에서, 방법, 속성을, 파일

---

리눅스에서는 파일의 속성을 설정하여 삭제, 수정, 추가 등을 제어할 수 있습니다. 이때 사용하는 명령어가 바로 `lsattr`와 `chattr`입니다. 이 글에서는 이 두 명령어의 사용법과 주요 옵션에 대해 알아보겠습니다.

---

## Table of Contents
---

## 1. `lsattr` - 파일 속성 확인하기
`lsattr` 명령어는 파일에 설정된 속성을 확인할 때 사용됩니다. 기본적으로 리눅스에서는 파일의 읽기, 쓰기, 실행 권한 외에도 특별한 속성들을 부여할 수 있으며, lsattr 명령어는 이런 속성을 확인할 수 있습니다.

- **사용법**

```bash
lsattr [옵션] [파일/디렉토리]
```

- **주요옵션**

|옵션|내용|
|---|-----|
|`-a`|숨김 파일을 포함하여 모든 파일 속성을 출력합니다.|
|`-d`|디렉토리 자체의 속성을 보여줍니다 (디렉토리 내의 파일 속성은 표시하지 않음).|
|`-R`|하위 디렉토리까지 재귀적으로 속성을 확인합니다.|

- **예제**

```bash
$> lsattr myfile.txt
----i---------e---- myfile.txt
```

이 결과에서 `i` 속성은 파일을 보호하여 삭제 또는 수정이 불가능하게 하는 속성입니다.

---

## 2. `chattr` - 파일 속성 변경하기

`chattr` 명령어는 파일의 속성을 설정하거나 제거할 때 사용됩니다. 예를 들어, 중요한 파일이 실수로 삭제되지 않도록 보호하거나, 파일 내용이 추가되지 않도록 설정할 수 있습니다.

- **사용법**

```bash
chattr [옵션] [속성] [파일/디렉토리]
```

- **주요속성**

|Flag|속성|내용|
|---|---|-----|
|`A`|No atime Update|atime 레코드가 수정되지 않습니다.|
|`a`|Append Only|파일이 추가 모드로만 열리게 되어 내용을 덧붙이기만 할 수 있습니다.|
|`c`|Compressed|파일이 커널에 의해 자동적으로 압축됨<br>파일을 읽을 때는 압축을 해제하여 보여주며, 쓰기 작업 시에는 디스크에 저장하기 전에 압축부터 진행|
|`D`|Synchronous directory updates|디렉토리의 변경 사항이 디스크에 동기식으로 저장됩니다.|
|`d`|No Dump|dump 프로그램을 실행 될 때 해당 파일이 백업되지 않습니다.|
|`E`|Compression error|Experimental compression patch에 사용되며, 압축된 데이터가 오류를 가지고 있음을 의미합니다.|
|`e`|Extent format|파일이 디스크 클록에 매핑될 때 Extents를 사용합니다.|
|`h`|Huge file|파일을 저장할 때 섹터 단위 대신 블록사이즈 단위로 저장합니다.<br>파일이 2TB 이상의 크기를 가지고 있음을 의미합니다.|
|`I`|Indexed directory|디렉터리가 htree(Hashed tree)로 인덱싱 중 임을 의미합니다.|
|`i`|immutable|파일이 불변 상태가 되어 삭제, 수정, 이름 변경 등이 불가능해집니다.|
|`j`|Data Journaling|파일에 데이터를 쓰기 전에 ext3에 journal에 먼저 씀을 의미합니다.|
|`S`|Shnchronous updates|파일의 변경 사항이 디스크에 동기식으로 저장됩니다.|
|`s`|Secure deletion|파일을 제거했을 때 해당 블록은 zeroed되며, 디스크에 쓰여집니다.|
|`T`|Top of directory hierarchy|T 속성이 부여된 디렉토리는 가장 상위 디렉토리로 여겨집니다.|
|`t`|No tail-merging|파일에 Partial black fragmentation이 발새하지 않습니다.(tail-merging이 발생하지 않습니다.)|
|`u`|Undeletable|파일이 삭제되더라도 내용은 저장되어 있으며, 복구가 가능합니다.|
|`X`|Compression raw access|Experimental compression patch에 사용되며, 압축된 파일의 실제 내용을 직접 접근할 수 있음을 의미합니다.|
|`Z`|Compressed dirty file|Experimental compression patch에 사용되며, 압축된 데이터가 손상되었음을 의미합니다.|

- **주요옵션**

|옵션|내용|
|---|-----|
|`+`|속성을 추가할 때 사용합니다.|
|`-`|속성을 제거할 때 사용합니다.|
|`=`|기존 속성을 모두 제거하고 지정한 속성만 설정합니다.|

- **예제**

파일을 삭제 불가 상태로 만들고 싶다면, `i` 속성을 추가할 수 있습니다.

```bash
$> sudo chattr +i myfile.txt
```

이후, `myfile.txt` 파일은 삭제나 수정이 불가능하게 됩니다. 속성을 제거하려면 `-i` 옵션을 사용합니다.

```bash
$> sudo chattr -i myfile.txt
```

## 3. 실전 예제 - `lsattr`와 `chattr` 함께 사용하기

파일을 실수로 삭제하지 않도록 보호하고, 이를 확인하려면 다음과 같이 명령어를 사용할 수 있습니다.

```bash
# 파일 속성 추가
$> sudo chattr +i myfile.txt

# 파일 속성 확인
$> lsattr myfile.txt
----i---------e---- myfile.txt
```

`lsattr` 명령어를 통해 `i` 속성이 적용된 것을 확인할 수 있습니다.

---

## 4. 속성 설정 시 주의사항
- `chattr` 명령어는 일부 파일 시스템에서만 지원됩니다 (예: ext2, ext3, ext4).
- 속성 변경은 파일 소유자 또는 관리자 권한을 가진 사용자만 가능합니다.
- 시스템 파일에 불필요하게 속성을 설정하면 예기치 않은 동작이 발생할 수 있으므로 주의가 필요합니다.

---

## 마무리

`lsattr`와 `chattr` 명령어를 통해 파일 속성을 확인하고 설정하여 보다 안전하게 파일을 관리할 수 있습니다. 특히 중요한 파일에 대해 `i` 속성을 활용하여 실수로 삭제되지 않도록 하는 것이 유용합니다.