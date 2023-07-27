from django.urls import path
from .views import helloAPI
from .views import booksAPI
from .views import bookAPI

urlpatterns = [
    path('hello/', helloAPI),  # /example/hello/ 요청이 오면 helloAPI 함수가 처리
    path('fbv/books', booksAPI),  # /example/fbv/books/ 요청이 오면 booksAPI 함수가 처리
    path('fbv/book/<int:bid>', bookAPI)
]