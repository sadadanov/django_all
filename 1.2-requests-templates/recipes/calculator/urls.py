from django.urls import path, include, re_path, reverse
from .views import *
urlpatterns = [
    # path('', recipe, name='recipe'),
    re_path(r'(?P<rec>[\w]*)/?', recipe, name='recipe')

]