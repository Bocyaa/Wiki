from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="info"),
    path("wiki/search/", views.search, name="search"),
    path("wiki/create/", views.create, name="create"),
    path("wiki/message/<str:message>", views.message, name="message"),
    path("wiki/<str:title>/edit", views.edit, name="edit"),
    path("wiki/random/", views.random_page, name="random_page")
]
