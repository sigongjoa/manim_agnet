# 🎨 AI-Powered 코딩 문제 시각화 시스템

온라인 코딩테스트(LeetCode, 백준)의 대표 문제들을 **AI가 자동으로 분석**하고 **Manim으로 시각화**하는 시스템입니다.

## 📋 목차
- [시스템 개요](#시스템-개요)
- [지원 문제](#지원-문제)
- [설치 및 실행](#설치-및-실행)
- [파일 구조](#파일-구조)
- [사용 방법](#사용-방법)
- [커스터마이징](#커스터마이징)

---

## 🎯 시스템 개요

### 핵심 기능
1. **자동 알고리즘 분석**: AI가 문제의 해법을 자동으로 분석
2. **Manim 시각화**: Python Manim으로 알고리즘을 단계별로 시각화
3. **한글 음성 나레이션**: TTS(GTTS)를 사용한 한국어 자동 설명
4. **웹 뷰어**: 브라우저에서 모든 시각화를 한 곳에서 재생 가능
5. **수정 가능한 구조**: 사용자가 각 단계별로 수정 및 개선 가능

---

## 📚 지원 문제

### LeetCode
| # | 문제명 | 알고리즘 | 난이도 |
|---|--------|---------|--------|
| 1 | Two Sum | HashMap / Array | Medium |
| 102 | Binary Tree Level Order | BFS / Queue | Medium |

### 백준 (Baekjoon)
| # | 문제명 | 알고리즘 | 난이도 |
|---|--------|---------|--------|
| 1463 | 1로 만들기 | Dynamic Programming | Silver III |
| 2750 | 수 정렬하기 | Sorting (Bubble Sort) | Bronze I |

---

## 🚀 설치 및 실행

### 전제 조건
```bash
# Python 3.8+, Manim, manim-voiceover 설치 완료
python --version  # Python 3.8 이상 확인
```

### 1단계: 가상 환경 활성화
```bash
source /mnt/d/progress/manim_agent/manim_env/bin/activate
# Windows: manim_env\Scripts\activate
```

### 2단계: 모든 시각화 렌더링
```bash
# 자동 렌더링 스크립트 실행
python render_all_problems.py
```

**또는** 개별 렌더링:
```bash
# Two Sum
manim two_sum_visualization.py TwoSumVisualization -m

# Binary Tree Level Order
manim tree_level_order_visualization.py BinaryTreeLevelOrderVisualization -m

# 1로 만들기
manim dp_make_one_visualization.py DPMakeOneVisualization -m

# 수 정렬하기
manim sort_visualization.py SortVisualization -m
```

### 3단계: 웹 뷰어 열기
```bash
# 아래 파일을 브라우저로 열기:
# problem_viewer.html

# 또는 간단한 로컬 서버 시작:
python -m http.server 8000
# http://localhost:8000/problem_viewer.html 접속
```

---

## 📁 파일 구조

```
manim_agent/
├── 📋 문제 시각화 파일
│   ├── two_sum_visualization.py              # LeetCode #1 - Two Sum
│   ├── tree_level_order_visualization.py     # LeetCode #102 - BFS
│   ├── dp_make_one_visualization.py          # 백준 #1463 - DP
│   ├── sort_visualization.py                 # 백준 #2750 - 정렬
│   └── problem_visualizer.py                 # AI 분석 및 메타데이터
│
├── 🔧 실행 및 유틸리티
│   ├── render_all_problems.py                # 모든 문제 일괄 렌더링
│   └── problem_viewer.html                   # 웹 기반 뷰어
│
├── 📚 기존 파일들
│   ├── korean_math_problem.py                # 수학 문제 예제
│   ├── circle_angle_scene.py                 # 도형 시각화 예제
│   ├── voiceover_example.py                  # 음성 나레이션 예제
│   └── image_to_manim.py                     # 이미지 벡터화
│
├── 🎬 생성된 미디어
│   └── media/
│       └── videos/
│           ├── two_sum_visualization/
│           ├── tree_level_order_visualization/
│           ├── dp_make_one_visualization/
│           └── sort_visualization/
│
└── 📖 문서
    ├── README.md
    └── README_PROBLEM_VISUALIZER.md (이 파일)
```

---

## 💡 사용 방법

### 웹 뷰어에서 보기
1. `problem_viewer.html`을 브라우저로 오픈
2. 4가지 문제 카드에서:
   - 📺 비디오 재생 (렌더링 후)
   - 🔗 원본 문제 링크 클릭
   - 💾 비디오 다운로드

### 개별 문제 수정하기

#### Two Sum 수정 예시
```python
# two_sum_visualization.py 열기
# TwoSumVisualization 클래스 수정:
# - 배열 값 변경
# - 애니메이션 타이밍 조정
# - 나레이션 텍스트 수정
```

#### 렌더링
```bash
manim two_sum_visualization.py TwoSumVisualization -m
```

---

## 🎨 커스터마이징

### 나레이션 수정

현재 한국어 TTS를 사용합니다. 수정하려면:

```python
# 기존 코드
with self.voiceover(text="안녕하세요! 오늘은 Two Sum 문제를..."):
    # 애니메이션

# 수정 후
with self.voiceover(text="[수정된 텍스트]"):
    # 애니메이션
```

### 애니메이션 속도 조절

```python
# 기본: run_time 파라미터로 조절
self.play(Create(circle), run_time=2)  # 2초

# 또는 Scene 전체 속도 변경
# manim -m -s (--speed_up 적용)
```

### 배열/그래프 데이터 변경

```python
# 원본 배열 변경
nums = [5, 2, 8, 1, 9]  # 필요한 배열로 수정
target = 9

# 그러면 자동으로 시각화 업데이트
```

### 폰트 변경

```python
# 현재 한글 폰트: NanumGothic
Text("텍스트", font="NanumGothic")

# 다른 폰트로 변경 가능:
Text("텍스트", font="/path/to/font.ttf")
```

---

## 🔧 고급 기능

### 렌더링 품질 조정

```bash
# 저품질 (빠름)
manim two_sum_visualization.py TwoSumVisualization -l

# 중품질 (권장)
manim two_sum_visualization.py TwoSumVisualization -m

# 고품질 (느림)
manim two_sum_visualization.py TwoSumVisualization -k
```

### 비디오 포맷 변경

```bash
# MP4 (기본값)
manim two_sum_visualization.py TwoSumVisualization -m

# GIF 생성
manim two_sum_visualization.py TwoSumVisualization -m --format gif
```

### 특정 레이아웃으로 렌더링

```bash
# 기본 (9:16)
manim two_sum_visualization.py TwoSumVisualization -m

# 와이드스크린 (16:9)
manim two_sum_visualization.py TwoSumVisualization -m --config_file custom_config.cfg
```

---

## 📊 각 문제별 상세 설명

### 1️⃣ Two Sum (LeetCode #1)

**문제:**
```
nums = [2, 7, 11, 15], target = 9
출력: [0, 1] (nums[0] + nums[1] = 9)
```

**해법:**
- HashMap을 사용하여 O(n) 시간에 해결
- 각 원소에 대해 complement(target - num) 확인
- HashMap에 있으면 바로 답 반환

**시각화 순서:**
1. 배열 표시
2. HashMap 초기화
3. 각 원소 순회
4. complement 계산 및 HashMap 조회
5. 답 찾기

---

### 2️⃣ Binary Tree Level Order (LeetCode #102)

**문제:**
```
트리:     3
         / \
        9  20
          /  \
         15   7

출력: [[3], [9, 20], [15, 7]]
```

**해법:**
- BFS(너비 우선 탐색) 알고리즘
- Queue를 사용하여 레벨별 노드 처리
- 각 레벨의 노드들을 한 번에 처리

**시각화 순서:**
1. 트리 구조 그리기
2. 루트 노드부터 큐에 추가
3. 각 레벨별로 노드 처리
4. 최종 결과 표시

---

### 3️⃣ 1로 만들기 (백준 #1463)

**문제:**
```
N = 10 일 때:
- 10 → 5 → 4 → 2 → 1 (3번 연산)
- 연산: /3, /2, -1 (각 조건에 맞을 때)
```

**해법:**
- Dynamic Programming (DP)
- dp[i] = i를 1로 만드는 최소 연산 횟수
- 각 i에 대해 가능한 모든 연산의 최솟값

**시각화 순서:**
1. 문제 설명 및 연산 소개
2. DP 배열 초기화
3. 단계별 DP 값 계산
4. 최적 경로 추적

---

### 4️⃣ 수 정렬하기 (백준 #2750)

**문제:**
```
입력: [5, 2, 8, 1, 9]
출력: [1, 2, 5, 8, 9]
```

**해법:**
- Bubble Sort 알고리즘 (시각화 친화적)
- 인접한 두 원소 비교 후 교환
- 각 Pass마다 가장 큰 원소가 맨 뒤로

**시각화 순서:**
1. 초기 배열 표시
2. 인접한 원소들 비교
3. 필요시 교환 시각화
4. Pass 완료 후 상태 확인
5. 반복

---

## 📝 비고

### 한글 경로 문제 해결 ✅
- UTF-8 인코딩 사용
- 한글 폰트 (NanumGothic) 지정
- 파일명은 영문 유지

### 음성 나레이션 ✅
- Google Text-to-Speech (GTTS) 사용
- 한국어 지원 (`lang="ko"`)
- 대사와 애니메이션 동기화

### 커스터마이징 가능성 ✅
- 모든 시각화 코드는 수정 가능
- 단계별 애니메이션 조절 가능
- 새로운 문제 추가 용이

---

## 🚀 다음 단계 (추천)

1. **더 많은 문제 추가**
   - Graph 문제들 (DFS, 최단경로)
   - DP 심화 문제들
   - 그리디 알고리즘

2. **웹 인터페이스 확장**
   - 비디오 업로드 및 관리
   - 문제별 댓글/피드백
   - 난이도별 필터링

3. **자동화 개선**
   - 문제 크롤링 자동화
   - AI 해설 생성 개선
   - 배치 렌더링 최적화

4. **공유 기능**
   - 소셜 미디어 공유
   - 임베딩 코드 생성
   - PDF 교재 생성

---

## 📞 문제 해결

### 비디오가 렌더링되지 않음
```bash
# 1. Manim 설치 확인
manim --version

# 2. 가상 환경 활성화 확인
which manim  # Linux/Mac
where manim  # Windows

# 3. 의존성 설치
pip install -r requirements.txt
```

### 한글이 깨지는 경우
```bash
# 한글 폰트 설치 (Ubuntu/Debian)
sudo apt-get install fonts-noto-cjk

# macOS
brew install font-noto-naskh-arabic font-noto-sans-cjk
```

### 메모리 부족
```bash
# 낮은 품질로 렌더링
manim two_sum_visualization.py TwoSumVisualization -l
```

---

## 📄 라이센스

이 프로젝트는 교육 목적으로 제작되었습니다.

---

**마지막 업데이트**: 2024-11-21
**버전**: 1.0.0
