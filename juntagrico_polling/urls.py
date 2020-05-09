from django.urls import path
from juntagrico_polling import views

app_name = 'polling'
urlpatterns = [
    path('poll/', views.poll_list, name='list'),
    path('poll/vote/<int:poll_id>/<int:choice>/', views.submit_vote, name='vote'),
    path('poll/results/', views.results),
]
