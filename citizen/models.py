from django.db import models


class CitizenModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    published_on = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Citizen Articles'
        verbose_name_plural = 'Citizen Articles'

    def __str__(self):
        return self.title
