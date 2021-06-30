from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=255)
    keterangan = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategori"

class Artikel(models.Model):
    judul = models.CharField(max_length=255)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='image')
    body = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.judul
    
    class Meta:
        verbose_name = "Artikel"
        verbose_name_plural = "Artikel"
