# Roy's Factory

개발자 ROY의 개인 기술 블로그입니다.  
Jekyll 기반으로 제작되었으며, 리눅스 시스템 관리, AI/머신러닝, 개발 관련 다양한 기술 포스팅을 제공합니다.

**사이트**: https://royfactory.net

## 프로젝트 개요

Roy's Factory는 개발자를 위한 기술 블로그로, 실무에서 활용할 수 있는 다양한 기술 정보를 제공합니다.

### 주요 콘텐츠
- **Linux 시스템 관리**: 50여 개의 리눅스 관련 기술 포스트
- **AI/머신러닝**: RAG, 벡터 데이터베이스, BM25 등 최신 AI 기술
- **개발 도구**: 다양한 개발 환경 설정 및 도구 활용법
- **미니 웹앱**: 개발자 생산성 향상을 위한 유틸리티 도구들

## 프로젝트 구조

```
royfactory.net/
├── _config.yml                 # Jekyll 설정 파일
├── _data/
│   └── organisers.yml          # 작성자 정보
├── _includes/                  # 재사용 가능한 템플릿 조각
│   ├── footer.html
│   ├── head.html
│   └── header.html
├── _layouts/                   # 페이지 레이아웃 템플릿
│   ├── about.html              # 소개 페이지
│   ├── apps.html               # 앱 페이지
│   ├── archive.html            # 아카이브 페이지
│   ├── default.html            # 기본 레이아웃
│   ├── home.html               # 홈 페이지
│   ├── page.html               # 일반 페이지
│   └── post.html               # 포스트 페이지
├── _posts/                     # 블로그 포스트
│   ├── ai/                     # AI/머신러닝 관련 포스트
│   │   ├── 2024-11-14-what-is-the-rag.md
│   │   ├── 2024-11-15-what-is-the-bm25.md
│   │   ├── 2024-12-02-what-is-the-vector-db.md
│   │   ├── 2024-12-03-what-is-the-cos-similarity.md
│   │   ├── 2024-12-03-what-is-the-faiss.md
│   │   └── ...
│   ├── linux/                  # Linux 시스템 관리 포스트
│   │   ├── 2024-10-28-how-to-use-account.md
│   │   ├── 2024-11-01-how-to-use-chmod.md
│   │   ├── 2024-11-07-how-to-use-firewalld.md
│   │   ├── 2024-11-12-how-to-use-apache-access.md
│   │   └── ... (50여 개의 포스트)
│   └── summit/                 # 기타 포스트
├── _sass/                      # SCSS 스타일시트
│   ├── _base.scss
│   ├── _buttons.scss
│   ├── _layout.scss
│   └── _syntax-highlighting.scss
├── assets/                     # 정적 자원
│   ├── css/                    # CSS 파일
│   ├── fonts/                  # 웹폰트
│   ├── img/                    # 이미지 파일
│   └── js/                     # JavaScript 파일
├── apps/                       # 미니 웹앱
│   ├── bookmark/               # 북마크 관리 도구
│   ├── boxingtimer/            # 복싱 타이머
│   ├── myvoca/                 # 개인 단어장
│   ├── planktime/              # 플랭크 운동 타이머
│   ├── scoreboard/             # 스코어보드
│   └── tableclock/             # 테이블 시계
├── about.md                    # 소개 페이지
├── archive.md                  # 아카이브 페이지
├── index.html                  # 메인 페이지
└── README.md                   # 프로젝트 설명서
```

## 로컬 개발 환경 설정

### 1. 저장소 클론
```bash
git clone https://github.com/royfactory/royfactory.github.io.git
cd royfactory.net
```

### 2. Ruby 및 Jekyll 설치
```bash
# Bundler를 통한 의존성 설치
bundle install
```

### 3. 로컬 서버 실행
```bash
bundle exec jekyll serve
```

### 4. 브라우저에서 확인
```
http://localhost:4000
```

## 주요 기능

### 기술 블로그
- **Linux 시스템 관리**: 계정 관리, 파일 시스템, 네트워크, 보안 등
- **AI/머신러닝**: RAG, 벡터 데이터베이스, 코사인 유사도, BM25 알고리즘 등
- **개발 도구**: Apache, Nginx, Elasticsearch, 방화벽 설정 등

### 미니 웹앱
개발자 생산성 향상을 위한 유틸리티 도구들:
- **북마크 관리 도구**: 개발 관련 북마크 정리
- **복싱 타이머**: 운동 타이머 앱
- **개인 단어장**: 기술 용어 학습 도구
- **플랭크 운동 타이머**: 운동 관리 도구
- **스코어보드**: 점수 관리 도구
- **테이블 시계**: 시계 위젯

### 디자인 특징
- **반응형 디자인**: 모바일, 태블릿, 데스크톱 완벽 지원
- **SEO 최적화**: 검색 엔진 친화적 구조
- **현대적 UI**: 깔끔하고 직관적인 사용자 인터페이스
- **빠른 로딩**: 최적화된 정적 사이트

## 기술 스택

### 프론트엔드
- **정적 사이트 생성기**: Jekyll 4.3.4
- **마크업**: HTML5, Liquid 템플릿
- **스타일링**: SCSS, CSS3
- **스크립트**: JavaScript, jQuery
- **폰트**: Google Fonts (Droid Serif, Montserrat)

### 백엔드 & 인프라
- **호스팅**: GitHub Pages
- **도메인**: 커스텀 도메인 지원
- **플러그인**: 
  - jekyll-feed (RSS 피드)
  - jekyll-sitemap (사이트맵)
  - jekyll-toc (목차 자동 생성)

### 개발 도구
- **의존성 관리**: Bundler
- **버전 관리**: Git
- **테마**: Minima 기반 커스터마이징

## 콘텐츠 현황

### 블로그 포스트
- **총 포스트 수**: 60여 개
- **Linux 카테고리**: 50여 개 포스트
- **AI 카테고리**: 7개 포스트
- **업데이트 주기**: 주 1-2회

### 주요 시리즈
1. **Linux 시스템 관리 완전 가이드**
   - 사용자 계정 관리
   - 파일 시스템 및 권한 관리
   - 네트워크 설정 및 보안
   - 서버 설정 (Apache, Nginx, Samba 등)

2. **AI/머신러닝 기초**
   - RAG (Retrieval-Augmented Generation)
   - 벡터 데이터베이스와 유사도 측정
   - 정보 검색 알고리즘 (TF-IDF, BM25)

## 사이트 통계

- **월간 방문자**: 지속적 증가 추세
- **Google Analytics**: 설정 완료
- **SEO 최적화**: 메타 태그, 사이트맵 완비
- **RSS 피드**: 구독 가능

## 관련 링크

- **메인 사이트**: https://royfactory.net
- **개인 블로그**: https://royzero.tistory.com
- **GitHub**: https://github.com/royfactory
- **이메일**: worry1318@naver.com

## 라이선스

MIT License

Copyright (c) 2024 Roy (장진용)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

**Star를 눌러 프로젝트를 응원해주세요!**

개발자를 위한 유용한 기술 정보와 도구들을 지속적으로 업데이트하고 있습니다.

## 연락처

- **이메일**: worry1318@naver.com
- **블로그**: https://royzero.tistory.com
- **GitHub**: https://github.com/royfactory


