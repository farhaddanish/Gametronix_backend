from django.contrib import admin
from .models import Accounts
# Register your models here.


class AccountsAdmin (admin.ModelAdmin):

    def capitalize_firstname(self, obj):
        return obj.first_name.capitalize()

    def capitalize_lastname(self, obj):
        return obj.last_name.capitalize()

    capitalize_firstname.short_description = 'First Name'
    capitalize_lastname.short_description = 'Last Name'

    list_display = ("capitalize_firstname", "capitalize_lastname", "email",
                    "last_login", "date_joined", "is_active")

    list_display_links = ["email",]
    readonly_fields = ["last_login", "date_joined",]

    ordering = ("-date_joined",)

    filter_horizontal = ()
    list_filter = ()

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "date_joined",
                    "last_login",
                )
            },
        ),
        (
            "Personal Info",
            {
                "fields": (
                    "capitalize_firstname",
                    "capitalize_lastname",
                    "profile_photo",
                )
            }
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_admin",
                    "is_active",
                    "is_staff",
                    "is_superadmin",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "capitalize_firstname", "password1", "password2"),
            },
        ),
    )


admin.site.register(Accounts, AccountsAdmin)
