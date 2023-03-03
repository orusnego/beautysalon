from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Master, Review, Work
from django.shortcuts import get_object_or_404, redirect
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from zapis.telegrambot import *

 
def detail(request, master_id):
    master = get_object_or_404(Master,pk=master_id)
    reviews = Review.objects.filter(master=master)
    return render(request, 'detail.html',
        {'master':master, 'reviews':reviews})

def masters(request):
    masters = Master.objects.all()
    return render(request, 'masters.html', {'masters': masters})


@login_required
def createreview(request, master_id):
    master = get_object_or_404(Master,pk=master_id)
    if request.method == 'GET':
        return render(request, 'createreview.html',
        {'form':ReviewForm(), 'master': master})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.master = master
            newReview.save()
            send_message(chat_id='197670320', text=f'Новый отзыв от {newReview.name}\nМастер:{newReview.master}\nОценка мастеру: {newReview.rate}\nОтзыв: {newReview.text}')
            
            return redirect('detail', newReview.master.id)
        except ValueError:
            return render(request, 'createreview.html',
            {'form':ReviewForm(),'error':'Введены неверные данные'})

@login_required
def updatereview(request, review_id):
    review = get_object_or_404(Review,pk=review_id,user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatereview.html',
        {'review': review,'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.master.id)
        except ValueError:
            return render(request,
            'updatereview.html',
            {'review': review,'form':form,
            'error':'Введены неверные данные'})

@login_required
def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('detail', review.master.id)
# Create your views here.
