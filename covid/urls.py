from django.contrib import admin
from django.urls import path
from app.views import IndexView

urlpatterns = [
    path('', IndexView.as_view())
]
