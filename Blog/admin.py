from django.contrib import admin
from .models import Post
from .models import BlogComment

# Register your models here.

admin.site.register((Post,BlogComment))
