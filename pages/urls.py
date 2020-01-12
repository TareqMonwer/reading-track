from django.urls import path
from .views import home
# from .views import portfolio

urlpatterns = [
    path('', home, name='home-page'),
    # path('profile/', portfolio, name='portfolio-page'),
]