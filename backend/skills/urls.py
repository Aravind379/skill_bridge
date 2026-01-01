from django.urls import path
from .views import skill_gap

urlpatterns = [
    path('gap/', skill_gap),
]
