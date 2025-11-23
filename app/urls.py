from django.urls import path

from . import views

urlpatterns = [
    path("", views.cat_list, name="cat_list"),
    path("about/", views.about_us, name="about_us"),
    path("help/", views.how_to_help, name="how_to_help"),
    path("cat/<int:cat_id>", views.cat_detail, name="cat_detail"),
]