---
layout: post

#event information
title: "코사인 유사도란 무엇인가?"
cover: "/img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg"
categories: ai
date: 2024-12-03
tags: ai vector-db vector-database cos-similarity cosine-similarity algorithm

toc: true

#event organiser details
organiser: "Royfactory"


---

## 1. 코사인 유사도란?
코사인 유사도(Cosine Similarity)는 두 벡터 간의 **각도(Cosine of the Angle)**를 기반으로 유사성을 측정하는 방법입니다. 벡터의 크기(길이)가 아니라 방향에 초점을 맞추기 때문에, 데이터의 크기가 다르더라도 유사성을 계산하는 데 유용합니다.
코사인 유사도의 값은 -1부터 1 사이의 범위를 가지며:
- 1: 두 벡터가 완전히 같은 방향을 가짐 (가장 유사).
- 0: 두 벡터가 서로 직각(독립적).
- -1: 두 벡터가 반대 방향을 가짐 (가장 비유사).

---

## 2. 코사인 유사도 공식
두 벡터 $𝐴$와 $𝐵$의 코사인 유사도는 다음과 같이 계산됩니다:

$$
\text{Cosine Similarity}(A, B) = \frac{\vec{A} \cdot \vec{B}}{\|\vec{A}\| \|\vec{B}\|}
$$

여기서:
- $\vec{A} \cdot \vec{B}$는 두 벡터의 내적
- $\|\vec{A}\|$ 벡터 $\text{A}$의 크기 (Euclidean Norm).
- $\|\vec{B}\|$ 벡터 $\text{B}$의 크기.

### 내적과 벡터 크기
**1. 내적**:

$$
\vec{A} \cdot \vec{B} = \sum\limits_{i=1}^n A_i B_i
$$

**2. 벡터 크기**:

$$
\|\vec{A}\| = \sqrt{\sum\limits_{i=1}^n A_i^2} \, ,\, \|\vec{B}\| = \sqrt{\sum\limits_{i=1}^n B_i^2}
$$

---

## 3. 코사인 유사도의 특징
1. **크기의 영향 배제**:
  - 벡터의 크기는 무시되고, 방향(패턴)의 유사성을 측정합니다.
  - 텍스트 분석에서 단어 빈도가 다르더라도 패턴을 비교할 수 있습니다.
2. **0~1 사이의 범위로 해석 가능**:
  - $\text{1}$에 가까울수록 유사, $\text{0}$에 가까울수록 비유사.
3. **고차원 데이터에 적합**:
  - 벡터가 고차원이라도 효율적으로 유사성을 계산할 수 있습니다.

---

## 4. 코사인 유사도 계산 예제
### 2차원 벡터 예제
벡터 $\text{A} = [3, 4], \text{B} = [4, 3]$일 때:

**1. 내적 계산**:

$$
\vec{A} \cdot \vec{B} = (3 \cdot 4) + (4 \cdot 3) = 12 + 12 = 24
$$


**2. 벡터 크기 계산**:

$$
\|\vec{A}\| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = 5
\\
\|\vec{B}\| = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = 5
$$

**3. 코사인 유사도 계산**:

$$
\text{Cosine Similarity}(A, B) = \frac{24}{5 \cdot 5} = \frac{24}{25} = 0.96
$$

이 멕터는 매우 유사하다고 판단됩니다.

---

## 5. 코사인 유사도의 활용 사례
### 1) 텍스트 유사도 분석
- **단어 임베딩**: 문장을 벡터로 변환하고, 코사인 유사도로 유사한 문장을 찾습니다.
- **예제**: "I love AI"와 "AI is great" 사이의 의미적 유사성을 계산.
### 2) 추천 시스템
- 사용자와 아이템의 벡터를 기반으로 선호도를 계산하여 추천합니다.
- **예제**: 영화 추천 시스템에서 사용자의 시청 이력과 유사한 영화를 추천.
### 3) 이미지 검색
- 이미지 특징을 벡터로 변환하여, 유사한 이미지를 검색합니다.
### 4) 클러스터링
- 데이터 포인트 간 코사인 유사도를 계산하여 비슷한 항목끼리 그룹화합니다.

---

## 6. 코사인 유사도의 장단점
### 장점
1. **크기 독립적**: 벡터의 크기(스케일)가 달라도 비교 가능.
2. **효율적**: 고차원 데이터를 처리할 때 계산이 단순.
3. **다양한 활용**: 텍스트, 이미지, 오디오 등 다양한 데이터 유형에 적용 가능.

### 단점
1. **희소 벡터의 한계**:
  - 매우 희소한 데이터(예: 문서의 TF-IDF 벡터)는 유사성이 낮게 계산될 수 있음.
2. **선형 관계만 측정**:
  - 비선형 관계를 다루지 못하며, 복잡한 관계를 반영하는 데 한계가 있음.

---

## 7. 코사인 유사도와 유클리디안 거리 비교

|특징|코사인 유사도|유클리디안 거리|
|---|------|-----|
|측정 방식|두 벡터 간의 각도|두 점 간의 직선 거리|
|크기 영향|무시|크기에 민감|
|적용 사례|텍스트 분석, 추천 시스템|위치 정보, 물리적 거리 계산|
|값의 범위|-1 ~ 1|0 이상|

---

## 8. 결론
코사인 유사도는 데이터 크기에 민감하지 않고, 방향 기반의 유사성을 측정하는 데 강력한 도구입니다. 텍스트, 이미지, 추천 시스템 등 다양한 분야에서 널리 사용되며, 특히 고차원 데이터에서 효과적입니다. 하지만, 특정 데이터 유형(예: 희소 벡터)에서는 보완적 방법과 함께 사용하는 것이 좋습니다.

---