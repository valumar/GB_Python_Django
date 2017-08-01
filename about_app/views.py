from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Work, Education, Organization


def main_view(request):
    name = 'Обо мне'
    about_dict = {
        'state': 'Техас',
        'city': 'Галвестон',
        'birthday': date(1980, 2, 26),
        'additional_info': '''Хорошо владею не только физикой, но и
химией, биологией, астрономией, математикой, программированием, историей, географией, знаю
несколько языков, в том числе китайский, арабский и клингонский.'''
    }
    return render(request, 'index.html', {'nbar': 'home', 'name': name, 'about_dict': about_dict})


def edu_view(request):
    name = 'Образование'
    edu_list = Education.objects.all()
    return render(request, 'edu.html', {'nbar': 'edu', 'name': name, 'edu_places': edu_list})


def work_view(request):
    name = 'Работа'
    works_list = Work.objects.all()
    return render(request, 'work.html', {'nbar': 'work', 'name': name, 'work_places': works_list})


def work_detail(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    return render(request, 'work_detail.html', {'organization': organization})
