from django.urls import path

from transactions import views

urlpatterns = [
    path("transactions/", views.TransactionView.as_view(), name = "list"),
    path("transactions/<str:transaction_id>/", views.TransactionRetrieveView.as_view(), name="retrieve"),
]
