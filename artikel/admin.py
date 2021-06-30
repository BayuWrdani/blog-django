from artikel.models import Artikel, Kategori
from django.contrib import admin

class KategoriAdmin(admin.ModelAdmin):
    list_display = ('nama', 'keterangan')
    search_fields = ('nama',)


class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('judul', 'kategori', 'cover', 'body')
    search_fields = ('judul',)
    list_filter = ('kategori',)

    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Artikel, ArtikelAdmin)
admin.site.register(Kategori, KategoriAdmin)