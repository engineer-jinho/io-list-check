from django.shortcuts import render, get_object_or_404
from .models import AIModel, DIModel, DOModel, AOModel

def home(request):
    ais = AIModel.objects.all()
    dis = DIModel.objects.all()
    dos = DOModel.objects.all()
    aos = AOModel.objects.all()
    return render(request, 'io_app/home.html', {'ais': ais, 'dis': dis, 'dos': dos, 'aos': aos})

def ai_detail(request, pk):
    ai = get_object_or_404(AIModel, pk=pk)
    next_ai = AIModel.objects.filter(pk__gt=pk).order_by('pk').first()
    prev_ai = AIModel.objects.filter(pk__lt=pk).order_by('-pk').first()
    return render(request, 'io_app/ai_detail.html', {'ai': ai, 'next_ai': next_ai, 'prev_ai': prev_ai})

def ai_detail_hmi(request, pk):
    ai = get_object_or_404(AIModel, pk=pk)
    next_ai = AIModel.objects.filter(pk__gt=pk).order_by('pk').first()
    prev_ai = AIModel.objects.filter(pk__lt=pk).order_by('-pk').first()
    return render(request, 'io_app/ai_detail_hmi.html', {'ai': ai, 'next_ai': next_ai, 'prev_ai': prev_ai})

def di_detail(request, pk):
    di = get_object_or_404(DIModel, pk=pk)
    next_di = DIModel.objects.filter(pk__gt=pk).order_by('pk').first()
    prev_di = DIModel.objects.filter(pk__lt=pk).order_by('-pk').first()
    return render(request, 'io_app/di_detail.html', {'di': di, 'next_di': next_di, 'prev_di': prev_di})

def do_detail(request, pk):
    do = get_object_or_404(DOModel, pk=pk)
    next_do = DOModel.objects.filter(pk__gt=pk).order_by('pk').first()
    prev_do = DOModel.objects.filter(pk__lt=pk).order_by('-pk').first()
    return render(request, 'io_app/do_detail.html', {'do': do, 'next_do': next_do, 'prev_do': prev_do})

def ao_detail(request, pk):
    ao = get_object_or_404(AOModel, pk=pk)
    next_ao = AOModel.objects.filter(pk__gt=pk).order_by('pk').first()
    prev_ao = AOModel.objects.filter(pk__lt=pk).order_by('-pk').first()
    return render(request, 'io_app/ao_detail.html', {'ao': ao, 'next_ao': next_ao, 'prev_ao': prev_ao})

