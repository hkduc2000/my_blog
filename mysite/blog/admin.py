from django.contrib import admin
from blog.models import Comment,Post,Notification
# Register your models here.
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Notification)
