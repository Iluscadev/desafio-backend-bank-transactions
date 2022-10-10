from django.urls import path

from transactions import views

urlpatterns = [
    path("transactions/", views.TransactionView.as_view()),
    
]
