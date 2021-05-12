from django.db import models
from datetime import date
# Create your models here.


class Concurso(models.Model):

    numero = models.IntegerField()
    class Meta:
        verbose_name = _("Concurso")
        verbose_name_plural = _("Concursos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Concurso_detail", kwargs={"pk": self.pk})
