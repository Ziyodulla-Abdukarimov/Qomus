from django.shortcuts import render, redirect
from tablib import Dataset
from .models import Quiz, Score
from accounts.models import CustomUser


# Create your views here.
def base(request):
    return render(request, 'base.html')


def quiz(request):
    if request.method == 'POST':
        quiz_number = request.POST.get('quiz_number')
        ans_number = request.POST.get('number')

        if ans_number == str(Quiz.objects.get(id=quiz_number).true):
            #  Update User Rank Field
            user = CustomUser.objects.get(id=request.user.id)
            user.client.rank += 1
            user.client.save()
        else:
            # Update User Rank equal to zero rank = 0
            user = CustomUser.objects.get(id=request.user.id)
            Score(user=user.client, res_rank=user.client.rank, ans_time=0).save()

            temp_rank = user.client.rank

            user.client.rank = 1
            user.client.save()
            context = {
                'rank': temp_rank,
            }
            return render(request, 'wrong.html', context=context)

    user = CustomUser.objects.get(id=request.user.id)
    range = user.client.rank
    context = {
        'quiz': Quiz.objects.filter(question_range=range).order_by('?').first(),
        'user': user.client.rank,
    }
    return render(request, 'quiz.html', context=context)


def score(request):
    context = {
        'score': Score.objects.all(),
    }
    return render(request, 'score.html', context=context)


def upload(request):
    if request.method == 'POST':
        dataset = Dataset()
        new_book = request.FILES['file']

        imported_data = dataset.load(new_book.read(), format='xlsx')
        for data in imported_data:
            value = Quiz(
                question=data[1],
                answer1=data[2],
                answer2=data[3],
                answer3=data[4],
                answer4=data[5],
                true=data[6],
                question_range=data[7],
            )
            value.save()
    return render(request, 'upload.html')
