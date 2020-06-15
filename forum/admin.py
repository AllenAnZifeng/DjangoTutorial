from django.contrib import admin
from .models import ForumUser,Comments,Posts,Threads
# Register your models here.

admin.site.register(ForumUser)
admin.site.register(Comments)
admin.site.register(Posts)
admin.site.register(Threads)
