---
layout: post

#event information
title: "RAG (Retrieval-Augmented Generation)란 무엇인가?"
cover: "/img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg"
categories: ai
date: 2024-11-14
tags: ai rag

toc: true

#event organiser details
organiser: "Royfactory"


---

# RAG (Retrieval-Augmented Generation)란 무엇인가?
최근 몇 년간 자연어 처리(NLP) 기술이 급격히 발전하면서, 대규모 언어 모델(LLM)들이 다양한 문제를 해결하는 데 사용되고 있습니다. 그러나 LLM은 모든 정보를 내부에 저장하고 추론하는 방식으로 설계되어 있어, 최신 정보나 방대한 외부 데이터를 활용하는 데 한계가 있습니다. 이러한 한계를 극복하기 위해 등장한 기술이 바로 RAG (Retrieval-Augmented Generation) 입니다.

---

## RAG의 개념
RAG는 Retrieval-Augmented Generation의 약자로, 대규모 언어 모델(Generation)과 외부 정보 검색(Retrieval)을 결합한 하이브리드 방식입니다. 이 기술은 다음 두 가지 단계를 통해 작동합니다:
1. **Retrieval (정보 검색)**
  - 입력 질문에 대해 적합한 정보를 외부 데이터베이스나 문서에서 검색합니다.
  - 검색된 정보는 모델의 컨텍스트로 제공됩니다.
2. **Generation (텍스트 생성)**
  - 검색된 정보를 기반으로 대규모 언어 모델이 응답을 생성합니다.
  - 생성된 응답은 검색된 데이터와 질문을 통합하여 보다 정확하고 구체적인 결과를 제공합니다.

이 과정을 통해 RAG는 대규모 언어 모델의 한계를 보완하고, 최신 정보나 특정 도메인의 전문 지식을 활용할 수 있게 됩니다.

--- 

## RAG의 구조
RAG의 구조는 크게 두 가지로 나뉩니다.

### 1. Retriver
Retriever는 입력 쿼리(질문)와 관련된 정보를 검색하는 역할을 합니다. 일반적으로 다음과 같은 기술이 사용됩니다:
- **Sparse Retrieval**: TF-IDF, BM25와 같은 전통적인 정보 검색 알고리즘
- **Dense Retrieval**: 문서와 쿼리를 벡터로 임베딩하여 유사도를 계산하는 방식 (예: DPR, Sentence-BERT)

### 2. Generator
Generator는 검색된 정보를 바탕으로 텍스트를 생성합니다. 주로 GPT 계열의 언어 모델이 사용되며, Retrieval 단계에서 제공된 정보를 컨텍스트로 활용하여 응답을 생성합니다.

---

## RAG의 장점
1. **최신성**
  - LLM은 훈련 시점 이후의 정보에 접근할 수 없지만, RAG는 외부 데이터베이스에서 최신 정보를 검색하여 활용할 수 있습니다.
2. **효율성**
  - 모든 정보를 모델 내부에 포함시키는 대신, 필요한 정보만 검색하여 사용하므로 모델 크기와 메모리 요구사항을 줄일 수 있습니다.
3. **도메인 확장성**
  - 특정 도메인에 대한 지식이 부족한 모델도 관련 데이터베이스를 통해 전문적인 응답을 생성할 수 있습니다.

---

## RAG의 한계
1. **의존성**
  - Retrieval 단계에서 부정확한 정보가 검색될 경우, Generation 결과도 잘못될 가능성이 있습니다.
2. **속도**
  - 검색과 생성 과정을 거치므로 순수 언어 모델보다 응답 속도가 느릴 수 있습니다.
3. **복잡성**
  - Retrieval와 Generation 단계를 결합해야 하므로 시스템 설계와 구현이 복잡합니다.

---

## RAG의 활용 사례
1. **챗봇**
  - 고객 지원 챗봇에서 RAG를 사용하면 최신 데이터나 제품 정보를 실시간으로 반영하여 사용자에게 더 나은 답변을 제공합니다.
2. **지식 검색 시스템**
  - 대규모 문서나 논문 데이터베이스에서 특정 질문에 대한 답변을 생성하는 데 활용됩니다.
3. **의료 및 법률**
  - 최신 의료 논문이나 법률 문서를 검색하여 전문가 수준의 정보를 제공합니다.

---

## 결론
RAG는 LLM의 한계를 보완하면서도 최신성과 확장성을 갖춘 강력한 기술입니다. 검색과 생성을 결합한 방식은 다양한 응용 분야에서 혁신적인 가능성을 열어줍니다. RAG를 활용하여 더욱 정교하고 실시간으로 대응 가능한 시스템을 구축할 수 있습니다.

---