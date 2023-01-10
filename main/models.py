from django.db import models


# Create your models here.


class Word(models.Model):
    name = models.CharField(max_length=50, verbose_name="So'z", db_index=True)
    description = models.TextField(max_length=500, verbose_name="So'z izohi", null=True, blank=True)
    description2 = models.TextField(max_length=500, verbose_name="So'z izohi2", null=True, blank=True)
    description3 = models.TextField(max_length=500, verbose_name="So'z izohi3", null=True, blank=True)
    description4 = models.TextField(max_length=500, verbose_name="So'z izohi4", null=True, blank=True)
    description5 = models.TextField(max_length=500, verbose_name="So'z izohi5", null=True, blank=True)
    description6 = models.TextField(max_length=500, verbose_name="So'z izohi6", null=True, blank=True)
    description7 = models.TextField(max_length=500, verbose_name="So'z izohi7", null=True, blank=True)
    description8 = models.TextField(max_length=500, verbose_name="So'z izohi8", null=True, blank=True)
    description9 = models.TextField(max_length=500, verbose_name="So'z izohi9", null=True, blank=True)
    description10 = models.TextField(max_length=500, verbose_name="So'z izohi10", null=True, blank=True)
    slug = models.SlugField(max_length=200, verbose_name="slug")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "So'z"
        verbose_name_plural = "So'zlar"


class Saytlar(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    text = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
