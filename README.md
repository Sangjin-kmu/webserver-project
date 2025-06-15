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
  
