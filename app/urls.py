from django.urls import path

from . import views

urlpatterns = [
    path("", views.cat_list, name="cat_list"),
    path("about/", views.about_us, name="about_us")
]