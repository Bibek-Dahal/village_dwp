from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from user_account.models import MyUser


class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('full_name','email', 'first_name','last_name','phone_num','is_superuser')
    search_fields = ('email', 'first_name', 'last_name',)
    list_filter = ('is_superuser','is_active',)
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name','middle_name','last_name')}),
        ('contact info',{'fields':('phone_num',)}),
        ('Permissions', {'fields': ('is_superuser','is_staff','is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','first_name','middle_name','last_name','phone_num','password1', 'password2'),
        }),
    )

    filter_horizontal = ()



# Now register the new UserAdmin...
admin.site.register(MyUser, MyUserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.

