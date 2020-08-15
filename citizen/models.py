from django.db import models


class CitizenModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    published_on = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    order_by = models.DateTimeField(null=True, blank=True)
    image_urls = models.TextField(null=True)
    images = models.TextField(null=True)
    path = models.CharField(null=True, blank=True, max_length=300)
    checksum = models.CharField(null=True, blank=True, max_length=300)
    status = models.CharField(null=True, blank=True, max_length=300)
    url = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = 'Citizen Articles'
        verbose_name_plural = 'Citizen Articles'

    def __str__(self):
        return self.title
