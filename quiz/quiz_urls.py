from django.urls import path
from .views import base, quiz, upload, score, team

urlpatterns = [
    path('', base, name='base'),
    path('quiz', quiz, name='quiz'),
    path('upload', upload, name='upload'),
    path('score', score, name='score'),
    path('team', team, name='team'),
]
