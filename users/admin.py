from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Profile, CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'role']
    fieldsets = (
        (('User'), {'fields': ('username', 'email','password', 'role')}),
    )

#Customize the admin site header and title
admin.site.site_header = "SuperUser Admin Portal ";
admin.site.site_title = "Admin Portal ";
admin.site.index_title = "Welcome to Administrator Portal ";

#add these models to the admin page
admin.site.register(CustomUser, CustomUserAdmin)

#hide these models on the admin page
admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.unregister(EmailAddress)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)
