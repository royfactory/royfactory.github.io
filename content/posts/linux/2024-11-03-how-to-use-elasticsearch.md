---
ShowToc: true
categories:
- linux
date: 2024-11-03
description: 엘라스틱서치(Elasticsearch)는 대규모 데이터의 검색과 분석을 지원하는 오픈소스 분산 검색 엔진입니다. 일반적으로
  데이터의 빠른 검색과 실시간 로그 분석 등에 자주 사용됩니다. 설치와 간단한 사용 방법에 대해 단계별로 설명해드릴게요.
draft: false
image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
---

  22.04.1 ...
  shell scripting, system administration, terminal, unix, 방법, 사용하는, 서치, 엘라스틱

---

엘라스틱서치(Elasticsearch)는 대규모 데이터의 검색과 분석을 지원하는 오픈소스 분산 검색 엔진입니다. 일반적으로 데이터의 빠른 검색과 실시간 로그 분석 등에 자주 사용됩니다. 설치와 간단한 사용 방법에 대해 단계별로 설명해드릴게요.

---

## Table of Contents
---

## 1. 설치하기

### 0. 개발환경:

- Ubuntu 22.04.1 LTS

### 1. apt 업데이트 및 wget 등 필수 라이브러리 설치하기:

```bash
apt update -y
apt install apt-transport-https ca-certificates wget -y
```

- [Elasticsearch](https://www.elastic.co/kr/downloads/elasticsearch){:target="_blank"} 공식 사이트에서 운영체제에 맞는 버전을 다운로드합니다.
- 다운로드한 파일을 압축 해제하고, `bin/elasticsearch`를 실행하여 서버를 시작합니다.

### 2. 엘라스틱 서치 설치하기

```bash
# 리포지토리 GPG Key 가져오기
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

# Elastic search 리포지토리 시스템 추가
sh -c 'echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" > /etc/apt/sources.list.d/elastic-7.x.list'

# apt 업데이트
apt update -y

# Elastic search 설치하기
apt install elasticsearch -y
```

### 3. 외부 접속 및 Kibana 연결을 위해 설정

```bash
vi /etc/elasticsearch/elasticsearch.yml

...
# 원하는 node name을 설정
node.name: node-1

# 외부에서 접속할 수 있도록 오픈
network.host: 0.0.0.0
discovery.seed_hosts: ["elastic", "127.0.0.1"]

# node.name의 값을 설정
cluster.initial_master_nodes: ["node-1"]
...
```

---

## 2. 인덱스(Index) 만들기

Elasticsearch에서는 데이터를 인덱스라는 형태로 저장합니다. 인덱스는 일종의 데이터베이스에 해당합니다.

```bash
curl -X PUT "localhost:9200/my_index"
```

- 여기서 `my_index`는 새로 생성할 인덱스 이름입니다.

---

## 3. 문서(Document) 추가하기

문서는 Elasticsearch에서 기본 데이터 저장 단위입니다. 인덱스에 JSON 형식으로 문서를 추가할 수 있습니다.

```bash
curl -X POST "localhost:9200/my_index/_doc/1" -H 'Content-Type: application/json' -d'
{
  "name": "홍길동",
  "age": 30,
  "job": "개발자"
}
'
```

- `_doc/1` 부분에서 `1`은 문서 ID입니다. 고유한 ID를 지정하지 않으면 자동으로 ID가 부여됩니다.

---

## 4. 문서 검색하기

Elasticsearch는 기본적으로 강력한 검색 기능을 제공합니다. 간단한 예시로 인덱스 내 모든 문서를 검색할 수 있습니다.

```bash
curl -X GET "localhost:9200/my_index/_search"
```

- 조건 검색을 위해 쿼리를 추가할 수도 있습니다.

```bash
curl -X GET "localhost:9200/my_index/_search" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match": {
      "job": "개발자"
    }
  }
}
'
```

---

## 5. 인덱스 삭제하기

더 이상 필요 없는 인덱스는 삭제할 수 있습니다.

```bash
curl -X DELETE "localhost:9200/my_index"
```

---

## 6. Elasticsearch와 Kibana 연동하기

Elasticsearch와 시각화 도구인 Kibana를 연동하면 데이터를 쉽게 조회하고 분석할 수 있습니다. Elasticsearch 설치 후 Kibana를 설치한 다음, `localhost:5601`로 접속하면 Kibana 대시보드를 이용할 수 있습니다.

### 추가 팁

- **REST API 사용** : Elasticsearch는 대부분의 작업을 REST API로 처리하므로, 다양한 프로그래밍 언어에서도 연동할 수 있습니다.
- **분산 처리 및 확장성** : 데이터가 많아지면 노드를 추가하여 확장할 수 있습니다.

이 과정을 통해 기본적인 Elasticsearch 사용법을 익힐 수 있습니다.