from django.shortcuts import render
from django.http import HttpResponse
from .models import Beauty
from masters.models import Review, Master, Work
from django.shortcuts import get_object_or_404, redirect



def home(request):
    reviews = Review.objects.all()
    return render(request, 'home.html',
    {'reviews':reviews})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

def about(request):
    return render(request, 'about.html')

def allreviews(request):
    searchTerm = request.GET.get('searchReview')
    if searchTerm:
        reviews = Review.objects.filter(name__icontains=searchTerm)
    else:
        reviews = Review.objects.all()
    return render(request, 'allreviews.html',
    {'searchTerm':searchTerm,'reviews':reviews})

def allworks(request):
    searchTerm = request.GET.get('searchWork')
    if searchTerm:
        works = Work.objects.filter(master__name__icontains=searchTerm)
    else:
        works = Work.objects.all()
    return render(request, 'allworks.html',
    {'searchTerm':searchTerm,'works':works})


def brows(request):
    procedures = Beauty.objects.all()
    return render(request, 'uslugi.brovi.html',
    {'procedures':procedures})

def procedures_detail(request, procedure_id):
    procedure = get_object_or_404(Beauty,pk=procedure_id)
    works = Work.objects.filter(procedure=procedure)
    return render(request, 'procedure.detail.html',
        {'procedure':procedure, 'works':works})

def lashes(request):
    procedures = Beauty.objects.all()
    return render(request, 'uslugi.resn.html',
    {'procedures':procedures})

def nails(request):
    procedures = Beauty.objects.all()
    return render(request, 'uslugi.nogti.html',
    {'procedures':procedures})

def hair(request):
    procedures = Beauty.objects.all()
    return render(request, 'uslugi.hair.html',
    {'procedures':procedures})

