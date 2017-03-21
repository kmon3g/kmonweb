from django.contrib import admin
from .models import Entry
from .models import Category
from .models import Comment
from .models import TagModel
from .models import Photo
# Register your models here.
admin.site.register(Entry)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(TagModel)
admin.site.register(Photo)