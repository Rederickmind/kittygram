from django.urls import include, path

from cats.views import APICat

urlpatterns = [
    path('cats/', APICat.as_view()),
]
