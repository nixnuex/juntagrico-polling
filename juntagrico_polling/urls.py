from django.urls import path
from juntagrico_polling import views

urlpatterns = [
    path('poll/', views.poll),
    path('poll/vote/<int:poll_id>/<int:choice>/', views.poll),
    path('poll/results/', views.results),
]
