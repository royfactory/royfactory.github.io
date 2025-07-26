# GitHub Pages Hugo 설정 가이드

이 문서는 GitHub Pages에서 Hugo 사이트를 올바르게 배포하기 위한 설정 가이드입니다.

## 필수 설정 사항

### 1. GitHub Repository 설정

#### Pages 설정
1. GitHub 저장소로 이동: https://github.com/royfactory/royfactory.github.io
2. **Settings** > **Pages** 메뉴로 이동
3. **Source** 설정을 **GitHub Actions**로 변경
   - ⚠️ **중요**: "Deploy from a branch"가 아닌 "GitHub Actions"를 선택해야 함

#### Actions 권한 설정
1. **Settings** > **Actions** > **General** 메뉴로 이동
2. **Workflow permissions** 섹션에서:
   - "Read and write permissions" 선택
   - "Allow GitHub Actions to create and approve pull requests" 체크

### 2. 파일 구조 확인

다음 파일들이 올바르게 설정되어 있는지 확인:

```
royfactory.github.io/
├── .github/workflows/hugo.yml    # Hugo 배포 워크플로우
├── .nojekyll                     # Jekyll 비활성화
├── hugo.toml                     # Hugo 설정
├── content/                      # Hugo 콘텐츠
├── themes/PaperMod/             # Hugo 테마
└── static/                      # 정적 파일들
```

### 3. 중요한 파일들

#### `.nojekyll`
- GitHub Pages가 Jekyll 대신 GitHub Actions를 사용하도록 함
- 파일 내용: 빈 파일

#### `hugo.toml`
- Hugo 사이트 설정
- baseURL이 올바른 GitHub Pages URL로 설정되어야 함: `https://royfactory.github.io`

#### `.github/workflows/hugo.yml`
- Hugo 빌드 및 배포 자동화
- GitHub Actions 워크플로우 정의

## 배포 과정

### 자동 배포 프로세스
1. **코드 푸시**: `main` 브랜치에 푸시
2. **Actions 트리거**: GitHub Actions 워크플로우 자동 시작
3. **Hugo 빌드**: 사이트 빌드 및 최적화
4. **Pages 배포**: GitHub Pages에 자동 배포

### 배포 상태 확인
- **Actions 탭**: https://github.com/royfactory/royfactory.github.io/actions
- **배포된 사이트**: https://royfactory.github.io

## 문제 해결

### 일반적인 문제들

#### 1. "Your site is having problems building"
**원인**: Jekyll 설정과 Hugo 설정이 충돌
**해결방법**: 
- `.nojekyll` 파일 존재 확인
- Jekyll 파일들 (_config.yml, Gemfile) 제거 또는 이름 변경

#### 2. "Page not found" 또는 404 오류
**원인**: GitHub Pages 소스 설정이 잘못됨
**해결방법**:
- Settings > Pages > Source를 "GitHub Actions"로 설정
- hugo.toml의 baseURL 확인

#### 3. 워크플로우 실패
**원인**: 권한 또는 설정 문제
**해결방법**:
- Settings > Actions에서 권한 설정 확인
- 워크플로우 로그에서 오류 메시지 확인

#### 4. 테마가 제대로 로드되지 않음
**원인**: Git submodule 문제
**해결방법**:
```bash
git submodule update --init --recursive
```

### 수동 배포 트리거
워크플로우를 수동으로 실행하려면:
1. Actions 탭으로 이동
2. "Deploy Hugo Site to GitHub Pages" 워크플로우 선택
3. "Run workflow" 버튼 클릭

## 성능 최적화

### Hugo 설정 최적화
- `hugo.toml`에서 최적화 옵션 활성화
- 이미지 압축 및 최적화
- CSS/JS 압축 (minify)

### GitHub Pages 최적화
- CDN 활용 (자동 제공)
- HTTPS 강제 사용
- 커스텀 도메인 설정 (선택사항)

## 추가 기능

### 커스텀 도메인 설정
1. Settings > Pages > Custom domain에 도메인 입력
2. DNS 설정에서 CNAME 레코드 추가
3. HTTPS 강제 사용 설정

### 보안 설정
- Branch protection rules 설정
- Signed commits 요구
- Vulnerability alerts 활성화

---

## 체크리스트

배포 전 다음 사항들을 확인하세요:

- [ ] GitHub Pages Source가 "GitHub Actions"로 설정됨
- [ ] Actions 권한이 "Read and write permissions"로 설정됨
- [ ] `.nojekyll` 파일이 루트 디렉토리에 존재
- [ ] `hugo.toml`의 baseURL이 올바름
- [ ] Jekyll 설정 파일들이 비활성화됨
- [ ] 테마 서브모듈이 올바르게 설정됨
- [ ] 워크플로우 파일이 올바른 위치에 있음

모든 설정이 완료되면 코드를 푸시하여 자동 배포를 테스트하세요! 🚀
