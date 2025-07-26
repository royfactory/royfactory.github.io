# Jekyll to Hugo Migration Guide

이 문서는 Royfactory 블로그를 Jekyll에서 Hugo로 성공적으로 마이그레이션한 과정을 설명합니다.

## 완료된 작업

### 1. Hugo 프로젝트 설정
- ✅ Hugo 설정 파일 (`hugo.toml`) 생성
- ✅ PaperMod 테마 설치
- ✅ 기본 디렉토리 구조 생성

### 2. 콘텐츠 변환
- ✅ Jekyll 포스트를 Hugo 포스트로 변환 (총 65개 포스트)
  - AI 카테고리: 22개 포스트
  - Linux 카테고리: 30개 포스트  
  - Cloud 카테고리: 15개 포스트
- ✅ Frontmatter 형식 변환 (Jekyll → Hugo)
- ✅ TOC (Table of Contents) 변환
- ✅ 태그 및 카테고리 시스템 변환

### 3. 정적 파일 마이그레이션
- ✅ 이미지 파일 복사 (`/img`, `/assets`)
- ✅ SEO 파일들 복사 (`robots.txt`, `sitemap.xml`, `ads.txt` 등)

### 4. 페이지 생성
- ✅ About 페이지
- ✅ Archive 페이지
- ✅ Apps 페이지
- ✅ 홈페이지

### 5. 배포 설정
- ✅ GitHub Actions 워크플로우 생성 (Hugo 배포용)

## 사이트 구조

```
royfactory.github.io/
├── hugo.toml                 # Hugo 설정 파일
├── content/                  # 콘텐츠 디렉토리
│   ├── _index.md            # 홈페이지
│   ├── about.md             # About 페이지
│   ├── archive.md           # Archive 페이지
│   ├── apps.md              # Apps 페이지
│   └── posts/               # 블로그 포스트
│       ├── ai/              # AI 관련 포스트
│       ├── cloud/           # 클라우드 관련 포스트
│       ├── linux/           # 리눅스 관련 포스트
│       └── summit/          # 서밋 관련 포스트
├── static/                  # 정적 파일
│   ├── img/                 # 이미지
│   ├── assets/              # 기타 자산
│   └── robots.txt           # SEO 파일들
├── themes/                  # 테마 디렉토리
│   └── PaperMod/           # PaperMod 테마
└── .github/workflows/       # GitHub Actions
    └── hugo.yml            # Hugo 배포 워크플로우
```

## Hugo 사이트 특징

### 테마: PaperMod
- 현대적이고 깔끔한 디자인
- 다크/라이트 모드 지원
- 빠른 로딩 속도
- SEO 최적화
- 모바일 반응형

### 주요 기능
- 🔍 검색 기능
- 📱 모바일 최적화
- ⚡ 빠른 페이지 로딩
- 📊 Google Analytics 지원
- 🔗 소셜 링크 (GitHub, Tistory)
- 📖 목차 (TOC) 자동 생성
- 🏷️ 태그 및 카테고리 시스템

## 로컬 개발

### 개발 서버 시작
```bash
cd /Users/royzero/royfactory.github.io
hugo server --buildDrafts --port 1314
```

### 사이트 빌드
```bash
hugo
```

빌드된 파일은 `public/` 디렉토리에 생성됩니다.

## 배포

GitHub Pages를 통한 자동 배포가 설정되어 있습니다:

1. `main` 브랜치에 푸시
2. GitHub Actions가 자동으로 Hugo 빌드 실행
3. GitHub Pages에 배포

## 성능 향상

Hugo로 마이그레이션 후 다음과 같은 성능 향상을 기대할 수 있습니다:

- ⚡ **빌드 속도**: Jekyll 대비 10-100배 빠른 빌드
- 🚀 **로딩 속도**: 정적 파일 최적화로 더 빠른 페이지 로딩
- 📱 **모바일 최적화**: PaperMod 테마의 반응형 디자인
- 🔍 **SEO**: 향상된 SEO 최적화

## 추가 작업 (선택사항)

향후 고려할 수 있는 추가 기능들:

- [ ] 댓글 시스템 (Disqus, Giscus 등)
- [ ] 검색 기능 강화 (Algolia, Lunr.js)
- [ ] PWA (Progressive Web App) 지원
- [ ] 다국어 지원
- [ ] 커스텀 테마 개발

## 문제 해결

### 일반적인 문제들

1. **빌드 오류**: Frontmatter 형식 확인
2. **이미지 표시 안됨**: `/static` 디렉토리 경로 확인
3. **테마 문제**: 서브모듈 업데이트 (`git submodule update --init --recursive`)

### 유용한 명령어

```bash
# 테마 업데이트
git submodule update --remote --merge

# 캐시 정리
hugo --cleanDestinationDir

# 초안 포함 빌드
hugo --buildDrafts

# 미래 날짜 포스트 포함
hugo --buildFuture
```

---

**마이그레이션 완료!** 🎉

Jekyll에서 Hugo로의 성공적인 마이그레이션이 완료되었습니다. 새로운 Hugo 사이트는 더 빠르고 현대적인 기능들을 제공합니다.
