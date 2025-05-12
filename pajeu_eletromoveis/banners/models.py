from django.db import models

class Banner(models.Model):
    TIPO_CHOICES = [
        ('desktop', 'Desktop'),
        ('mobile', 'Mobile'),
    ]
    
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='banners/')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    link = models.URLField(blank=True, null=True)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
        ordering = ['-data_criacao']