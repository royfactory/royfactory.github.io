// Sticky TOC with Auto-collapse functionality
document.addEventListener('DOMContentLoaded', function() {
    const tocContainer = document.querySelector('.toc-container');
    const toc = document.querySelector('.toc');
    
    if (!tocContainer || !toc) return;
    
    // TOC 구조 업데이트
    updateTocStructure();
    
    // 스크롤 이벤트 리스너
    let ticking = false;
    
    function handleScroll() {
        if (!ticking) {
            requestAnimationFrame(function() {
                updateTocPosition();
                updateActiveLink();
                ticking = false;
            });
            ticking = true;
        }
    }
    
    // TOC 구조 업데이트 (헤더와 토글 버튼 추가)
    function updateTocStructure() {
        const tocContent = toc.innerHTML;
        
        toc.innerHTML = `
            <div class="toc-header">
                <span class="toc-title">목차</span>
                <span class="toc-toggle">▼</span>
            </div>
            <div class="toc-content">
                ${tocContent}
            </div>
        `;
        
        // 기본적으로 접힌 상태로 시작
        toc.classList.add('collapsed');
        
        // 토글 기능 추가
        const tocHeader = toc.querySelector('.toc-header');
        if (tocHeader) {
            tocHeader.addEventListener('click', toggleToc);
        }
    }
    
    // TOC 토글 기능
    function toggleToc() {
        toc.classList.toggle('collapsed');
        
        // 로컬 스토리지에 상태 저장
        const isCollapsed = toc.classList.contains('collapsed');
        localStorage.setItem('tocCollapsed', isCollapsed);
    }
    
    // 저장된 상태 복원
    function restoreTocState() {
        const savedState = localStorage.getItem('tocCollapsed');
        
        // 저장된 상태가 없으면 기본적으로 접힌 상태 유지
        // 저장된 상태가 'false'인 경우에만 펼치기
        if (savedState === 'false') {
            toc.classList.remove('collapsed');
        }
        // 다른 모든 경우 (null, 'true', 기타)는 접힌 상태 유지
    }
    
    // TOC 위치 업데이트
    function updateTocPosition() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const tocOriginalTop = tocContainer.offsetTop;
        const threshold = 100; // 스크롤 임계값
        
        if (scrollTop > tocOriginalTop + threshold) {
            tocContainer.classList.add('sticky');
            
            // 자동 접기 (스크롤이 많이 내려갔을 때)
            if (scrollTop > tocOriginalTop + 500 && !toc.classList.contains('collapsed')) {
                // 사용자가 수동으로 펼쳐놓았다면 자동 접기 안함
                if (localStorage.getItem('tocManuallyExpanded') !== 'true') {
                    toc.classList.add('collapsed');
                }
            }
        } else {
            tocContainer.classList.remove('sticky');
            
            // 원래 위치로 돌아올 때는 사용자 설정 존중
            // 자동 펼치기 하지 않음 (사용자가 수동으로 펼쳐야 함)
        }
    }
    
    // 활성 링크 업데이트
    function updateActiveLink() {
        const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
        const tocLinks = document.querySelectorAll('.toc a');
        
        let activeHeading = null;
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const offset = 100;
        
        // 현재 보이는 헤딩 찾기
        for (let i = headings.length - 1; i >= 0; i--) {
            const heading = headings[i];
            const rect = heading.getBoundingClientRect();
            
            if (rect.top <= offset) {
                activeHeading = heading;
                break;
            }
        }
        
        // 모든 링크에서 active 클래스 제거
        tocLinks.forEach(link => link.classList.remove('active'));
        
        // 활성 링크에 클래스 추가
        if (activeHeading && activeHeading.id) {
            const activeLink = document.querySelector(`.toc a[href="#${activeHeading.id}"]`);
            if (activeLink) {
                activeLink.classList.add('active');
                
                // 활성 링크가 보이도록 스크롤
                const tocContent = document.querySelector('.toc-content');
                if (tocContent && !toc.classList.contains('collapsed')) {
                    const linkRect = activeLink.getBoundingClientRect();
                    const contentRect = tocContent.getBoundingClientRect();
                    
                    if (linkRect.top < contentRect.top || linkRect.bottom > contentRect.bottom) {
                        activeLink.scrollIntoView({
                            behavior: 'smooth',
                            block: 'center'
                        });
                    }
                }
            }
        }
    }
    
    // 수동 토글 감지
    const tocHeader = toc.querySelector('.toc-header');
    if (tocHeader) {
        tocHeader.addEventListener('click', function() {
            // 사용자가 수동으로 조작했음을 표시
            setTimeout(() => {
                if (!toc.classList.contains('collapsed')) {
                    localStorage.setItem('tocManuallyExpanded', 'true');
                } else {
                    localStorage.removeItem('tocManuallyExpanded');
                }
            }, 100);
        });
    }
    
    // 스무스 스크롤 추가
    const tocLinks = document.querySelectorAll('.toc a[href^="#"]');
    tocLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                const headerHeight = 80; // 헤더 높이 고려
                const targetTop = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;
                
                window.scrollTo({
                    top: targetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // 초기화
    restoreTocState();
    
    // 이벤트 리스너 등록
    window.addEventListener('scroll', handleScroll, { passive: true });
    window.addEventListener('resize', handleScroll, { passive: true });
    
    // 초기 위치 설정
    setTimeout(updateTocPosition, 100);
    setTimeout(updateActiveLink, 100);
});
