from django.urls import path
from juntagrico_polling import views

urlpatterns = [
    path('poll/', views.poll, name='poll'),
    path('poll/vote/<int:poll_id>/<int:choice>/', views.poll, name='vote'),
    path('poll/results/', views.results),
]
