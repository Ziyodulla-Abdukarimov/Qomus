from django.urls import path
from .views import base, quiz, upload, score

urlpatterns = [
    path('', base),
    path('quiz', quiz, name='quiz'),
    path('upload', upload, name='upload'),
    path('score', score, name='score'),
]
