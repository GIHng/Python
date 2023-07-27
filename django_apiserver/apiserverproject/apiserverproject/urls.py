from django.contrib import admin
from django.urls import path, include
from apiserverapplication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # example로 시작하는 url은 apiserverapplication.urls.py 파일에서 처리
    path('example/', include("apiserverapplication.urls")),
    path('ajax/', views.ajax)
]

