from django.urls import path
from .views import draw_menu, home

urlpatterns = [
    path('', home, name='main_menu'),
    path('<path:path>/', draw_menu, name='draw_menu'),
]
