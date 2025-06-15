from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'common'

urlpatterns = [
    # 인증 관련
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),

    # 홈 & 메인
    path('', views.book_list, name='book_list'),  # 루트: 책 목록
    path('home/', views.home_view, name='home'),

    # 책 관련
    path('add/', views.book_add, name='book_add'),  # 책 추가
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),  # 상세
    path('book/<int:book_id>/history/', views.borrow_history_view, name='borrow_history'),
    path('book/<int:book_id>/borrow/', views.borrow_book, name='borrow_book'),
    path('book/<int:book_id>/return/', views.return_book, name='return_book'),

    # 요청 정보
    path('request-info/', views.request_info_view, name='request_info'),
]

# 개발용 미디어 파일 서빙
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
