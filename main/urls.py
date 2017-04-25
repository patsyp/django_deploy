
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include ('random_word_app.urls'))
    ]