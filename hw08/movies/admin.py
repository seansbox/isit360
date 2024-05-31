from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Celeb, Genre, Movie

admin.site.site_header = "Yummy Tomatoes Administration"  # default: "Django Administration"
admin.site.index_title = "Site administration"  # default: "Site administration"
admin.site.site_title = "Yummy Tomatoes admin"  # default: "Django site admin"


class CelebAdmin(ImportExportModelAdmin):
    list_display = ("name", "birthday", "birthplace")
    search_fields = ["name", "summary"]
    ordering = ("name",)


class GenreAdmin(ImportExportModelAdmin):
    ordering = ("name",)


class MovieAdmin(ImportExportModelAdmin):
    list_display = ("name", "release", "meter", "score")
    search_fields = ["name", "summary"]
    ordering = ("-meter",)


admin.site.register(Celeb, CelebAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
