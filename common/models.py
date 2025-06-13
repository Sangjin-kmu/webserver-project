from django.db import models
from django.db.models import QuerySet
from django.contrib.auth.models import User

# ---------- Book 모델 ----------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=20, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return f"{self.title} by {self.author}"

    @classmethod
    def get_all_books(cls) -> QuerySet['Book']:
        return cls.objects.all()

    @classmethod
    def get_books_by_author(cls, author_name: str) -> QuerySet['Book']:
        return cls.objects.filter(author__iexact=author_name)

    @classmethod
    def get_books_by_title_keyword(cls, keyword: str) -> QuerySet['Book']:
        return cls.objects.filter(title__icontains=keyword)

    @classmethod
    def get_books_ordered_by_title(cls) -> QuerySet['Book']:
        return cls.objects.all().order_by('title')

    def get_average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(r.score for r in ratings) / ratings.count(), 1)
        return 0

    def is_borrowed(self):
        return self.borrowhistory_set.filter(returned_at__isnull=True).exists()

    def get_current_borrower(self):
        return self.borrowhistory_set.filter(returned_at__isnull=True).first()

    def get_status(self):
        return "대출 중" if self.is_borrowed() else "대출 가능"

# ---------- 댓글 모델 ----------
class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} on {self.book.title}"

# ---------- 별점 모델 ----------
class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()

    class Meta:
        unique_together = ('book', 'user')

# ---------- 대출 기록 모델 ----------
class BorrowHistory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({'미반납' if not self.returned_at else '반납됨'})"
