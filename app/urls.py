from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'Ritvik',views.Data.as_view()),
]