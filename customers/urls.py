from django.urls import path

from . import views

app_name = "customers"

urlpatterns = [
    path("", views.PersonListView.as_view(), name="list"),
    path("<int:pk>/", views.PersonDetailView.as_view(), name='detail')
]
