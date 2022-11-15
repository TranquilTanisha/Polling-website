from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('register/', views.checkDiv, name='check-div'),
    path('register-user-A/', views.registerA, name='register-user-A'),
    path('register-user-B/', views.registerB, name='register-user-B'),
    path('a-home/', views.homeA, name='a-home'),
    path('b-home/', views.homeB, name='b-home'),
    path('a-view-polls/', views.viewPollsA, name='a-view-polls'),
    path('b-view-polls/', views.viewPollsB, name='b-view-polls'),
    path('a-vote/<str:pk>/', views.voteA, name='a-vote'),
    path('b-vote/<str:pk>/', views.voteB, name='b-vote'),
    path('result_a/',views.resultA, name='result-A'),
    path('result_b/',views.resultB, name='result-B'),
    path('piechart_a/<str:pk>',views.piechartA, name='piechart-A'),
    path('piechart_b/<str:pk>',views.piechartB, name='piechart-B'),
]
