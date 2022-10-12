from django.urls import path

from users import views

urlpatterns = [
    path("users/", views.RegisterView.as_view(), name="create"),
    
]
