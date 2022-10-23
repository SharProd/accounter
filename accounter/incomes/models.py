from django.db import models
from user.models import CustomUser
from accounter.mixins import DateTimeMixin
from django.core.validators import MinValueValidator


class Photo(models.Model):
    photo = models.ImageField(
        upload_to="image/%Y/%m/%d/",
    )

    def __str__(self):
        return f"{self.id}, path-{self.photo}"

    class Meta:
        verbose_name = "photo"
        verbose_name_plural ="photos"



class OneNote(models.Model,DateTimeMixin):
    user = models.ForeignKey(CustomUser,on_delete= models.CASCADE)
    date_in_check = models.DateTimeField()
    score = models.FloatField(validators=[MinValueValidator(0, "Min number value!")])
    photo = models.ManyToManyField(Photo)
    where_from = models.CharField(max_length=30,null=True)

    def __str__(self):
        return f'{self.pk} - {self.user} - {self.score}'

    class Meta:
        verbose_name = 'income_note'
        verbose_name_plural = 'income_notes'
        ordering = ['-date_in_check']