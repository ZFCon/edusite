from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from account.models import Account, Student, Teacher, OAdmin


class AccountAdmin(UserAdmin):
	list_display = ('email','username','user_type', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username',) 
	readonly_fields=('last_login',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

    

admin.site.register(Account, AccountAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(OAdmin)
