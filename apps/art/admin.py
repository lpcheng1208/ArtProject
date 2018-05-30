from django.contrib import admin

# Register your models here.
from art.models import Art, Tag

admin.site.register(Art)
admin.site.register(Tag)