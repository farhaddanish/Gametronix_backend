from django.contrib import admin
from .models import Games


class GameAdmin (admin.ModelAdmin):
    list_display = ("name", "type", "size", "date_added",)
    list_display_links = ("name",)
    list_filter = ("type", "name",)

    readonly_fields = (
        "date_added",
        "date_updated",
    )
    ordering = ("-date_added",)

    filter_horizontal = ()
    exclude = ("size", "slug",)


admin.site.register(Games, GameAdmin)
