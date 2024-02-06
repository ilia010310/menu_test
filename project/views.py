from django.shortcuts import render

from .models import Menu


def home(request):
    return render(request, 'home.html', {'menus': Menu.objects.all()})


def draw_menu(request, path):
    splitted_path = path.split('/')
    assert len(splitted_path) > 0, ('Отрисовка не работает')
    return render(
        request, 'home.html', {'menu_name': splitted_path[0], 'menu_item': splitted_path[-1]})