# 2025-06-13 국민대학교 웹서버 컴퓨팅 팀:콰삭킹(배경준, 이상진, 황찬우)
# 수업때 진행한 기존 도서사이트 리뉴얼  
  
## 디렉토리 구조
```
kwasaking_code/
├── 콰삭킹-코드/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── .gitignore
│   ├── pybo/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views/
│   │   │   ├── base_views.py
│   │   │   ├── question_views.py
│   │   │   ├── answer_views.py
│   │   │   ├── comment_views.py
│   │   │   ├── vote_views.py
│   │   ├── templatetags/
│   │   │   ├── pybo_filter.py
│   │   ├── migrations/
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_question_author.py
│   │   │   ├── 0003_answer_author.py
│   │   │   ├── 0004_auto_20200507_1149.py
│   │   │   ├── 0005_comment.py
│   │   │   ├── 0006_auto_20200507_1449.py
│   │   │   ├── 0007_alter_answer_id_alter_comment_id_alter_question_id.py
│
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   ├── asgi.py
│
│   ├── common/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── forms.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── middleware.py
│   │   ├── templatetags/
│   │   │   ├── markdown_comments.py
│   │   ├── migrations/
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_book_views.py
│   │   │   ├── 0003_comment.py
│   │   │   ├── 0004_book_category_book_description_book_image_book_isbn_and_more.py
│   │   │   ├── 0005_borrowhistory.py
│
│   ├── static/
│   │   ├── bootstrap.min.css
│   │   ├── bootstrap.min.js
│   │   ├── jquery-3.4.1.min.js
│   │   ├── style.css
│
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── navbar.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── book_list.html
│   │   ├── book_detail.html
│   │   ├── book_add.html
│   │   ├── borrow_history.html
│   │   ├── request_info.html
│   │   ├── form_errors.html
│   │   ├── pybo/
│   │   │   ├── question_list.html
│   │   │   ├── question_detail.html
│   │   │   ├── question_form.html
│   │   │   ├── answer_form.html
│   │   │   ├── comment_form.html
│   │   ├── common/
│   │   │   ├── login.html
│   │   │   ├── signup.html
│
│   ├── media/
│   │   ├── book_covers/
│   │   │   ├── 이미지

```  
  
## 주요 코드 설명  
### config/
Django 프로젝트의 전역 설정을 담당하는 폴더입니다.  
 
settings.py: 프로젝트 설정 파일로, 앱 등록, 데이터베이스 설정, 정적 파일 및 미디어 파일 경로, 인증 시스템 등이 정의되어 있습니다.

urls.py: 최상위 URL 라우팅 설정 파일입니다. 각 앱의 URLconf를 include하여 전체 라우팅을 구성합니다.

wsgi.py / asgi.py: 배포 시 사용하는 서버 인터페이스 설정 파일입니다.

pybo/
질문과 답변, 댓글, 별점 등의 게시판 기능이 구현된 핵심 앱입니다.

models.py: 질문, 답변, 댓글, 별점 등의 데이터 모델이 정의되어 있습니다. 작성자, 생성일, 수정일, 외래키 관계 등이 설정되어 있습니다.

views/: 기능별로 분리된 뷰 로직이 포함되어 있습니다.

base_views.py: 메인 페이지, 목록 출력 등 기본 페이지 처리

question_views.py: 질문 등록, 수정, 삭제 처리

answer_views.py: 답변 등록, 삭제 처리

comment_views.py: 댓글 작성, 수정, 삭제 처리 및 마크다운 렌더링

vote_views.py: 추천 및 별점 기능 처리

forms.py: 질문, 답변, 댓글 등의 폼이 정의되어 있으며 사용자 입력 검증을 담당합니다.

urls.py: pybo 앱 내부 URL 라우팅을 정의합니다.

templatetags/pybo_filter.py: 댓글 및 게시글 본문에서 마크다운을 HTML로 변환하는 템플릿 필터가 정의되어 있습니다.

migrations/: 데이터베이스 스키마 변경 이력을 관리하는 마이그레이션 파일들이 포함되어 있습니다.

common/
사용자 인증, 마크다운 필터, 요청 기록 미들웨어 등 공통 기능을 담당하는 핵심 앱입니다.

views.py: 회원가입, 로그인, 로그아웃과 같은 사용자 인증 로직이 포함되어 있습니다. 로그인 성공 시 사용자 홈으로 리디렉션되며, 실패 시 오류 메시지를 제공합니다.

forms.py: Django의 기본 UserCreationForm을 기반으로 회원가입 폼을 구성하며, 사용자 입력 필드 구성을 커스터마이징합니다.

urls.py: 인증 관련 URL(/login/, /logout/, /signup/)을 처리합니다.

middleware.py: 사용자의 요청 정보를 기록하는 미들웨어가 정의되어 있습니다. 사용자가 어떤 경로에 언제 접근했는지를 로그로 저장하여 사용자 활동 분석에 활용됩니다.

