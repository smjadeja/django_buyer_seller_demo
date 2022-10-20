from django.contrib import admin
from . models import MyUser, User_Role

@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','dob','email', 'mobile','balance','password','address', 'user_role']
    fieldsets = (
        (None, {
            "fields": ('name','dob','email', 'mobile','balance','password','address','user_role' ),
        }),
    )
    

@admin.register(User_Role)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['role_name', 'role_desc']
    fieldsets = (
        (None, {
            "fields": ('role','role_desc',),
        }),
    )
