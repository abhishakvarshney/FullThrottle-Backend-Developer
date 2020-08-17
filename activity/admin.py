from django.contrib import admin
from activity.models import User, UserActivity

# Register your models here.
admin.site.register(User)
admin.site.register(UserActivity)