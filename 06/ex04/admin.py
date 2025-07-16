from django.contrib import admin
from .models import Tip, MyUser, Vote

admin.site.register(Tip)
admin.site.register(Vote)

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
	list_display = ('username',)
	filter_horizontal = ('groups', 'user_permissions')
