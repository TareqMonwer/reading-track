from django.urls import path
from .views import home, note_details
# from .views import portfolio

urlpatterns = [
    path('', home, name='home-page'),
    path('note/<int:note_id>/', note_details, name='note-details'),
    # path('profile/', portfolio, name='portfolio-page'),
]