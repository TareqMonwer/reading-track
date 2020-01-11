from django.urls import path

from .views import Reading, WishList, Completed


urlpatterns = [
    path('reading/', Reading.as_view(), name='reading-list'),
    path('completed/', Completed.as_view(), name='completed-list'),
    path('wishlist/', WishList.as_view(), name='wish-list'),
]