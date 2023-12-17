from django.contrib import admin
from home.models import user,post, comment, saved, userSetting

# Register your models here.
admin.site.register (user)
admin.site.register (post)
admin.site.register (comment)
admin.site.register (saved)
admin.site.register (userSetting)