templatetags/markdown_comments.py: 댓글에서 입력된 마크다운을 HTML로 변환하는 필터가 정의되어 있습니다. 보안 강화를 위해 마크다운 변환 후 불필요한 태그를 제거하는 기능도 포함될 수 있습니다. 템플릿에서는 {{ comment.content|markdown }} 형식으로 사용됩니다.

admin.py: Django 관리자 페이지에서 사용자 및 관련 모델을 관리하기 위한 설정 파일입니다.

models.py: 사용자 관련 모델 정의 또는 사용자 확장 시 사용됩니다.

migrations/: 사용자 인증 또는 공통 모델 관련 데이터베이스 스키마 변경 이력이 포함되어 있습니다.

templates/
프론트엔드에 렌더링되는 HTML 템플릿 파일들이 포함된 폴더입니다.

base.html: 모든 페이지의 공통 레이아웃을 정의하는 기본 템플릿입니다. 네비게이션 바, 공통 스타일, 스크립트 등을 포함합니다.

home.html: 로그인 후 사용자의 홈 화면

book_list.html, book_detail.html, book_add.html: 도서 목록, 상세정보, 등록 페이지 템플릿

borrow_history.html: 사용자별 대출 이력을 보여주는 페이지

request_info.html: 사용자의 요청 정보를 표시하는 로그 페이지

form_errors.html: 폼 오류 메시지를 출력하는 공통 템플릿

pybo/: 게시판 관련 템플릿 (질문 목록, 상세보기, 댓글 입력 등)

common/: 인증 관련 템플릿 (로그인, 회원가입 등)

static/
정적 자원이 저장되는 폴더로, CSS, JavaScript, 이미지 파일 등이 포함됩니다.

bootstrap.min.css, bootstrap.min.js: 부트스트랩 프레임워크

jquery-3.4.1.min.js: jQuery 라이브러리

style.css: 사용자 정의 스타일 시트

media/
사용자 업로드 파일이 저장되는 폴더입니다.

book_covers/: 도서 표지 이미지 파일들이 저장됩니다. Django 설정의 MEDIA_ROOT 경로와 연동되어 작동합니다.
## 메인화면(127.0.0.1)
<img width="985" alt="image" src="https://github.com/user-attachments/assets/31a5ffe5-5cac-44c8-9ada-3aec1311bc6e" />  
  
## 로그인 전  
  
### 책 정보(http://127.0.0.1:8000/book/8/)  
<img width="973" alt="스크린샷 2025-06-13 오후 10 31 18" src="https://github.com/user-attachments/assets/c40357ec-95cb-427b-ab2b-ce2e3a384dea" />  
  
### 책 등록(http://127.0.0.1:8000/add/)  
<img width="966" alt="image" src="https://github.com/user-attachments/assets/c48a5c1a-9ea6-4921-a16a-10fd412d305e" /> 
  
### 요청 정보(http://127.0.0.1:8000/request-info/)
<img width="676" alt="image" src="https://github.com/user-attachments/assets/8c127899-a740-4938-8048-691a71ff5967" />  
  
### 로그인(http://127.0.0.1:8000/login/)  
<img width="733" alt="image" src="https://github.com/user-attachments/assets/02a6d1ac-10ee-419d-b563-4167b47d0fb8" />  
  
### 회원가입(http://127.0.0.1:8000/signup/)
<img width="717" alt="image" src="https://github.com/user-attachments/assets/5baff390-9d93-4654-b41c-9361b6f46dfb" />  
  
## 로그인 후  
  
### 책 정보(http://127.0.0.1:8000/book/1/)
<img width="1081" alt="image" src="https://github.com/user-attachments/assets/07febe91-fe1a-46b4-b2f1-971fdd124a2d" />  
  
### 책 정보(대출 및 별점 동작 후)  
<img width="922" alt="image" src="https://github.com/user-attachments/assets/16075451-97fe-4691-8a28-88d4ed7162e2" />  
  
### 댓글(마크다운 포함)
<img width="979" alt="image" src="https://github.com/user-attachments/assets/9e69e65a-6a0d-4018-ad7f-7b4756e1456a" />  
  
### 책 대출 기록(http://127.0.0.1:8000/book/1/history/)  
<img width="942" alt="image" src="https://github.com/user-attachments/assets/8724a07e-a814-4c6c-ba75-3a2f21f6df15" />  
  
### 책 등록(http://127.0.0.1:8000/add/)  
<img width="676" alt="image" src="https://github.com/user-attachments/assets/a6712604-90b5-4370-a24c-b169f0e786a1" />  
  
### 요청 정보(http://127.0.0.1:8000/request-info/)  
<img width="656" alt="image" src="https://github.com/user-attachments/assets/ecdf6b5f-d3df-4aec-9bc1-6a59b6d7baf8" />  
  
### 내 홈(http://127.0.0.1:8000/home/)
<img width="822" alt="image" src="https://github.com/user-attachments/assets/547ae03c-def4-4438-9400-727f4d297d80" />  
  
### 깃허브 링크 : https://github.com/Sangjin-kmu/webserver-project  
  
