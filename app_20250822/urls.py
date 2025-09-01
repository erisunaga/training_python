from django.urls import path

from . import views

app_name = "app_20250822"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
]
