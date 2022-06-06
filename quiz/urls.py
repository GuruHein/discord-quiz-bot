from django.urls import path
from . import views

urlpatterns = [
    path('random/', views.QuestionAPIView.as_view(), name='question'),
]
