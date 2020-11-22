from django.shortcuts import render
from django.utils import timezone
from .models import Quiz

# Create your views here.
def solv_quiz(request):
    quizzes = Quiz.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'quiz_service/solv_quiz.html', {'quizzes': quizzes})

def register(request):
    return render(request, 'quiz_service/register.html', {})

def index(request):
    return render(request, 'quiz_service/index.html', {})
