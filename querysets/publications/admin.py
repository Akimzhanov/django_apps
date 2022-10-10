from django.contrib import admin
from .models import Publication, Comment


"""
admin.py - файл отвечающий за работу с админ понелью
"""
admin.site.register(Publication)
admin.site.register(Comment)
