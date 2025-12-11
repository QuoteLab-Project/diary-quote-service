![베드바츠마루](https://bestfriend.hellosweetdays.kr/_nuxt/img/img_16_character.dfff15f.png)

# 오늘의 다이어리 / Diary Quote Service

FastAPI, Tortoise ORM, PostgreSQL, uv 패키지 매니저를 사용해 구현한  
**“일기 + 명언 + 오늘의 질문”** 웹 서비스입니다.

사용자는 회원가입과 로그인을 통해 본인 계정으로 접속하고,  
홈 화면에서 다음을 할 수 있습니다.

- 웹 스크래핑으로 수집한 명언을 카드 형태로 확인
- 북마크할 명언 선택(구현/계획)
- “오늘의 질문”에 대한 답을 일기로 기록
- 최근 일기 목록을 날짜/시간과 함께 조회 및 수정·삭제

이 README는 **현재까지 작업한 내용 기준**으로 작성되었습니다.

---

## 목차

1. [프로젝트 개요](#프로젝트-개요)  
2. [핵심 기능](#핵심-기능)  
   - [인증(Auth)](#인증auth)  
   - [일기(Diary)](#일기도iary)  
   - [명언(Quote)](#명언quote)  
   - [오늘의 질문(Today’s Question)](#오늘의-질문todays-question)  
   - [홈 화면(Frontend)](#홈-화면frontend)  
3. [기술 스택](#기술-스택)  
4. [프로젝트 구조](#프로젝트-구조)  
5. [사전 준비 사항](#사전-준비-사항)  
6. [로컬 개발 환경 설정](#로컬-개발-환경-설정)  
7. [환경 변수 설정](#환경-변수-설정)  
8. [데이터베이스 & 마이그레이션](#데이터베이스--마이그레이션)  
9. [서버 실행 방법](#서버-실행-방법)  
10. [API 명세(초안)](#api-명세초안)  
11. [프론트엔드 동작 개요](#프론트엔드-동작-개요)  
12. [개발/협업 규칙](#개발협업-규칙)  
13. [향후 개선 계획](#향후-개선-계획)

---

## 프로젝트 개요

**오늘의 다이어리(Diary Quote Service)** 는 다음과 같은 목적을 가진 웹 서비스입니다.

- 하루를 돌아보는 **일기**와
- 영감을 주는 **명언(Quote)**,
- 스스로에게 던지는 **오늘의 질문(Today’s Question)**

을 한 화면에서 다루며,  
사용자가 규칙적으로 기록하고 생각을 정리할 수 있게 돕는 것을 목표로 합니다.

특징:

- FastAPI 기반 **백엔드 API 서버**
- Jinja2 템플릿 + JS/CSS로 만든 간단한 **프론트엔드**
- **JWT 인증** + **토큰 블랙리스트** 로 로그아웃 처리
- **Tortoise ORM + Aerich** 로 DB 스키마 관리
- **PostgreSQL**을 메인 DBMS로 사용
- **웹 스크래핑(BeautifulSoup)** 으로 명언 데이터 수집

---

## 핵심 기능

### 인증(Auth)

- **회원가입**
  - 이메일(email), 닉네임(nickname), 비밀번호(password)를 이용해 회원가입
  - 비밀번호는 `bcrypt`로 해시하여 DB에 저장

- **로그인**
  - 로그인 성공 시 **JWT Access Token** 발급
  - 클라이언트는 토큰을 LocalStorage/SessionStorage 등에 저장 후  
    이후 요청에서 `Authorization: Bearer <token>` 헤더로 전송

- **로그아웃**
  - 발급된 토큰을 `TokenBlacklist` 테이블에 저장
  - 블랙리스트에 포함된 토큰으로 API 접근 시 `401 Unauthorized` 응답

- **현재 유저 확인**
  - `HTTPBearer` 의존성을 이용해 헤더에서 토큰 추출
  - `jose.jwt` 로 디코딩
  - 토큰 블랙리스트 여부 확인
  - 유효한 경우 해당 `User` 인스턴스 반환

---

### 일기(Diary)

- **일기 작성 (Create)**
  - 제목, 내용, 작성 날짜/시간을 함께 저장
  - 작성 시점의 `created_at` 타임스탬프 기록

- **일기 조회 (Read)**
  - 로그인한 유저의 일기 목록 조회
  - 홈 화면에서 **내 최근 일기 카드**에 N개 표시
  - 일기마다 `작성 날짜 + 시간대` 가 함께 보이도록 구현

- **일기 수정 (Update)**
  - 기존 일기의 제목/내용 수정
  - 수정 시 `updated_at` 필드 자동 갱신

- **일기 삭제 (Delete)**
  - 특정 일기를 삭제

---

### 명언(Quote)

- **명언 데이터 수집**
  - 예: `https://saramro.com/quotes?page=1..N` 형태의 페이지를 대상으로
    `requests + BeautifulSoup`을 사용해 스크래핑
  - `<td colspan="5">` 등의 셀에서 텍스트를 추출한 후
    - `content` : 명언 문장
    - `author` : 저자
  - 형태로 파싱해 리스트 또는 DB에 저장

- **명언 카드**
  - 홈 화면에 랜덤 혹은 지정 로직에 따른 명언 1개 표시
  - 요소:
    - 명언 텍스트
    - 저자 이름
  - “명언 바꾸기” 버튼 클릭 시 JS로 API 호출 → 새로운 명언 로드
  - “북마크” 버튼(마음에 드는 명언 저장) 기능 구현/확장 예정

---

### 오늘의 질문(Today’s Question)

- 직접 만든 **질문 더미 데이터(약 100개)** 를 DB에 저장
  - 질문 내용
  - 카테고리(예: 감정, 목표, 관계 등)

- 홈 화면의 “오늘의 질문” 카드에 표시
  - `GET /questions/today` 또는 랜덤/날짜 기반 로직으로 1개 조회
  - “질문 바꾸기” 버튼으로 다른 질문으로 새로고침 가능(구현/계획)

---

### 홈 화면(Frontend)

- **헤더 영역**
  - 타이틀: `오늘의 다이어리`
  - 우측: 로그인한 유저의 닉네임 표시
  - `로그아웃` 버튼

- **메인 레이아웃**
  - 브라우저 너비에 맞춰 전체 화면을 가득 채우도록 CSS 구성
  - 주요 섹션(카드)들:
    1. **오늘의 질문 카드**
       - 질문 내용
       - 카테고리/부가 정보
       - 질문 새로고침 버튼(구현/계획)
    2. **명언 카드**
       - 명언 텍스트, 저자
       - 명언 바꾸기 버튼
       - 북마크 버튼
    3. **일기 카드**
       - 오늘 일기 작성/수정 영역
       - “내 최근 일기” 리스트
         - 제목, 내용 일부, 작성/수정 날짜 및 시간
         - 수정/삭제 버튼

- **정적 파일 구성**
  - `frontend/templates/home.html`
  - `frontend/static/style.css`
  - `frontend/static/home.js`

---

## 기술 스택

### Backend

- Python 3.11+
- FastAPI
- Uvicorn (ASGI 서버)
- Tortoise ORM
- Aerich (마이그레이션 도구)
- PostgreSQL
- python-jose (JWT 발급/검증)
- passlib[bcrypt] (비밀번호 해시)
- python-dotenv (환경 변수 로딩)
- requests, beautifulsoup4 (명언 스크래핑)

### Frontend

- HTML5 (Jinja2 템플릿)
- CSS (커스텀 스타일)
- JavaScript (ES6)
- Fetch API (백엔드와 비동기 통신)

### 개발 도구 및 기타

- 패키지 매니저: `uv`
- 가상환경: `.venv` (uv 관리)
- 코드 스타일/정적 분석: `ruff`
- DB 클라이언트: `psql`, 기타 GUI 툴

---

## 프로젝트 구조

실제 예시 구조 (변경 가능):

```bash
diary-quote-service/
├── app/
│   ├── __init__.py
│   ├── main.py                # FastAPI 진입점
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py            # 회원가입/로그인/로그아웃
│   │   ├── diary.py           # 일기 CRUD
│   │   ├── quote.py           # 명언 관련 API
│   │   └── question.py        # 오늘의 질문 API (선택)
│   ├── core/
│   │   ├── __init__.py
│   │   ├── security.py        # JWT 발급/검증, 비밀번호 해시 함수 등
│   │   └── auth.py            # get_current_user, 토큰 검증 로직
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py            # User, TokenBlacklist 모델
│   │   ├── diary.py           # Diary 모델
│   │   ├── quote.py           # Quote, Question 모델 등
│   │   └── ...
│   ├── schemas/               # Pydantic 스키마
│   ├── services/              # 도메인 로직(선택)
│   ├── scraping/
│   │   └── scrape_quotes.py   # 명언 스크래핑 스크립트
│   └── database.py            # Tortoise ORM 설정(TORTOISE_ORM)
├── frontend/
│   ├── templates/
│   │   └── home.html          # 홈 화면 템플릿
│   └── static/
│       ├── style.css          # CSS
│       └── home.js            # 홈 화면 JS
├── migrations/                # Aerich 마이그레이션 파일
├── .env                       # 환경 변수 (개발용)
├── pyproject.toml             # uv, ruff, aerich 설정
└── README.md
