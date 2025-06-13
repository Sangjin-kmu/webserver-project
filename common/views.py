from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils import timezone
import datetime
from .models import Book, Comment, Rating, BorrowHistory
from .forms import CommentForm, RatingForm, BookForm





# ---------- 책 상세 ----------

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    viewed_flag = f'viewed_book_{book_id}'
    if request.method == "GET" and not request.session.get(viewed_flag):
        book.increase_views()
        request.session[viewed_flag] = True

    comments = book.comments.all().order_by('-created_at')
    form = CommentForm()
    rating_form = None
    user_rating = None
    is_borrowed = book.is_borrowed()
    current_borrow = book.get_current_borrower()
    is_borrowed_by_user = current_borrow and current_borrow.user == request.user

    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(book=book, user=request.user).first()

        if request.method == "POST":
            if 'content' in request.POST:
                form = CommentForm(request.POST)
                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.book = book
                    comment.user = request.user
                    comment.save()
                    return redirect('common:book_detail', book_id=book.id)

            elif 'score' in request.POST:
                rating_form = RatingForm(request.POST)
                if rating_form.is_valid() and not user_rating:
                    rating = rating_form.save(commit=False)
                    rating.book = book
                    rating.user = request.user
                    rating.save()
                    return redirect('common:book_detail', book_id=book.id)
        else:
            rating_form = RatingForm()

    context = {
        'book': book,
        'form': form,
        'comments': comments,
        'avg_rating': book.get_average_rating(),
        'user_rating': user_rating,
        'rating_form': rating_form,
        'is_borrowed': is_borrowed,
        'current_borrow': current_borrow,
        'is_borrowed_by_user': is_borrowed_by_user,
    }
    return render(request, 'book_detail.html', context)


# ---------- 대출 ----------
@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if not book.is_borrowed():
        BorrowHistory.objects.create(book=book, user=request.user)
    return redirect('common:book_detail', book_id=book.id)


# ---------- 반납 ----------
@login_required
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    borrow = BorrowHistory.objects.filter(book=book, user=request.user, returned_at__isnull=True).first()
    if borrow:
        borrow.returned_at = timezone.now()
        borrow.save()
    return redirect('common:book_detail', book_id=book.id)


# ---------- 책 목록 ----------
def book_list(request):
    keyword = request.GET.get('q', '')
    order = request.GET.get('order', '')
    books = Book.get_all_books()
    if keyword:
        books = Book.get_books_by_title_keyword(keyword)
    if order == 'title':
        books = books.order_by('title')
    return render(request, 'book_list.html', {'books': books, 'keyword': keyword, 'order': order})


# ---------- 책 등록 ----------
def book_add(request):
    if not request.user.is_authenticated:
        return render(request, 'book_add.html', {'not_logged_in': True})

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()
    return render(request, 'book_add.html', {'form': form})


# ---------- 대출 기록 보기 ----------
@login_required
def borrow_history_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    history = book.borrowhistory_set.order_by('-borrowed_at')

    context = {
        'book': book,
        'history': history,
    }
    return render(request, 'borrow_history.html', context)


# ---------- 로그인 ----------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('common:home')
        else:
            messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
    return render(request, 'login.html')  # ✅ 수정: common/login.html → login.html



@login_required
def home_view(request):
    borrowed_books = BorrowHistory.objects.filter(user=request.user).order_by('-borrowed_at')
    return render(request, 'home.html', {
        'user': request.user,
        'borrowed_books': borrowed_books,
    })



def logout_view(request):
    logout(request)
    return redirect('common:login')


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('common:home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})  # ✅ 수정: common/signup.html → signup.html


# ---------- 요청 정보 ----------

# views.py
def request_info_view(request):
    recent_requests = reversed(request.session.get('request_log', [])[-30:])
    context = {
        'method': request.method,
        'get_data': request.GET,
        'post_data': request.POST,
        'user': request.user,
        'is_logged_in': request.user.is_authenticated,
        'session_value': request.session.get('demo', '없음'),
        'user_agent': request.META.get('HTTP_USER_AGENT', '알 수 없음'),
        'client_ip': request.META.get('REMOTE_ADDR', '알 수 없음'),
        'path': request.path,
        'full_url': request.build_absolute_uri(),
        'recent_requests': recent_requests
    }
    return render(request, 'request_info.html', context)
