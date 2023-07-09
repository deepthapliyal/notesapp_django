# todo_list/todo_app/admin.py

from django.contrib import admin
from api.models import Item

admin.site.register(Item)

