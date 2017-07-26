from datetime import date
from django.shortcuts import render


# Create your views here.
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
    edu_list = [
        {
            'years': '1991-1994',
            'place': 'Техасский университет в Остине',
            'position': 'Студент',
        },
        {
            'years': '1995-1996',
            'place': 'Университет Гейдельберга в Германии',
            'position': 'Кандидат наук',
        },
    ]
    return render(request, 'edu.html', {'nbar': 'edu', 'name': name, 'edu_places': edu_list})

def work_view(request):
    name = 'Работа'
    works_list = [
        {
            'years': '1996',
            'place': 'Университет Гейдельберга в Германии',
            'position': 'Приглашенный профессор',
        },
        {
            'years': '1996-',
            'place': 'Калифорнийский технологический институт',
            'position': 'физик-теоретик',
        },
    ]
    return render(request, 'work.html', {'nbar': 'work', 'name': name, 'work_places': works_list})
